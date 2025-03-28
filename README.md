# Smart Aquafarm Feeder and Monitoring System for Highly Turbid Conditions

## Project Description

This project is a Computer Vision-based Smart Aquafarm Feeder and Monitoring System designed to detect shrimp feeds under highly turbid water conditions. It leverages object detection and segmentation techniques using the YOLOv8 model to identify shrimp feeds in underwater images. The system aims to optimize feed distribution, reduce waste, and improve aquaculture efficiency by automating the monitoring process.

---

## Technologies Used

- **Python 3.12**
- **Roboflow** - Dataset preparation and annotation
- **YOLOv8 (Ultralytics)** - Object detection and segmentation
- **OpenCV** - Image processing
- **NumPy** - Numerical operations
- **ONNX** - Model export for cross-platform deployment
- **Raspberry Pi (Theoretical Deployment)** - For real-time, on-board processing

---

## How Does It Work?

### Dataset Preparation

1. **Image Annotation (Roboflow)**
   - Uploaded shrimp feed images to Roboflow.
   - Annotated shrimp feeds manually (not all feeds were annotated due to time constraints).
   - Exported the dataset in **YOLOv8 format**.

2. **Dataset Structure**
   - The dataset contains `train`, `valid`, and `test` directories with `images` and `labels` subfolders.
   - A `data.yaml` configuration file was created to define dataset paths and classes.
   - Example configuration:
     ```yaml
     train: D:\DOST-Internship\Pre-assesment\myenv\Smart_Aquafarm_Feeder\dataset\train\images
     val: D:\DOST-Internship\Pre-assesment\myenv\Smart_Aquafarm_Feeder\dataset\valid\images
     test: D:\DOST-Internship\Pre-assesment\myenv\Smart_Aquafarm_Feeder\dataset\test\images

     nc: 1
     names: ['Shrimp feeds']
     ```

---

### Model Training and Implementation

1. **Environment Setup**
   - Created a Python virtual environment.
   - Installed dependencies listed in `requirements.txt`.
   - Copied the Roboflow dataset to the project directory.

2. **Model Selection**
   - Chose **YOLOv8s (small version)** due to:
     - Lightweight architecture
     - Reasonable size for CPU processing
     - Faster training time
     - Fair performance on object detection

   - **Trade-offs:**
     - Less accurate than larger YOLO models
     - Struggles with small or overlapping objects

3. **Training Process**
   - Initial training was done without data augmentation:
     - **50 epochs**
     - **Image size:** 640
     - **Batch size:** 4
     - **Device:** CPU
     - Training time: **3.172 hours**
   - Model exported to **ONNX format** for cross-platform compatibility.

4. **Training with Data Augmentation**
   - Applied advanced augmentation techniques:
     - HSV color jitter
     - Brightness and saturation variation
     - Random flipping (horizontal & vertical)
     - Mosaic augmentation
     - Mixup augmentation
     - Perspective transformation
   - Training time: **4.277 hours**
   - Model exported to **ONNX format**.

---

### Results and Findings

| Experiment | Precision (P) | Recall (R) | mAP50 | mAP50-95 | Training Time |
|---------|---------:|--------:|-------:|---------:|-------------:|
| Without Augmentation | 0.141 | 0.231 | 0.0671 | 0.0344 | 3.172 hrs |
| With Augmentation    | 0.0174 | 0.615 | 0.0272 | 0.00654 | 4.277 hrs |

**Analysis:**
- **Without Augmentation:**
  - Higher precision but lower recall.
  - Detected shrimp feeds but struggled with detecting more varied instances.
  - Overfitted on a small dataset.

- **With Augmentation:**
  - Precision dropped but recall significantly improved.
  - The model became more sensitive to detecting shrimp feeds even under diverse conditions.
  - This trade-off is expected due to the limited dataset and heavy augmentation, causing the model to generalize more but make false positives.
  - Ideal for aquaculture use where missing shrimp feeds is costlier than detecting false feeds.

---

## Theoretical Deployment on Raspberry Pi (For On-Board Processing)

### Hardware Requirements

- **Raspberry Pi 4 (4GB/8GB RAM)**
- **MicroSD Card (32GB or higher)**
- **USB Camera or Pi Camera Module**
- **Stable 5V 3A Power Supply**

### Setup Overview

1. **Install Raspberry Pi OS**
2. **Set up Python & dependencies**
3. **Transfer the trained `.pt` model to Raspberry Pi**
4. **Run YOLOv8 inference on live camera feed or stored images**
   ```bash
   yolo task=segment mode=predict model=best.pt source=0
