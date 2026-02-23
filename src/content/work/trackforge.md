---
title: TrackForge
publishDate: 2024-03-01 00:00:00
img: /assets/stock-3.jpg
img_alt: Object tracking visualization
description: |
  A unified, high-performance computer vision tracking library in Rust with Python bindings. Features ByteTrack and DeepSORT.
tags:
  - Rust
  - Python
  - Computer Vision
  - Tracking
---

**TrackForge** is a unified, high-performance computer vision tracking library, implemented in Rust and exposed as a Python package. It provides state-of-the-art tracking algorithms like **ByteTrack** and **DeepSORT**, optimized for speed and ease of use in both Rust and Python environments.

## Features

- **High Performance**: Native Rust implementation for maximum speed and memory safety
- **Python Bindings**: Seamless integration with the Python ecosystem using `pyo3`
- **Unified API**: Consistent interface for tracking tasks across both languages
- **ByteTrack**: Robust multi-object tracking using Kalman filters and IoU matching
- **DeepSORT**: SORT + appearance embeddings for improved tracking

## Installation

### Python
```bash
pip install trackforge
```

### Rust
```toml
[dependencies]
trackforge = "0.1.8"
```

**Role: Main Maintainer**

[GitHub Repository](https://github.com/onuralpszr/trackforge)
