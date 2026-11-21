"""Generate animated README SVGs (light + dark) for the GitHub profile.

GitHub renders SVGs as <img>: CSS animations work, scripts and web fonts do not,
so everything uses system font stacks and pure CSS keyframes.
"""
import pathlib
import sys

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', 'Cascadia Code', Menlo, Consolas, monospace"

THEMES = {
    "dark": dict(bg="#0a0b0e", panel="#101217", line="#1d2028", line2="#2c313c", ink="#eef1f6", ink2="#a8afbd",
                 ink3="#6f7787", accent="#4d7cff", signal="#4d7cff", ok="#4d7cff", bar="#4d7cff", dot="#1d2028",
                 face="#dfe5f2", chipink="#ffffff", light=False),
    "light": dict(bg="#f7f8fa", panel="#ffffff", line="#e3e6eb", line2="#c9ced7", ink="#0d1017", ink2="#3a4150",
                  ink3="#6b7383", accent="#2753f5", signal="#2753f5", ok="#2753f5", bar="#2753f5", dot="#e3e6eb",
                  face="#1a1f2b", chipink="#ffffff", light=True),
}

REDUCED = """
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.001s !important; animation-iteration-count: 1 !important; animation-delay: 0s !important; }
}"""


def halftone(t, size=288, n=56):
    """Portrait as a dot matrix: radius from brightness, edge dots in the accent colour."""
    from PIL import Image

    img = Image.open(pathlib.Path(__file__).with_name("portrait.jpg")).convert("RGB").resize((n, n), Image.LANCZOS)
    px = img.load()
    lum = [[(0.299 * px[x, y][0] + 0.587 * px[x, y][1] + 0.114 * px[x, y][2]) / 255 for x in range(n)] for y in range(n)]
    bg = [[px[x, y][2] > px[x, y][0] * 1.25 and px[x, y][2] > 90 for x in range(n)] for y in range(n)]

    def L(x, y):
        return lum[min(n - 1, max(0, y))][min(n - 1, max(0, x))]

    step = size / n
    rows = []
    for y in range(n):
        dots = []
        for x in range(n):
            nb = sum(bg[min(n - 1, max(0, y + dy))][min(n - 1, max(0, x + dx))] for dy in (-1, 0, 1) for dx in (-1, 0, 1))
            if bg[y][x] or nb >= 6:  # backdrop, or an isolated speck next to it
                continue
            gx = L(x + 1, y) - L(x - 1, y)
            gy = L(x, y + 1) - L(x, y - 1)
            edge = (gx * gx + gy * gy) ** 0.5
            v = (1 - lum[y][x]) if t["light"] else lum[y][x]
            r = 0.3 + v * step * 0.48
            fill = t["accent"] if edge > 0.22 else t["face"]
            dots.append(f'<circle cx="{x * step + step / 2:.1f}" cy="{y * step + step / 2:.1f}" r="{r:.2f}" fill="{fill}"/>')
        rows.append(f'<g class="row" style="animation-delay:{y * 0.015:.3f}s">{"".join(dots)}</g>')
    return "".join(rows)


def header(t):
    W, H = 1200, 360
    S = 288
    ox, oy = 56, 36
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Onuralp Sezer, Senior Machine Learning Engineer at Ultralytics">
<style>
  .mono {{ font-family: {MONO}; }}
  .sans {{ font-family: {SANS}; }}
  .row {{ opacity: 0; animation: fade .5s ease-out forwards; }}
  .fade {{ opacity: 0; animation: fade .6s ease-out forwards; }}
  .d1 {{ animation-delay: .5s; }} .d2 {{ animation-delay: .7s; }} .d3 {{ animation-delay: .9s; }} .d4 {{ animation-delay: 1.1s; }}
  .box {{ stroke-dasharray: 1100; stroke-dashoffset: 1100; animation: draw 1s cubic-bezier(.2,.7,.2,1) 1.3s forwards; }}
  .tag {{ opacity: 0; animation: fade .3s ease-out 2.2s forwards; }}
  @keyframes fade {{ to {{ opacity: 1; }} }}
  @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
  {REDUCED}
</style>
<rect width="{W}" height="{H}" rx="16" fill="{t['bg']}"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="16" fill="none" stroke="{t['line']}"/>

<g transform="translate({ox} {oy})">{halftone(t, S)}</g>

<!-- detection box around the face -->
<rect class="box" x="{ox + 50}" y="{oy + 14}" width="{S - 92}" height="{S - 14}" fill="none" stroke="{t['accent']}" stroke-width="2.5"/>
<g class="tag">
  <rect x="{ox + 49}" y="{oy - 10}" width="112" height="24" fill="{t['accent']}"/>
  <text class="mono" x="{ox + 58}" y="{oy + 7}" font-size="13" font-weight="600" fill="{t['chipink']}">person 0.87</text>
</g>

<g transform="translate(420 0)">
  <text class="mono fade d1" x="0" y="104" font-size="14" fill="{t['accent']}">Senior ML Engineer · Ultralytics</text>
  <text class="sans fade d2" x="-3" y="166" font-size="58" font-weight="700" letter-spacing="-2" fill="{t['ink']}">Onuralp Sezer</text>
  <text class="sans fade d3" x="0" y="212" font-size="22" fill="{t['ink2']}">I work on YOLO and the software that runs it:</text>
  <text class="sans fade d3" x="0" y="242" font-size="22" fill="{t['ink2']}">research, training, and a Rust runtime for GPUs, phones and the web.</text>
  <g class="fade d4" font-size="13">
    <rect x="0" y="272" width="104" height="30" rx="15" fill="none" stroke="{t['line2']}"/>
    <text class="mono" x="52" y="292" text-anchor="middle" fill="{t['ink2']}">YOLO R&amp;D</text>
    <rect x="114" y="272" width="166" height="30" rx="15" fill="none" stroke="{t['line2']}"/>
    <text class="mono" x="197" y="292" text-anchor="middle" fill="{t['ink2']}">VLMs · embeddings</text>
    <rect x="290" y="272" width="166" height="30" rx="15" fill="none" stroke="{t['line2']}"/>
    <text class="mono" x="373" y="292" text-anchor="middle" fill="{t['ink2']}">PyTorch · ExecuTorch</text>
    <rect x="466" y="272" width="150" height="30" rx="15" fill="none" stroke="{t['line2']}"/>
    <text class="mono" x="541" y="292" text-anchor="middle" fill="{t['ink2']}">Fedora since 2011</text>
  </g>
</g>
</svg>
"""


def pipeline(t):
    W, H = 1200, 210
    stages = [
        ("data", "Datasets", "images · labels"),
        ("train", "PyTorch", "Ultralytics YOLO"),
        ("export", "ONNX", "ONNXSlim"),
        ("optimize", "TensorRT", "ExecuTorch · ncnn"),
        ("deploy", "Rust · Edge", "crates.io · npm"),
    ]
    n = len(stages)
    bw, bh, gap = 196, 104, 40
    x0 = (W - (n * bw + (n - 1) * gap)) / 2
    y0 = 70
    parts = []
    for i, (k, title, sub) in enumerate(stages):
        x = x0 + i * (bw + gap)
        last = i == n - 1
        stroke = t["signal"] if last else t["line2"]
        parts.append(f"""
  <g class="stage" style="animation-delay:{i * 0.9:.1f}s">
    <rect x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="12" fill="{t['panel']}" stroke="{stroke}" stroke-width="{1.5 if last else 1}"/>
    <rect class="hl" x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="12" fill="none" stroke="{t['signal']}" stroke-width="2" style="animation-delay:{i * 0.9:.1f}s"/>
    <text class="mono" x="{x + 18}" y="{y0 + 30}" font-size="12" fill="{t['signal'] if last else t['ink3']}">{i + 1:02d} {k}</text>
    <text class="sans" x="{x + 18}" y="{y0 + 62}" font-size="21" font-weight="650" fill="{t['ink']}">{title}</text>
    <text class="mono" x="{x + 18}" y="{y0 + 86}" font-size="12" fill="{t['ink3']}">{sub}</text>
  </g>""")
        if not last:
            lx1, lx2, ly = x + bw, x + bw + gap, y0 + bh / 2
            parts.append(f"""
  <line x1="{lx1}" y1="{ly}" x2="{lx2}" y2="{ly}" stroke="{t['line2']}" stroke-width="2"/>
  <line class="flow" x1="{lx1}" y1="{ly}" x2="{lx2}" y2="{ly}" stroke="{t['accent']}" stroke-width="2" style="animation-delay:{i * 0.9 + 0.45:.2f}s"/>
  <path d="M{lx2 - 7} {ly - 5} L{lx2} {ly} L{lx2 - 7} {ly + 5}" fill="none" stroke="{t['line2']}" stroke-width="2"/>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Pipeline: datasets, PyTorch training, ONNX export, TensorRT and ExecuTorch optimization, Rust and edge deployment">
<style>
  .mono {{ font-family: {MONO}; }} .sans {{ font-family: {SANS}; }}
  .hl {{ opacity: 0; animation: hl 4.5s ease-in-out infinite; }}
  .flow {{ stroke-dasharray: 10 30; stroke-dashoffset: 40; opacity: 0; animation: flow 4.5s linear infinite; }}
  @keyframes hl {{ 0% {{ opacity: 0; }} 6% {{ opacity: 1; }} 20% {{ opacity: 0; }} 100% {{ opacity: 0; }} }}
  @keyframes flow {{ 0% {{ opacity: 1; stroke-dashoffset: 40; }} 12% {{ opacity: 1; stroke-dashoffset: 0; }} 13%, 100% {{ opacity: 0; }} }}
  {REDUCED}
</style>
<rect width="{W}" height="{H}" rx="18" fill="{t['bg']}"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{t['line']}"/>
<text class="mono" x="{x0}" y="44" font-size="13" fill="{t['ink3']}">$ research ──▶ production</text>
{''.join(parts)}
</svg>
"""


def contributions(t):
    W, H = 1200, 330
    data = [("2021", 243), ("2022", 466), ("2023", 2044), ("2024", 2620), ("2025", 2320), ("2026", None)]
    left, right, top, bottom = 90, 60, 96, 270
    ph = bottom - top
    ceiling = 3000
    slot = (W - left - right) / len(data)
    bw = 56
    out = []
    for tick in (0, 1000, 2000, 3000):
        y = bottom - tick / ceiling * ph
        out.append(f'<line x1="{left}" y1="{y}" x2="{W - right}" y2="{y}" stroke="{t["line"] if tick else t["line2"]}"/>')
        out.append(f'<text class="mono" x="{left - 14}" y="{y + 4}" font-size="12" text-anchor="end" fill="{t["ink3"]}">{"0" if tick == 0 else f"{tick // 1000}k"}</text>')
    for i, (year, v) in enumerate(data):
        cx = left + slot * i + slot / 2
        out.append(f'<text class="mono" x="{cx}" y="{bottom + 26}" font-size="13" text-anchor="middle" fill="{t["ink3"]}">{year}</text>')
        if v is None:
            h = 0.4 * ph * 0.62
            out.append(f'<path class="pend" d="M{cx - bw / 2} {bottom} V{bottom - h + 4} Q{cx - bw / 2} {bottom - h} {cx - bw / 2 + 4} {bottom - h} H{cx + bw / 2 - 4} Q{cx + bw / 2} {bottom - h} {cx + bw / 2} {bottom - h + 4} V{bottom}" fill="none" stroke="{t["line2"]}" stroke-width="1.5" stroke-dasharray="5 5"/>')
            out.append(f'<text class="mono lbl" x="{cx}" y="{bottom - h - 12}" font-size="13" text-anchor="middle" fill="{t["ink2"]}" style="animation-delay:{0.3 + i * 0.15 + 0.8:.2f}s">growing…</text>')
            continue
        h = v / ceiling * ph
        d = 0.3 + i * 0.15
        x1, x2, yt = cx - bw / 2, cx + bw / 2, bottom - h
        out.append(f'<path class="bar" d="M{x1} {bottom} V{yt + 4} Q{x1} {yt} {x1 + 4} {yt} H{x2 - 4} Q{x2} {yt} {x2} {yt + 4} V{bottom} Z" fill="{t["bar"]}" style="animation-delay:{d:.2f}s"/>')
        out.append(f'<text class="mono lbl" x="{cx}" y="{bottom - h - 12}" font-size="13" text-anchor="middle" fill="{t["ink2"]}" style="animation-delay:{d + 0.8:.2f}s">{v:,}</text>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="GitHub contributions per year: 2021 243, 2022 466, 2023 2,044, 2024 2,620, 2025 2,320, 2026 in progress">
<style>
  .mono {{ font-family: {MONO}; }} .sans {{ font-family: {SANS}; }}
  .bar {{ transform-box: fill-box; transform-origin: bottom; transform: scaleY(0); animation: grow 1s cubic-bezier(.2,.7,.2,1) forwards; }}
  .lbl {{ opacity: 0; animation: fade .4s ease-out forwards; }}
  .pend {{ animation: dash 1.2s linear infinite; }}
  @keyframes grow {{ to {{ transform: scaleY(1); }} }}
  @keyframes fade {{ to {{ opacity: 1; }} }}
  @keyframes dash {{ to {{ stroke-dashoffset: -10; }} }}
  {REDUCED}
</style>
<rect width="{W}" height="{H}" rx="18" fill="{t['bg']}"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{t['line']}"/>
<text class="mono" x="40" y="42" font-size="13" fill="{t['ink3']}">contributions.plot()</text>
<text class="sans" x="40" y="72" font-size="22" font-weight="650" fill="{t['ink']}">7,693 contributions since 2021 <tspan class="mono" font-size="13" font-weight="400" fill="{t['ink3']}">  across 45+ repositories on GitHub, GitLab and Pagure</tspan></text>
{''.join(out)}
</svg>
"""


def footer(t):
    W, H = 1200, 96
    msg = "> Model 'Onuralp' successfully converged. Next objective: AGI & beyond..."
    chars = len(msg)
    cw = 9.0  # approx advance for 15px monospace
    tw = chars * cw
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{msg.replace("&", "&amp;")}">
<defs><clipPath id="type"><rect class="typer" x="0" y="0" width="0" height="{H}"/></clipPath></defs>
<style>
  .mono {{ font-family: {MONO}; }}
  .typer {{ animation: type 3.2s steps({chars}) .4s forwards; }}
  .cursor {{ animation: move 3.2s steps({chars}) .4s forwards, blink 1s steps(1) infinite; }}
  @keyframes type {{ to {{ width: {W}px; }} }}
  @keyframes move {{ from {{ transform: translateX(0); }} to {{ transform: translateX({tw:.0f}px); }} }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  {REDUCED}
</style>
<rect width="{W}" height="{H}" rx="18" fill="{t['bg']}"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{t['line']}"/>
<circle cx="34" cy="48" r="5" fill="{t['line2']}"/><circle cx="52" cy="48" r="5" fill="{t['line2']}"/><circle cx="70" cy="48" r="5" fill="{t['accent']}"/>
<g transform="translate(100 0)">
  <text class="mono" x="0" y="53" font-size="15" fill="{t['ink2']}" textLength="{tw:.0f}" lengthAdjust="spacingAndGlyphs" clip-path="url(#type)">{msg.replace("&", "&amp;").replace("'", "&#39;")}</text>
  <rect class="cursor" x="2" y="38" width="9" height="19" fill="{t['signal']}"/>
</g>
</svg>
"""


for name, fn in [("header", header), ("pipeline", pipeline), ("contributions", contributions), ("footer", footer)]:
    for mode, t in THEMES.items():
        (OUT / f"{name}-{mode}.svg").write_text(fn(t))
print("ok", sorted(p.name for p in OUT.iterdir()))
