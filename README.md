<p align="center">
  <a href="https://github.com/Brajesh31/Video-quality-conversion-SD-to-HD--main">
    <img src="https://raw.githubusercontent.com/Brajesh31/asset/main/video-upscaler-banner.png" alt="SD to HD Video Upscaler Banner">
  </a>
</p>

<div align="center">

# 📹 SD to HD Video Upscaler 🖼️

**A Python-based tool to upscale Standard Definition (SD) videos to High Definition (HD) using traditional interpolation, while perfectly preserving the original audio.**

</div>

<p align="center">
  <img src="https://img.shields.io/github/stars/Brajesh31/Video-quality-conversion-SD-to-HD--main?style=for-the-badge&color=gold" alt="Stars">
  &nbsp;
  <img src="https://img.shields.io/github/last-commit/Brajesh31/Video-quality-conversion-SD-to-HD--main?style=for-the-badge&color=blue" alt="Last Commit">
  &nbsp;
  <img src="https://img.shields.io/github/license/Brajesh31/Video-quality-conversion-SD-to-HD--main?style=for-the-badge&color=green" alt="License">
</p>

---

## 🎯 Project Overview

This project is a prototype of a video conversion process that efficiently upscales **SD resolution (640x480px)** videos to **HD resolution (1280x720px)**. It leverages traditional, fast interpolation techniques like cubic interpolation to resize video frames while maintaining the best possible quality.

A key feature of this tool is its ability to handle audio separately. It extracts the original audio from the source video, processes the video frames, and then seamlessly merges the preserved audio with the newly upscaled video, ensuring perfect synchronization.

<br>

## ✨ Core Features

* **High-Quality Interpolation:** Uses **Cubic Interpolation** via OpenCV for a smoother and higher-quality upscale compared to simpler methods.
* **Audio Preservation:** Extracts the original audio track using FFmpeg and flawlessly merges it with the upscaled video.
* **Efficient Processing:** Built with performance in mind, using optimized libraries to process videos in a reasonable amount of time.
* **Standard Formats:** Supports common input video formats and produces standard `.mp4` output files.

<br>

## 🛠️ Technology Stack

This tool is built with a combination of powerful, open-source libraries for media processing.

| Technology                                                                                                               | Purpose                                                                          |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| [![Python][Python-badge]][Python-url]                                                                                    | The core programming language for the script.                                    |
| [![OpenCV][OpenCV-badge]][OpenCV-url]                                                                                    | Used for all video processing tasks, including reading, resizing, and writing frames. |
| [![FFmpeg][FFmpeg-badge]][FFmpeg-url]                                                                                    | A command-line tool used for fast and reliable audio extraction and merging. |

<br>

## 📁 File Structure

The project uses a simple and intuitive directory structure.
