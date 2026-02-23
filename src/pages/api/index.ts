import type { APIRoute } from 'astro';

const ESC = '\x1b';
const RESET = `${ESC}[0m`;
const BOLD = `${ESC}[1m`;
const RED = `${ESC}[31m`;
const GREEN = `${ESC}[32m`;
const YELLOW = `${ESC}[33m`;
const BLUE = `${ESC}[34m`;
const CYAN = `${ESC}[36m`;

const banner = `
${CYAN}${BOLD}  ___  _   _ _   _ ____      _    _     ____  ${RESET}
${CYAN}${BOLD} / _ \\| \\ | | | | |  _ \\    / \\  | |   |  _ \\ ${RESET}
${CYAN}${BOLD}| | | |  \\| | | | | |_) |  / _ \\ | |   | |_) |${RESET}
${CYAN}${BOLD}| |_| | |\\  | |_| |  _ <  / ___ \\| |___|  __/ ${RESET}
${CYAN}${BOLD} \\___/|_| \\_|\\___/|_| \\_\\/_/   \\_\\_____|_|    ${RESET}
`;

const output = `
${banner}
${BOLD}${GREEN}Onuralp Sezer${RESET} - Senior Machine Learning Engineer

${YELLOW}[ Skills & Expertise ]${RESET}
- Computer Vision (Object Detection, Segmentation, Target Tracking)
- Deep Learning & MLOps
- Frameworks: PyTorch, ONNX, TensorRT
- Projects: YOLO, SAHI, Tracking, Supervision
- Community: Fedora Project, openSUSE, OpenCV

${BLUE}[ Links ]${RESET}
- GitHub:   ${BOLD}https://github.com/onuralpszr${RESET}
- LinkedIn: ${BOLD}https://www.linkedin.com/in/onuralpsezer/${RESET}
- Website:  ${BOLD}https://onuralpszr.github.io${RESET}

${CYAN}>>> "Vision is the art of seeing what is invisible to others." -- Jonathan Swift${RESET}
`;

export const GET: APIRoute = () => {
    return new Response(output, {
        status: 200,
        headers: {
            'Content-Type': 'text/plain; charset=utf-8',
        },
    });
};
