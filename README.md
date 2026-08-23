# ESP32-CAM Edge AI

Real-time Edge AI object detection system using ESP32-CAM.

## Project Goals

- Capture images using OV2640 camera
- Preprocess images on-device
- Run TinyML object detection locally
- Control LED / buzzer based on detection
- Display inference results on OLED
- Measure latency, FPS, RAM and Flash usage

## Hardware

- ESP32-CAM
- OV2640
- OLED
- LED
- Buzzer
- Push button

## Architecture

```text
Camera
   ↓
Image Preprocessing
   ↓
TinyML Model
   ↓
Object Detection
   ↓
Decision
   ↓
OLED / LED / Buzzer