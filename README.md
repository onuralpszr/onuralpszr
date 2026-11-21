<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/readme/header-light.svg">
  <img alt="Onuralp Sezer, Senior Machine Learning Engineer @Ultralytics" src="./assets/readme/header-dark.svg" width="100%">
</picture>

<div align="center">
  <a href="https://github.com/onuralpszr">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=4D7CFF&center=true&vCenter=true&width=600&lines=%3E_Initializing+neural+networks...;%3E_Loading+YOLO+weights...;%3E_Compiling+Rust+to+PTX...;%3E_Hello+World!+I'm+Onuralp+%F0%9F%91%8B">
      <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=2753F5&center=true&vCenter=true&width=600&lines=%3E_Initializing+neural+networks...;%3E_Loading+YOLO+weights...;%3E_Compiling+Rust+to+PTX...;%3E_Hello+World!+I'm+Onuralp+%F0%9F%91%8B">
      <img alt="Typing SVG" src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=4D7CFF&center=true&vCenter=true&width=600&lines=%3E_Initializing+neural+networks...;%3E_Loading+YOLO+weights...;%3E_Compiling+Rust+to+PTX...;%3E_Hello+World!+I'm+Onuralp+%F0%9F%91%8B">
    </picture>
  </a>
</div>

<p align="center">
    <img alt="X Follow" src="https://img.shields.io/twitter/follow/onuralpszr">
    <a href="https://www.linkedin.com/in/osezer/"><img alt="Linkedin" src="https://img.shields.io/badge/Linkedin-0A66C2?logo=Linkedin&logoColor=white"></a>
    <a href="https://user-badge.committers.top/turkey_public/onuralpszr">
    <img alt="commiter" src="https://user-badge.committers.top/turkey_public/onuralpszr.svg" alt="committers.top badge"> </a>
    <a href="https://huggingface.co/onuralpszr"><img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-FF9A00?logo=HuggingFace&logoColor=white"></a>
    <a href="https://onuralpsezer.com"><img alt="Website" src="https://img.shields.io/badge/Website-onuralpsezer.com-4A71D9?logo=internet-explorer&logoColor=white"></a>
</p>

<p align="center">
  <a href="#-researchexploring"><b>Research</b></a> ·
  <a href="#-projectsactive"><b>Projects</b></a> ·
  <a href="#-git-log---milestones"><b>Journey</b></a> ·
  <a href="#-cuda_oxidekernellaunch"><b>GPU kernels</b></a> ·
  <a href="#-osscontributions"><b>Open Source</b></a> ·
  <a href="#-speakertalks"><b>Talks</b></a> ·
  <a href="#-deploystack"><b>Stack</b></a> ·
  <a href="https://onuralpsezer.com"><b>Website ↗</b></a>
</p>

</div>

👋 **Greetings everyone!** I'm **Onuralp**, a **Senior Machine Learning Engineer [@Ultralytics](https://github.com/ultralytics)**. I work on **computer vision** with **Python**, **Rust**, **C++** and **Kotlin**: R&D on the next improvements to **YOLO**, the training code, and fast inference through **ONNX**, **TensorRT** and **ExecuTorch**, on a strong **DevOps / MLOps** foundation.

Right now I'm also **learning and experimenting with VLMs and vision embedding models**, and **contributing to the PyTorch source**. Ask me about YOLO, PyTorch, VLMs, open source and Fedora Linux.

### 🧠 `model.summary()`

```python
import torch.nn as nn

class Onuralp(nn.Module):
    def __init__(self):
        super().__init__()
        self.role = "Senior Machine Learning Engineer @Ultralytics"
        self.focus = ["YOLO R&D 🎯", "VLMs 🗣️", "Vision Embeddings 🧭", "GPU Kernels ⚡"]
        self.languages = ["Python 🐍", "Kotlin 📱", "C++ ⚙️", "Rust 🦀", "CUDA PTX ⚡"]
        self.upstream = ["PyTorch 🔥", "ExecuTorch 📱", "Fedora 🐧"]
        self.community = ["Fedora Project Contributor 🐧", "GDG Samsun Organizer 🎤"]

    def forward(self, coffee):
        code = self.write_code(coffee)
        models = self.train_yolo(code)
        return self.deploy_to_edge(models)
```

### 🚀 `inference_pipeline.run()`

From research to production, this is the path my work takes every day:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/pipeline-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/readme/pipeline-light.svg">
  <img alt="Pipeline: datasets → PyTorch → ONNX → TensorRT / ExecuTorch → Rust / Edge" src="./assets/readme/pipeline-dark.svg" width="100%">
</picture>

## 🔬 `research::exploring()`

| | |
|:---|:---|
| 🎯 **YOLO R&D** | Research and development on the next improvements to YOLO at Ultralytics: architectures, training recipes and the export paths that decide how fast a model really runs. |
| 🗣️ **VLMs & vision embeddings** | Learning and experimenting with Vision-Language Models and vision embedding models, where detection meets language, retrieval and open-vocabulary search. |
| 🔥 **PyTorch from the inside** | Contributing to the PyTorch source and ExecuTorch to understand the stack underneath every model I ship. |
| 🌐 **Vision in the browser** | YOLO running client-side through Ultralytics Inference compiled to WebAssembly on WebGPU. Try it live on [onuralpsezer.com](https://onuralpsezer.com) or in my [Python Pizza deck](https://pizza.onuralpsezer.com/). |

## 🧩 `projects::active()`

| Project | Role | Description | Live Stats |
|:---|:---:|:---|:---|
| [Ultralytics](https://github.com/ultralytics/ultralytics) | <code>Co&#8209;Maintainer</code> | World's leading YOLO framework for object detection, instance segmentation, semantic segmentation, depth estimation, image classification, pose estimation and oriented object detection, with tracking across video frames | <a href="https://github.com/ultralytics/ultralytics"><img alt="stars" src="https://img.shields.io/github/stars/ultralytics/ultralytics?style=flat&logo=github&label=%E2%AD%90"></a> |
| [Ultralytics Inference](https://github.com/ultralytics/inference) | <code>Main&nbsp;Maintainer</code> | 🦀 High-performance YOLO inference in Rust for ONNX and OpenVINO IR models, running natively and in the browser on WebGPU, dual-published as a [crate](https://crates.io/crates/ultralytics-inference) 📦 and an [npm](https://www.npmjs.com/package/@ultralytics/yolo) package 🟢 (Node bindings) | <a href="https://github.com/ultralytics/inference"><img alt="stars" src="https://img.shields.io/github/stars/ultralytics/inference?style=flat&logo=github&label=%E2%AD%90"></a> <a href="https://crates.io/crates/ultralytics-inference"><img alt="crate downloads" src="https://img.shields.io/crates/d/ultralytics-inference?style=flat&logo=rust&label=crate"></a> <a href="https://www.npmjs.com/package/@ultralytics/yolo"><img alt="npm downloads" src="https://img.shields.io/npm/dt/@ultralytics/yolo?style=flat&logo=npm&label=npm"></a> |
| [TrackForge](https://github.com/onuralpszr/trackforge) | <code>Main&nbsp;Maintainer</code> | Unified, high-performance multi-object tracking library in Rust with Python bindings: ByteTrack, DeepSORT, OC-SORT, Deep OC-SORT, BoT-SORT, TrackTrack and SORT, with pluggable Re-ID and Ultralytics integration | <a href="https://github.com/onuralpszr/trackforge"><img alt="stars" src="https://img.shields.io/github/stars/onuralpszr/trackforge?style=flat&logo=github&label=%E2%AD%90"></a> <a href="https://crates.io/crates/trackforge"><img alt="crate downloads" src="https://img.shields.io/crates/d/trackforge?style=flat&logo=rust&label=crate"></a> <a href="https://pypi.org/project/trackforge/"><img alt="pypi downloads" src="https://img.shields.io/pypi/dm/trackforge?style=flat&logo=python&logoColor=white&label=pypi"></a> |
| [SAHI](https://github.com/obss/sahi) | <code>Co&#8209;Maintainer</code> | Slicing Aided Hyper Inference for object detection on large images | <a href="https://github.com/obss/sahi"><img alt="stars" src="https://img.shields.io/github/stars/obss/sahi?style=flat&logo=github&label=%E2%AD%90"></a> <a href="https://pypi.org/project/sahi/"><img alt="pypi downloads" src="https://img.shields.io/pypi/dm/sahi?style=flat&logo=python&logoColor=white&label=pypi"></a> |
| [CvCamera-Mobile](https://github.com/onuralpszr/CvCamera-Mobile) | <code>Main&nbsp;Maintainer</code> | Android CV camera template with OpenCV and real-time ML | <a href="https://github.com/onuralpszr/CvCamera-Mobile"><img alt="stars" src="https://img.shields.io/github/stars/onuralpszr/CvCamera-Mobile?style=flat&logo=github&label=%E2%AD%90"></a> |
| [GFPGAN-ncnn-vulkan](https://github.com/onuralpszr/GFPGAN-ncnn-vulkan) | <code>Main&nbsp;Maintainer</code> | Face restoration via GFPGAN, accelerated with ncnn + Vulkan | <a href="https://github.com/onuralpszr/GFPGAN-ncnn-vulkan"><img alt="stars" src="https://img.shields.io/github/stars/onuralpszr/GFPGAN-ncnn-vulkan?style=flat&logo=github&label=%E2%AD%90"></a> |
| [PyTorch](https://github.com/pytorch/pytorch) · [ExecuTorch](https://github.com/pytorch/executorch) | `Contributor` | Contributing to the PyTorch source and its on-device runtime for edge and mobile | <a href="https://github.com/pytorch/executorch"><img alt="stars" src="https://img.shields.io/github/stars/pytorch/executorch?style=flat&logo=github&label=%E2%AD%90"></a> |
| [YOLO-World](https://github.com/AILab-CVC/YOLO-World) | `Contributor` | Real-time open-vocabulary object detection via text prompts | <a href="https://github.com/AILab-CVC/YOLO-World"><img alt="stars" src="https://img.shields.io/github/stars/AILab-CVC/YOLO-World?style=flat&logo=github&label=%E2%AD%90"></a> |
| [KDE](https://kde.org/) | `Contributor` | KDE ecosystem: Linux desktop and open-source community | [kde.org](https://kde.org/) |

#### 🧪 `lab::side_projects()`

| Project | Description |
|:---|:---|
| [xps-fedora](https://github.com/onuralpszr/xps-fedora) | Fedora on the Dell XPS 16 (Intel Panther Lake): kernel patches, IPU7 camera, IR face unlock, NPU and an Intel AI stack, packaged as RPMs on [COPR](https://copr.fedorainfracloud.org/coprs/thunderbirdtr/xps-fedora/) |
| [colabsh](https://github.com/onuralpszr/colabsh) | CLI for Google Colab: execute code and interact with Colab from the terminal |
| [yuko](https://github.com/onuralpszr/yuko) | Rust-backed validators for common validation tasks, as a Python package |
| [python-pizza-talk](https://github.com/onuralpszr/python-pizza-talk) | Animated slides and a live in-browser YOLO demo for Python Pizza Istanbul 2026 |

<details>
<summary><b>📜 <code>projects::past()</code></b></summary>
<br>

| Project | Description |
|:---|:---|
| [Supervision](https://github.com/roboflow/supervision) | Reusable CV tools for detections, annotations and datasets (former co-maintainer) |
| [Supervision Conda Forge](https://github.com/conda-forge/supervision-feedstock) | Conda package distribution for Supervision |
| [Gemma Cookbook](https://github.com/google-gemini/gemma-cookbook) | Guides and examples for Google Gemma |
| [Sceneview-android](https://github.com/SceneView/sceneview-android) | ARCore and 3D rendering for Android |
| [Sceneform-android](https://github.com/SceneView/sceneform-android) | ARCore SDK for Android from the SceneView team |
| [Nvidia Auto Installer](https://github.com/t0xic0der/nvidia-auto-installer-for-fedora) | Automated NVIDIA driver installer for Fedora Linux |

</details>

## 📈 `git log --milestones`

```console
$ git log --oneline --milestones --author="Onuralp"
2026  🍕 model.predict(): real-time edge vision talk at Python Pizza Istanbul
2026  🛠️ No GPU Left Behind: hybrid YOLO training workshop at GDG Samsun DevFest
2026  🦀 Created TrackForge: Rust multi-object tracking (ByteTrack, DeepSORT, OC-SORT, BoT-SORT, TrackTrack and more) + Python bindings
2025  🚀 Main maintainer of ultralytics/inference: Rust YOLO inference, dual-shipped to crates.io + npm
2024  🧠 Senior ML Engineer @Ultralytics, co-maintaining YOLO (detect, segment, semantic, depth, classify, pose, OBB)
2023  🔬 Co-maintainer @ SAHI · former co-maintainer @ Supervision (Roboflow)
2022  🌱 First Hacktoberfest, 4 consecutive years and counting (Holopin 10 Badge Club)
2021  🐧 Fedora RPM packager & KDE SIG member, shipping AI/ML libs to ~40M users
2016  🎤 Speaker at Flock to Fedora and BalCCon (also BalCCon 2015)
2013  🎤 Speaker at OSOL Conference Szeged · Fedora 18-20 QA & Anaconda testing
2012  👋 git init: joined GitHub · FUDCon Paris
2011  🎉 Fedora 16 release party in Tokat, the first of many Fedora events
```

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/contributions-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/readme/contributions-light.svg">
  <img alt="GitHub contributions per year: 2021 243, 2022 466, 2023 2,044, 2024 2,620, 2025 2,320, 2026 growing" src="./assets/readme/contributions-dark.svg" width="100%">
</picture>

<details>
<summary><b>🧬 <code>model.fit(epochs=1000)</code></b></summary>
<br>

<div align="center">

| `Epoch 1` | `Epoch 50` | `Epoch 100` |
|:---:|:---:|:---:|
| 🔲🔳🔲🔳🔳🔲🔳🔲<br>🔳🔲🔳🔲🔲🔳🔲🔳<br>🔲🔳🔲🔳🔳🔲🔳🔲<br>🔳🔲🔳🔲🔲🔳🔲🔳<br>🔲🔳🔲🔳🔳🔲🔳🔲<br>🔳🔲🔳🔲🔲🔳🔲🔳<br>🔲🔳🔲🔳🔳🔲🔳🔲<br>🔳🔲🔳🔲🔲🔳🔲🔳 | ⬛⬛⬛🟪🟪⬛⬛⬛<br>⬛⬛🟪🟪🟪🟪⬛⬛<br>⬛🟪🟪🟪🟪🟪🟪⬛<br>⬛🟪🟪🟪🟪🟪🟪⬛<br>⬛⬛🟪🟪🟪🟪⬛⬛<br>⬛⬛⬛🟪🟪⬛⬛⬛<br>⬛⬛⬛⬛⬛⬛⬛⬛<br>⬛⬛⬛⬛⬛⬛⬛⬛ | 🟥🟥🟥🟥🟥🟥🟥🟥<br>🟥⬛⬛⬛⬛⬛⬛🟥<br>🟥⬛🟦⬛⬛🟦⬛🟥<br>🟥⬛⬛⬛⬛⬛⬛🟥<br>🟥⬛⬛🟦🟦⬛⬛🟥<br>🟥⬛⬛⬛⬛⬛⬛🟥<br>🟥🟥🟥🟥🟥🟥🟥🟥<br>⬛⬛⬛⬛⬛⬛⬛⬛ |
| *Raw Data (Noise)* | *Feature Extraction* | *YOLO Object Detected!* |

</div>

```console
[Epoch 001] 🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪ (Learning Python & C++)
[Epoch 050] 🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪ (Mastering Computer Vision & OpenCV)
[Epoch 100] 🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪ (Training YOLO & Deep Learning Models)
[Epoch 500] 🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪ (Optimizing with ONNX, TensorRT & Rust)
[Epoch 999] 🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢 (Deploying AI @ Ultralytics 🚀)

> Model 'Onuralp' successfully converged.
> Current State: Senior ML Engineer Lv2
> Next Objective: AGI & Beyond...
```

</details>

## ⚡ `cuda_oxide::kernel::launch()`

Currently exploring **[cuda-oxide](https://nvlabs.github.io/cuda-oxide/)**, an experimental Rust-to-CUDA compiler from NVIDIA Research that compiles safe(ish), idiomatic Rust directly to PTX. No CUDA C, no DSLs, no foreign bindings: just Rust running on the GPU.

<table>
<tr>
<td width="55%" valign="top">

```rust
// 🦀 Rust compiles straight to PTX
#[kernel]
pub unsafe fn vector_add(a: &[f32], b: &[f32], c: &mut [f32]) {
    let tid = thread::index_1d() as usize;
    if tid < c.len() {
        c[tid] = a[tid] + b[tid]; // thousands of threads, one instruction
    }
}
```

</td>
<td width="45%" valign="top">

```console
$ cargo build --target nvptx64-nvidia-cuda
   ✅ Rust -> LLVM IR -> PTX
   ✅ Kernel compiled: vector_add.ptx
> Launching 4096 threads across 128 warps...
> All threads converged. ✅
> Status: still learning, the 🦀 loves the GPU
```

</td>
</tr>
</table>

## 🌍 `oss::contributions()`

```rust
let platforms = vec!["GitHub", "GitLab", "Pagure"];
let mission   = "build together, make open source better for everyone 🌍";
```

<table>
<tr>
<td width="50%" valign="top">

### 🐧 Fedora Project

Contributor **since 2011**: **Mindshare Member**, **KDE SIG Member**, **Websites & Apps Team Member** and **RPM Packager** ([wiki](https://fedoraproject.org/wiki/User:Thunderbirdtr)). I package Python, KDE, Qt and AI/ML libraries for the official Fedora repositories, bringing cutting-edge open source tools to millions of users. **157 Fedora badges**, talks at Flock, and two Fedora Magazine articles: *Use OpenCV on Fedora Linux* [Part 1](https://fedoramagazine.org/use-opencv-on-fedora-linux-part-1/) · [Part 2](https://fedoramagazine.org/use-opencv-on-fedora-linux-part-2/).

```console
$ fedpkg prep       # ✅ sources verified, patches applied
$ fedpkg mockbuild  # ✅ x86_64, aarch64
$ fedpkg push && fedpkg submit
> Update pushed to stable → ~40M Fedora users
```

</td>
<td width="50%" valign="top">

### 🎤 GDG Samsun

**Organizer & Speaker** at [GDG Samsun](https://gdgsamsun.org/), sharing insights on **Deep Learning**, **Computer Vision**, **LLMs / RAG** and **Vision-Language Models**.

### 🌱 Hacktoberfest

`2022` ✅ `2023` ✅ `2024` ✅ `2025` ✅

Four consecutive years, dozens of PRs, a spot in the **Holopin x Hacktoberfest 10 Badge Club**, and somewhere out there **a tree growing in my name** 🌳. For me it's about **people, learning and giving back**.

</td>
</tr>
</table>

I co-maintain **[SAHI](https://github.com/obss/sahi)** and was previously a co-maintainer of **[Supervision](https://supervision.roboflow.com/)**. I also contribute to the **[PyTorch](https://github.com/pytorch/pytorch)** source, **[ExecuTorch](https://github.com/pytorch/executorch)** and **[ONNXSlim](https://github.com/inisis/OnnxSlim)**, plus many FLOSS projects across GitHub, GitLab and Pagure.

## 🎤 `speaker::talks()`

| When | Talk | Event | |
|:---|:---|:---|:---:|
| `Dec 2026` | [Nerede? Turkish-English Semantic Search with EmbeddingGemma 2](https://onuralpszr.github.io/nerede/) | GDG DevFest İstanbul 2026 | 📝 proposal |
| `Nov 2026` | [model.predict(): Real-Time Edge Vision with Ultralytics](https://pizza.onuralpsezer.com/) | Python Pizza Istanbul 2026 | 🍕 live demo |
| `Oct 2026` | [No GPU Left Behind: Hybrid Ultralytics YOLO Training and Fast Execution](https://onuralpszr.github.io/gdg-samsun-etkinlik-2026-workshop/) | GDG Samsun DevFest 2026 | 🛠️ workshop |
| `Jun 2025` | [Computer Vision with Supervision](./Presentations/openSUSE-Conf-2025/supervision-computer-vision) | openSUSE Conference 2025 | 🐍 code |
| `May 2025` | [Fedora 42 KDE Plasma Desktop Edition](./Presentations/Fedora/Fedora%2042%20KDE%20Plasma%20Desktop%20Edition%20Release%20Party%20Slides.pdf) | Fedora 42 Release Party | 📄 slides |
| `Dec 2024` | [What’s new in Fedora 41](./Presentations/Samsun/Samsun_Fedora41_Release_Slides/Fedora_Samsun.pdf) | Fedora 41 Release Party · Samsun | 📄 slides |
| `Jun 2024` | [LLMs & Retrieval-Augmented Generation](./Presentations/Samsun/Samsun_GDG_LLM_RAG_Jun_1_2024/GDG%20Samsun%20-%20LLM_RAG.pdf) | GDG Samsun | 📄 slides |
| `Apr 2024` | [Computer Vision with Supervision](./Presentations/Samsun/Samsun_GDG_AI_Summit_April_7_2024/Supervision_Samsun_GDG.pdf) | GDG Samsun AI Summit | 📄 slides |
| `Apr 2024` | [On-device ML with Flutter & TFLite](./Presentations/Samsun/Samsun_GDG_AI_Summit_April_7_2024/Flutter_Tflite_Samsun_GDG.pdf) | GDG Samsun AI Summit | 📄 slides |
| `Feb 2024` | [Fedora Linux Meetup](./Presentations/Samsun/Fedora_Feb24_2024_Samsun.pdf) | Fedora · Samsun | 📄 slides |
| `Aug 2022` | [State of Gaming on Fedora Workstation](./Presentations/Samsun/Samsun_Fedora41_Release_Slides/NestWithFedora2022_1854IST_06Aug2022_FWStateOfGaming.pdf) | Nest with Fedora 2022 | 📄 slides |
| `Aug 2021` | [Fedora & Plasma Mobile](./Presentations/Nest_2021_Talk_Fedora_Plasma_Mobile.pdf) | Nest with Fedora 2021 | 📄 slides |
| `2016` | Speaker | [Flock to Fedora 2016](https://fedoraproject.org/wiki/Flock_2016) | 🎤 |
| `2016` | Speaker | [BalCCon 2k16](https://2k16.balccon.org/) | 🎤 |
| `2015` | Speaker | [BalCCon 2k15](https://2k15.balccon.org/) | 🎤 |
| `2013` | Speaker | OSOL Conference Szeged 2013 | 🎤 |

## 🔧 `deploy::stack()`

```python
stack = {
    "training":  ["PyTorch", "Ultralytics", "TensorFlow", "JAX", "Keras"],
    "inference": ["ONNX Runtime", "TensorRT", "ExecuTorch", "ncnn", "Vulkan", "OpenVINO"],
    "gpu":       ["CUDA", "cuda-oxide", "PTX", "NVIDIA TensorRT", "WebGPU"],
    "research":  ["YOLO R&D", "VLMs", "Vision Embeddings", "Tracking"],
    "backend":   ["Python", "FastAPI", "Django", "Flask"],
    "mobile":    ["Kotlin", "Flutter", "ARCore", "MediaPipe", "Firebase"],
}
```

On mobile I work with **Kotlin** and **Flutter** alongside [ARCore](https://developers.google.com/ar), [MediaPipe](https://mediapipe.dev/), [Firebase](https://firebase.google.com/), [FlatBuffers](https://flatbuffers.dev/), [ONNX Runtime](https://onnxruntime.ai/) and [ncnn](https://github.com/Tencent/ncnn). **[PyTorch](https://pytorch.org/)** is my primary deep learning framework, with [TensorFlow](https://www.tensorflow.org), [TensorBoard](https://www.tensorflow.org/tensorboard), [Keras](https://keras.io/) and [JAX](https://github.com/google/jax) for experiments and cross-framework work.

<details>
<summary><b>🧰 Full arsenal: languages, frameworks, tools, platforms</b></summary>
<br>

<h3 align="left">Programming</h3>
<p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white">
    <img alt="Kotlin" src="https://img.shields.io/badge/Kotlin-%23E34F26.svg?logo=Kotlin&logoColor=white">
    <img alt="Dart" src="https://img.shields.io/badge/Dart-00979D?logo=dart&logoColor=white">
    <img alt="cpp" src="https://img.shields.io/badge/C%2B%2B-00599C.svg?logo=cplusplus&logoColor=white">
    <img alt="c" src="https://img.shields.io/badge/C-A8B9CC.svg?logo=c&logoColor=black">
    <img alt="GNU Bash" src="https://img.shields.io/badge/GNU Bash-4EAA25.svg?logo=gnubash&logoColor=white">
    <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript%20-%23F7DF1E.svg?logo=javascript&logoColor=black">
    <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript%20-%23007ACC.svg?logo=typescript&logoColor=white">
    <img alt="HTML" src="https://img.shields.io/badge/HTML%20-%23E34F26.svg?logo=html5&logoColor=white">
    <img alt="CSS" src="https://img.shields.io/badge/CSS%20-%231572B6.svg?logo=css3&logoColor=white">
    <img alt="Rust" src="https://img.shields.io/badge/Rust-%23000000.svg?logo=rust&logoColor=white">

</p>

<h3 align="left">Backend-as-a-Service (Baas)</h3>
<p>
   <img alt="Firebase" src="https://img.shields.io/badge/Firebase-FFCA28.svg?logo=Firebase&logoColor=white">
      <img alt="Appwrite" src="https://img.shields.io/badge/Appwrite-F02E65.svg?logo=Appwrite&logoColor=white">
</p>

<h3 align="left">Web Servers</h3>
<p>
   <img alt="Nginx" src="https://img.shields.io/badge/Nginx-009639.svg?logo=Nginx&logoColor=white">
   <img alt="Apache" src="https://img.shields.io/badge/Apache-D22128.svg?logo=Apache&logoColor=white">
   <img alt="Traefik" src="https://img.shields.io/badge/Traefik-24A1C1.svg?logo=Traefik-Proxy&logoColor=white">
</p>

<h3 align="left">Framework & Libraries</h3>
<p>
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688.svg?logo=FastAPI&logoColor=white">
  <img alt="Django" src="https://img.shields.io/badge/Django-006400.svg?logo=Django&logoColor=white">
  <img alt="Django Rest Framework" src="https://img.shields.io/badge/Django%20Rest%20Framework%20-%23404d59.svg?logo=django&logoColor=white">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-000000.svg?logo=flask&logoColor=white">
  <img alt="Angular" src="https://img.shields.io/badge/Angular%20-%2320232a.svg?logo=angular&logoColor=red">
  <img alt="Qt" src="https://img.shields.io/badge/Qt-006400.svg?logo=Qt&logoColor=white">
  <img alt="Flutter" src="https://img.shields.io/badge/Flutter-2391E6.svg?logo=Flutter&logoColor=white">
  <img alt="Android" src="https://img.shields.io/badge/Android-7AFF33.svg?logo=Android&logoColor=black">
  <img alt="Tensorflow" src="https://img.shields.io/badge/Tensorflow-v2-FE7A16.svg?logo=Tensorflow&logoColor=white">
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-EE4C2C.svg?logo=PyTorch&logoColor=white">
  <img alt="PyTorch" src="https://img.shields.io/badge/TorchVision-EE4C2C.svg?logo=PyTorch&logoColor=white">
  <img alt="PyTorch" src="https://img.shields.io/badge/TorchAudio-EE4C2C.svg?logo=PyTorch&logoColor=white">
  <img alt="Onnx" src="https://img.shields.io/badge/Onnx-717272.svg?logo=Onnx&logoColor=white">
  <img alt="Onnx-runtime" src="https://img.shields.io/badge/OnnxRuntime-717272.svg?logo=Onnx&logoColor=white">
  <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-2391E6.svg?logo=OpenCV&logoColor=white">
  <img alt="Mediapipe" src="https://img.shields.io/badge/Mediapipe-008F9E.svg?&logoColor=white">
   <a href="#"><img alt="luxonis-depthai-core" src="https://img.shields.io/badge/Depthai-Core-4E26DA.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgdmVyc2lvbj0iMS4xIgogICB2aWV3Qm94PSIwIDAgMTI4LjQ2MDAxIDExMi43MyIKICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgaWQ9InN2ZzI0IgogICBzb2RpcG9kaTpkb2NuYW1lPSJsb2dvX3N5bWJvbC5zdmciCiAgIGlua3NjYXBlOmV4cG9ydC1maWxlbmFtZT0iXFx3c2wkXFVidW50dS0yMC4wNFxob21lXGphbmNpYnVsa2FcZGV2XHdlYnNpdGVccHVibGljXGFzc2V0c1xtYXJrZXRpbmdcYnJhbmRcbG9nby53ZWJwIgogICBpbmtzY2FwZTpleHBvcnQteGRwaT0iOTYiCiAgIGlua3NjYXBlOmV4cG9ydC15ZHBpPSI5NiIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMS4xLjIgKGI4ZTI1YmU4MzMsIDIwMjItMDItMDUpIgogICB3aWR0aD0iMTI4LjQ2MDAxIgogICBoZWlnaHQ9IjExMi43MyIKICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiCiAgIHhtbG5zOnNvZGlwb2RpPSJodHRwOi8vc29kaXBvZGkuc291cmNlZm9yZ2UubmV0L0RURC9zb2RpcG9kaS0wLmR0ZCIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZGVmcwogICBpZD0iZGVmczI4Ij4KCgoKCgoKCgoKICA8L2RlZnM+PHNvZGlwb2RpOm5hbWVkdmlldwogICBpZD0ibmFtZWR2aWV3MjYiCiAgIHBhZ2Vjb2xvcj0iI2ZmZmZmZiIKICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgaW5rc2NhcGU6cGFnZXNoYWRvdz0iMiIKICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgaW5rc2NhcGU6cGFnZWNoZWNrZXJib2FyZD0iMCIKICAgc2hvd2dyaWQ9ImZhbHNlIgogICBpbmtzY2FwZTp6b29tPSIyLjgzNTU0ODIiCiAgIGlua3NjYXBlOmN4PSI3MS45NDM3NiIKICAgaW5rc2NhcGU6Y3k9IjU2LjI1MDE0NiIKICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxOTIwIgogICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMDAxIgogICBpbmtzY2FwZTp3aW5kb3cteD0iLTkiCiAgIGlua3NjYXBlOndpbmRvdy15PSItOSIKICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ic3ZnMjQiCiAgIGlua3NjYXBlOnNob3dwYWdlc2hhZG93PSJ0cnVlIgogICBmaXQtbWFyZ2luLXRvcD0iMCIKICAgZml0LW1hcmdpbi1sZWZ0PSIwIgogICBmaXQtbWFyZ2luLXJpZ2h0PSIwIgogICBmaXQtbWFyZ2luLWJvdHRvbT0iMCIgLz4KICA8c3R5bGUKICAgdHlwZT0idGV4dC9jc3MiCiAgIGlkPSJzdHlsZTIiPgogICAgLnN0MCB7CiAgICAgIGZpbGw6ICM1NzI0RTg7CiAgICB9CiAgPC9zdHlsZT4KICA8ZwogICBpZD0iZzY4MSIKICAgY2xpcC1wYXRoPSJub25lIgogICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMC41LC0yNy45NykiPjxwYXRoCiAgICAgY2xhc3M9InN0MCIKICAgICBkPSJtIDcyLjYsMTE5LjA1IGMgLTE5LjE0LDAgLTM0LjcxLC0xNS41NyAtMzQuNzEsLTM0LjcyIDAsLTE5LjE0IDE1LjU3LC0zNC43MSAzNC43MSwtMzQuNzEgMTkuMTQsMCAzNC43MSwxNS41NyAzNC43MSwzNC43MSAwLjAxLDE5LjE0IC0xNS41NywzNC43MiAtMzQuNzEsMzQuNzIgbSAwLC05MS4wOCBjIC0yNy40MiwwIC01MC4yNiwxOS41OSAtNTUuMzEsNDUuNTQgSCAwLjUgdiAyMS42NSBoIDE2Ljc5IGMgNS4wNSwyNS45NSAyNy44OSw0NS41NCA1NS4zMSw0NS41NCAzMS4xMywwIDU2LjM2LC0yNS4yMyA1Ni4zNiwtNTYuMzYgMCwtMzEuMTMgLTI1LjIzLC01Ni4zNyAtNTYuMzYsLTU2LjM3IgogICAgIGlkPSJwYXRoMTgiIC8+PHBhdGgKICAgICBjbGFzcz0ic3QwIgogICAgIGQ9Im0gNzIuNiw4Ny4wOSBjIC0xLjUyLDAgLTIuNzYsLTEuMjQgLTIuNzYsLTIuNzYgMCwtMS41MiAxLjI0LC0yLjc2IDIuNzYsLTIuNzYgMS41MiwwIDIuNzYsMS4yNCAyLjc2LDIuNzYgMCwxLjUyIC0xLjI0LDIuNzYgLTIuNzYsMi43NiBtIDAsLTEzLjU3IGMgLTUuOTcsMCAtMTAuODEsNC44NCAtMTAuODEsMTAuODEgMCw1Ljk3IDQuODQsMTAuODEgMTAuODEsMTAuODEgNS45NywwIDEwLjgxLC00Ljg0IDEwLjgxLC0xMC44MSAwLC01Ljk3IC00Ljg0LC0xMC44MSAtMTAuODEsLTEwLjgxIgogICAgIGlkPSJwYXRoMjAiIC8+PC9nPgo8L3N2Zz4K"></a>
</p>

<h3 align="left">Game Engines</h3>
<p>
    <img alt="Unity" src="https://img.shields.io/badge/Unity%20-%2320232a.svg?logo=unity&logoColor=white">
    <img alt="UnrealEngine" src="https://img.shields.io/badge/UnrealEngine%20-%2320232a.svg?logo=UnrealEngine&logoColor=white">
    <img alt="Godotengine" src="https://img.shields.io/badge/Godotengine-478CBF.svg?logo=Godotengine&logoColor=white">

</p>

<h3 align="left">Databases</h3>
<p>
    <a href="#"><img alt="PostgreSql" src="https://img.shields.io/badge/PostgreSql-4169E1?logo=postgresql&logoColor=white"></a>
    <a href="#"><img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white"></a>
    <a href="#"><img alt="MySQL" src="https://img.shields.io/badge/MySQL-4479A1.svg?logo=MySQL&logoColor=white"></a>
    <a href="#"><img alt="MariaDB" src="https://img.shields.io/badge/MariaDB-003545.svg?logo=MariaDB&logoColor=white"></a>
</p>

<h3 align="left">VPN Servers</h3>
<p>
    <a href="#"><img alt="WireGuard" src="https://img.shields.io/badge/WireGuard-88171A?logo=WireGuard&logoColor=white"></a>
    <a href="#"><img alt="OpenVPN" src="https://img.shields.io/badge/OpenVPN-EA7E20?logo=OpenVPN&logoColor=white"></a>
</p>

<h3 align="left">Virtualization Platforms</h3>
<p>
    <a href="#"><img alt="QEMU" src="https://img.shields.io/badge/QEMU-FF6600?logo=QEMU&logoColor=white"></a>
    <a href="#"><img alt="VirtualBox" src="https://img.shields.io/badge/VirtualBox-183A61?logo=VirtualBox&logoColor=white"></a>
    <a href="#"><img alt="VMware" src="https://img.shields.io/badge/VMware-607078?logo=VMware&logoColor=white"></a>
    <a href="#"><img alt="VMwareESXI" src="https://img.shields.io/badge/VMware ESXI-607078?logo=VMware&logoColor=white"></a>
</p>

<h3 align="left">Software and tools</h3>
<p>
    <a href="#"><img alt="Git" src="https://img.shields.io/badge/Git%20-%23F05033.svg?logo=git&logoColor=white"></a>
    <a href="#"><img alt="Meson" src="https://img.shields.io/badge/Meson-2391E6.svg?logo=Meson&logoColor=white"></a>
    <a href="#"><img alt="Cmake" src="https://img.shields.io/badge/Cmake-064F8C.svg?logo=Cmake&logoColor=white"></a>
    <a href="#"><img alt="Docker" src="https://img.shields.io/badge/Docker-2391E6.svg?logo=docker&logoColor=white"></a>
    <a href="#"><img alt="Podman" src="https://img.shields.io/badge/Podman-892CA0.svg?logo=Podman&logoColor=white"></a>
    <a href="#"><img alt="Dependabot" src="https://img.shields.io/badge/Dependabot-025E8C.svg?logo=Dependabot&logoColor=white"></a>
    <a href="#"><img alt="Nvidia" src="https://img.shields.io/badge/Nvidia-76B900.svg?logo=Nvidia&logoColor=white"></a>
    <a href="#"><img alt="LLVM" src="https://img.shields.io/badge/LLVM-262D3A.svg?logo=LLVM&logoColor=white"></a>
    <a href="#"><img alt="Postman" src="https://img.shields.io/badge/Postman-FF6C37?logo=postman&logoColor=white"></a>
    <a href="#"><img alt="Conventional Commits" src="https://img.shields.io/badge/Conventional Commits-FE5196?logo=conventionalcommits&logoColor=white"></a>
    <a href="#"><img alt="Stack Overflow" src="https://img.shields.io/badge/-StackOverflow-F58025?logo=stack-overflow&logoColor=white"></a>
    <a href="#"><img alt="Visual Studio Code" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?logo=visual-studio-code&logoColor=white"></a>
    <a href="#"><img alt="PyCharm" src="https://img.shields.io/badge/PyCharm-000000.svg?logo=pycharm&logoColor=white"></a>
    <a href="#"><img alt="Clion" src="https://img.shields.io/badge/Clion-1AC69B.svg?logo=Clion&logoColor=white"></a>
    <a href="#"><img alt="Android Studio" src="https://img.shields.io/badge/Android Studio-3DDC84.svg?logo=androidstudio&logoColor=white"></a>
    <a href="#"><img alt="Jupyter" src="https://img.shields.io/badge/JupyterNotebook-F37626.svg?logo=Jupyter&logoColor=white"></a>
    <a href="#"><img alt="Kubernetes" src="https://img.shields.io/badge/Kubernetes-2391E6.svg?logo=Kubernetes&logoColor=white"></a>
    <a href="#"><img alt="Blender" src="https://img.shields.io/badge/Blender-F5792A.svg?logo=Blender&logoColor=white"></a>
    <a href="#"><img alt="GithubActions" src="https://img.shields.io/badge/Github Actions-2088FF.svg?logo=githubactions&logoColor=white"></a>
    <a href="#"><img alt="Anaconda" src="https://img.shields.io/badge/Anaconda-44A833.svg?logo=Anaconda&logoColor=white"></a>
    <a href="#"><img alt="Ansible" src="https://img.shields.io/badge/Ansible-EE0000.svg?logo=Ansible&logoColor=white"></a>
</p>

<h3 align="left">Linux Distributions</h3>
<p>
    <a href="#"><img alt="Fedora" src="https://img.shields.io/badge/Fedora-51A2DA.svg?logo=fedora&logoColor=white"></a>
    <a href="#"><img alt="CentOS" src="https://img.shields.io/badge/CentOS-262577.svg?logo=CentOS&logoColor=white"></a>
    <a href="#"><img alt="RHEL" src="https://img.shields.io/badge/RHEL-EE0000.svg?logo=redhat&logoColor=white"></a>
    <a href="#"><img alt="OpenSUSE" src="https://img.shields.io/badge/OpenSUSE-73BA25.svg?logo=OpenSUSE&logoColor=white"></a>
    <a href="#"><img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-FE7A16.svg?logo=Ubuntu&logoColor=white"></a>
    <a href="#"><img alt="Debian" src="https://img.shields.io/badge/Debian-A81D33.svg?logo=Debian&logoColor=white"></a>
</p>

<h3 align="left">Platforms</h3>
<p>
    <a href="#"><img alt="Linux" src="https://img.shields.io/badge/Linux-%23F7DF1E.svg?logo=Linux&logoColor=black"></a>
    <a href="#"><img alt="Windows" src="https://img.shields.io/badge/Windows-0078D4.svg?logo=Windows&logoColor=white"></a>
    <a href="#"><img alt="OSX" src="https://img.shields.io/badge/Mac-OSX-%23E34F26.svg?logo=Apple&logoColor=white"></a>
</p>

<h3 align="left">Cloud Providers</h3>
<p>
    <a href="#"><img alt="Amazon AWS" src="https://img.shields.io/badge/AmazonAWS-232F3E.svg?logo=amazonaws&logoColor=white"></a>
    <a href="#"><img alt="Azure" src="https://img.shields.io/badge/AzureCloud-232F3E.svg?logo=azuredevops&logoColor=white"></a>
    <a href="#"><img alt="Google Cloud" src="https://img.shields.io/badge/Google-Cloud-4285F4.svg?logo=googlecloud&logoColor=white"></a>
</p>

</details>

## 📊 `stats.render()`

<p align="center">
  <img width="49%" src="https://github-readme-stats-five-topaz-76.vercel.app/api?username=onuralpszr&show_icons=true&theme=dark&hide_border=true" alt="Onuralp's GitHub stats">
  <img width="49%" src="https://ghstats.onuralpsezer.com/?user=onuralpszr&theme=github-dark&hide_border=true" alt="Onuralp's GitHub Streak stats">
</p>

![3D contribution graph](./profile-3d-contrib/profile-night-rainbow.svg)

## 🔗 `links::connect()`

I'm always open to collaborating, contributing, or just talking about open source, computer vision and AI. 🚀

<p align="center">
  <a href="https://www.linkedin.com/in/osezer/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-osezer-0A66C2?logo=linkedin&logoColor=white"></a>
  <a href="https://twitter.com/onuralpszr"><img alt="Twitter" src="https://img.shields.io/badge/Twitter-onuralpszr-000000?logo=x&logoColor=white"></a>
  <a href="https://huggingface.co/onuralpszr"><img alt="HuggingFace" src="https://img.shields.io/badge/HuggingFace-onuralpszr-FF9A00?logo=huggingface&logoColor=white"></a>
  <a href="https://www.credly.com/users/onuralp-sezer/badges"><img alt="Credly" src="https://img.shields.io/badge/Credly-Badges-FF6B00?logo=credly&logoColor=white"></a>
  <a href="https://developers.google.com/profile/u/onuralpsezer"><img alt="Google Developer" src="https://img.shields.io/badge/Google%20Developer-Profile-4285F4?logo=google&logoColor=white"></a>
  <a href="https://www.cloudskillsboost.google/public_profiles/aa921c43-e963-4266-aa26-e7465dab9aec"><img alt="Cloud Skills Boost" src="https://img.shields.io/badge/Cloud%20Skills%20Boost-Profile-4285F4?logo=googlecloud&logoColor=white"></a>
  <a href="https://ask.fedoraproject.org/u/thunderbirdtr/"><img alt="Ask Fedora" src="https://img.shields.io/badge/Ask%20Fedora-thunderbirdtr-294172?logo=fedora&logoColor=white"></a>
  <a href="https://pagure.io/user/thunderbirdtr"><img alt="Fedora Pagure" src="https://img.shields.io/badge/Fedora%20Pagure-thunderbirdtr-294172?logo=fedora&logoColor=white"></a>
  <a href="https://src.fedoraproject.org/user/thunderbirdtr/"><img alt="Src Fedora" src="https://img.shields.io/badge/Src.Fedora-thunderbirdtr-294172?logo=fedora&logoColor=white"></a>
  <a href="https://fedoraproject.org/wiki/User:Thunderbirdtr"><img alt="Fedora Wiki" src="https://img.shields.io/badge/Fedora%20Wiki-Thunderbirdtr-294172?logo=fedora&logoColor=white"></a>
  <a href="https://badges.fedoraproject.org/user/thunderbirdtr"><img alt="Fedora Badges" src="https://img.shields.io/badge/Fedora%20Badges-thunderbirdtr-294172?logo=fedora&logoColor=white"></a>
</p>

<table>
<tr>
<td width="33%" valign="top" align="center">

**🤝 `mentorship::programs()`**

<p align="center">
  <a href="https://github.com/outreachy"><img alt="Outreachy" src="https://img.shields.io/badge/Outreachy-Mentor-4A71D9?logo=github&logoColor=white"></a>
  <a href="https://github.com/OpenTRFoundation/OpenTR"><img alt="OpenTR" src="https://img.shields.io/badge/OpenTR-Mentor-E74C3C?logo=github&logoColor=white"></a>
</p>

</td>
<td width="34%" valign="top" align="center">

**🙌 `volunteer::work()`**

<p align="center">
  <a href="https://fedoraproject.org/wiki/User:Thunderbirdtr"><img alt="Fedora Project" src="https://img.shields.io/badge/Fedora%20Project-Contributor-294172?logo=fedora&logoColor=white"></a>
  <a href="https://kde.org/"><img alt="KDE" src="https://img.shields.io/badge/KDE-Contributor-1D99F3?logo=kde&logoColor=white"></a>
  <a href="https://www.opensuse.org/"><img alt="openSUSE" src="https://img.shields.io/badge/openSUSE-Contributor-73BA25?logo=opensuse&logoColor=white"></a>
  <a href="https://gdg.community.dev/gdg-samsun/"><img alt="GDG Samsun" src="https://img.shields.io/badge/GDG%20Samsun-Member%20%7C%20Speaker%20%7C%20Organizer-4285F4?logo=google&logoColor=white"></a>
  <a href="https://gdgsamsun.org/"><img alt="GDG Samsun Website" src="https://img.shields.io/badge/gdgsamsun.org-Visit-4285F4?logo=google&logoColor=white"></a>
</p>

</td>
<td width="33%" valign="top" align="center">

**🏅 `certifications::earned()`**

<p align="center">
  <a href="https://www.credential.net/5d4c2d99-4c0b-4990-9399-2bdb496f7d4f#gs.axwujf"><img alt="TensorFlow Developer" src="https://img.shields.io/badge/TensorFlow%20Developer-Certified-FF6F00?logo=tensorflow&logoColor=white"></a>
  <a href="#"><img alt="HuggingFace Agents Course" src="https://img.shields.io/badge/HuggingFace%20Agents%20Course-Completed-FF9A00?logo=huggingface&logoColor=white"></a>
</p>

</td>
</tr>
</table>

<div align="center">

[![@osezer's Holopin board](https://holopin.me/osezer)](https://holopin.io/@osezer)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/footer-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/readme/footer-light.svg">
  <img alt="> Model 'Onuralp' successfully converged. Next objective: AGI &amp; beyond..." src="./assets/readme/footer-dark.svg" width="100%">
</picture>

</div>
