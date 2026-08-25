---

## 🔧 ESP32-CAM Firmware

The firmware is developed using **PlatformIO** with the Arduino framework for the **AI Thinker ESP32-CAM** board.

### ⚙️ Firmware Configuration

The current firmware environment:

```ini
[env:esp32cam]

platform = espressif32
board = esp32cam
framework = arduino

monitor_speed = 115200
upload_speed = 921600

build_flags =
    -DCORE_DEBUG_LEVEL=3

lib_deps =
    esphome/AsyncTCP-esphome
```

### 🧩 Development Environment

* PlatformIO Core: `6.1.19`
* Espressif32 Platform: `6.11.0`
* Framework: Arduino for ESP32
* Board: AI Thinker ESP32-CAM
* MCU: ESP32
* CPU Frequency: 240 MHz
* Flash: 4 MB
* RAM: 320 KB
* Serial Monitor: `115200`
* Upload Speed: `921600`

### 📦 Firmware Dependencies

The firmware currently uses:

* Arduino framework
* AsyncTCP-esphome

The dependency is declared in `firmware/platformio.ini`:

```ini
lib_deps =
    esphome/AsyncTCP-esphome
```

---

## 🏗️ Build Firmware

Move into the firmware directory:

```bash
cd firmware
```

Build the project:

```bash
pio run
```

A successful build generates:

```text
.pio/build/esp32cam/firmware.bin
```

Current build result:

```text
==================================== [SUCCESS] ====================================

RAM:   [=         ]   6.4% (used 21112 bytes from 327680 bytes)
Flash: [=         ]   7.8% (used 245581 bytes from 3145728 bytes)
```

This confirms that the firmware currently compiles and links successfully for the ESP32-CAM target.

---

## 🔌 Upload Firmware

Connect the ESP32-CAM to the computer through the USB-to-Serial interface.

Then run:

```bash
pio run --target upload
```

If the board requires manual flashing mode:

1. Connect `GPIO0` to `GND`.
2. Reset the ESP32-CAM.
3. Start the upload command.
4. Remove the `GPIO0` → `GND` connection after flashing.
5. Reset the board.

---

## 🖥️ Serial Monitor

Open the serial monitor with:

```bash
pio device monitor
```

Or explicitly specify the baud rate:

```bash
pio device monitor -b 115200
```

The firmware uses:

```text
115200 baud
```

for serial debugging and runtime logs.

---

## 🧪 Firmware Development Status

Current progress:

* [x] PlatformIO project initialized
* [x] ESP32-CAM board configured
* [x] Arduino framework configured
* [x] AsyncTCP dependency configured
* [x] Serial monitor configured
* [x] Upload speed configured
* [x] Firmware compilation verified
* [x] Firmware linking verified
* [x] `firmware.bin` generated successfully
* [ ] Camera initialization
* [ ] Camera capture pipeline
* [ ] Image preprocessing
* [ ] Edge AI inference
* [ ] Model integration
* [ ] Hardware communication
* [ ] End-to-end Edge AI pipeline

---

## 🧠 Edge AI Development Roadmap

The firmware will be developed progressively:

```text
ESP32-CAM Hardware
        ↓
Camera Initialization
        ↓
Image Capture
        ↓
Image Preprocessing
        ↓
Feature Extraction
        ↓
TinyML / Edge AI Model
        ↓
Local Inference
        ↓
Decision / Classification
        ↓
IoT Communication
```

The long-term goal is to build an **Edge AI system running directly on the ESP32-CAM**, minimizing the need for cloud-based inference.

---

## 📌 Current Milestone

### Milestone 01 — Firmware Foundation

Status: **Completed**

The PlatformIO firmware environment has been successfully configured and tested.

The project can now:

```text
PlatformIO
    ↓
ESP32-CAM
    ↓
Arduino Framework
    ↓
Compile
    ↓
Link
    ↓
Generate firmware.bin
```

The next development stage is to implement the **ESP32-CAM hardware layer**, beginning with camera initialization and image capture.

---

## 👨‍💻 Author

**Lê Văn Tuấn Em**

AI / Machine Learning / Edge AI / Embedded Systems

---
pio run 
pio run -t upload
pio device monitor -p COM8 -b 115200