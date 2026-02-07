# Real-Time Pothole Detection (YOLO + Model Ensemble) 🚧🕳️

A computer vision capstone project that detects potholes in **real time** using **object detection** (bounding boxes).  
The core detector is **YOLO** (fast + deployable), and for demonstration we also train **multiple models** and optionally combine them using an **ensemble** method (e.g., Weighted Box Fusion) to select the best-performing approach based on both **accuracy** and **speed (FPS/latency)**.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Goals and Objectives](#goals-and-objectives)
- [What This Repo Contains](#what-this-repo-contains)
- [Datasets](#datasets)
- [Models](#models)
- [Evaluation Metrics](#evaluation-metrics)
- [Ensembling Strategy](#ensembling-strategy)
- [Deployment Apps](#deployment-apps)
- [Project Structure](#project-structure)
- [Environment Setup](#environment-setup)
- [Data Preparation](#data-preparation)
- [Training](#training)
- [Evaluation](#evaluation)
- [Real-Time Demo](#real-time-demo)
- [Export for Android (Optional)](#export-for-android-optional)
- [Success Markers](#success-markers)
- [Troubleshooting](#troubleshooting)
- [References](#references)

---

## Project Overview
Road potholes are a major cause of:
- vehicle damage and higher maintenance costs,
- accidents (especially for motorcyclists),
- inefficient road maintenance due to slow/manual inspections.

This project builds an automated pothole detection system that:
1. Detects potholes using **bounding boxes**.
2. Runs in **real-time** on common devices (laptop/phone).
3. Compares YOLO against alternative detectors and (optionally) an ensemble.
4. Provides a demo app that shows **live bounding boxes** from a camera feed.

---

## Problem Statement
Manual road inspection is expensive, slow, and inconsistent. A deployable pothole detection system should work under real-world conditions like:
- shadows, dust, rain, glare,
- motion blur,
- occlusions and complex road textures.

**Goal:** Build a real-time pothole detector that is accurate **and** fast enough for live use.

---

## Goals and Objectives
### Aim
Design, train, evaluate, and deploy a real-time pothole detection system using YOLO and competing models, choosing the best based on accuracy + latency.

### Objectives
- Acquire and prepare a pothole/road damage dataset with bounding-box annotations.
- Train YOLO (primary) plus at least 2 alternative detectors.
- Evaluate accuracy (mAP/precision/recall) and runtime (FPS/latency/model size).
- Implement detection ensembling (e.g., Weighted Box Fusion) to test robustness gains.
- Deploy a demo app (local web app and/or Android) showing real-time detections.

---

## What This Repo Contains
✅ Training pipelines for object detection  
✅ Model comparison + evaluation scripts  
✅ Optional ensemble merging (WBF)  
✅ Real-time demo app (webcam → bounding boxes)  
✅ Export tooling for deployment formats (ONNX / TFLite, optional)

---

## Datasets
This project expects an **object detection dataset** (images + bounding box annotations).

### Recommended option (strong benchmark)
- **RDD2022 (Road Damage Dataset 2022)**: multi-country road damage labels including potholes (damage categories).  
  Use this if you want a credible “benchmark-grade” dataset and enough scale.

### Alternative (quick start)
- Pothole datasets on Kaggle in YOLO/VOC format (faster setup, sometimes smaller/noisier).

> ✅ Regardless of dataset, you must end up with labels in **YOLO format**:
