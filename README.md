# Research Plan: Hardware-Aware Efficient Deep Learning for Resource-Constrained Edge AI

## 1. Định hướng nghiên cứu chính

### Tên đề tài

> **Hardware-Aware Efficient Deep Learning for Resource-Constrained Edge AI**

### Hướng triển khai cụ thể

> **Hardware-Aware Tiny Vision Model Optimization for ESP32-S3**

### Hướng paper dự kiến

> **Hardware-Aware Joint Optimization of Tiny Vision Models for Memory- and Latency-Constrained Edge Devices**


---

# 2. Ý tưởng nghiên cứu cốt lõi
```text
                    Deep Learning Model
                            │
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
        Architecture    Compression     Training
             │              │              │
             ↓              ↓              ↓
        Efficient CNN   Quantization      KD
             │          Pruning            QAT
             └──────────────┼──────────────┘
                            ↓
                 Hardware-Aware Optimization
                            ↓
                     Target Hardware
                        ESP32-S3
                            ↓
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
           Accuracy      Latency        Memory
                            │
                            ↓
                          Energy
```
Mục tiêu:
> **Tìm một Deep Learning model có Pareto trade-off tốt nhất giữa accuracy, latency, memory và energy trên phần cứng Edge cụ thể.**
---
# 3. Research Question
## Main Research Question
> **How can Deep Learning models be jointly optimized with hardware constraints to achieve the best accuracy–latency–memory–energy trade-off on resource-constrained edge devices?**
---
## Research Questions cụ thể
### RQ1 — Architecture
> Những đặc điểm kiến trúc nào của Tiny Vision CNN ảnh hưởng mạnh nhất đến accuracy, latency và memory trên ESP32-S3?
### RQ2 — Quantization
> Độ nhạy quantization của từng layer ảnh hưởng như thế nào đến accuracy và runtime?
### RQ3 — Knowledge Distillation
> Knowledge Distillation có thể tạo ra student model nhỏ hơn nhưng vẫn giữ accuracy tốt đến mức nào?
### RQ4 — Joint Optimization
> Việc kết hợp architecture optimization + distillation + quantization có tốt hơn tối ưu từng kỹ thuật độc lập không?
### RQ5 — Hardware Awareness
> Nếu đưa thông tin latency/memory thực tế từ ESP32-S3 ngược vào quá trình model optimization, có thể tìm được model tốt hơn hardware-agnostic optimization hay không?
---
# 4. Research Hypothesis
### H1
> Hardware-aware optimization tạo ra Pareto frontier tốt hơn so với optimization chỉ dựa trên accuracy/FLOPs.
### H2
> Quantization sensitivity khác nhau giữa các layer; do đó precision đồng nhất cho toàn model không nhất thiết là lựa chọn tối ưu.
### H3
> Knowledge Distillation giúp giảm accuracy degradation khi model bị compression mạnh.
### H4
> Joint optimization giữa KD + quantization + architecture/hardware constraints tạo ra trade-off tốt hơn từng kỹ thuật riêng lẻ.
---
# 5. Research Gap dự kiến
Hiện ESP-DL đã có PTQ, QAT/TQT, equalization, mixed-precision và các công cụ tự động hóa quantization; trên ESP32-S3, ESP-DL sử dụng per-tensor quantization do giới hạn ISA. ([Espressif Systems][2])
## Gap cần điều tra
```text
Layer sensitivity
        +
Hardware latency
        +
Memory footprint
        +
Quantization precision
        +
Distillation
        +
Architecture
        ↓
Joint optimization
```
---
# 6. Research Contribution dự kiến
### Contribution 1
Một phương pháp đánh giá:
> **Layer-wise hardware sensitivity**
cho Tiny Vision models.
---
### Contribution 2
Một cơ chế:
> **Hardware-aware precision/model allocation**
dựa trên:
```text
Quantization sensitivity
+
Memory cost
+
Latency cost
+
Accuracy impact
```
---
### Contribution 3
Một pipeline:
```text
Teacher
   ↓
Knowledge Distillation
   ↓
Efficient Student
   ↓
Hardware-aware Compression
   ↓
Quantization
   ↓
ESP32-S3
```
---
### Contribution 4
Benchmark thực tế trên hardware:
```text
Accuracy
Latency
Memory
Energy
FPS
```
thay vì chỉ báo cáo FLOPs/parameters.
---
# 7. Research Framework
Toàn bộ nghiên cứu:
```text
                 DATASET
                    │
                    ▼
             BASELINE MODEL
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
    MODEL ANALYSIS       HARDWARE PROFILING
          │                   │
          │          ┌────────┴────────┐
          │          ↓                 ↓
          │       Latency            Memory
          │          │                 │
          └──────────┴─────────────────┘
                         ↓
                HARDWARE-AWARE
                  OPTIMIZATION
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
      KD            Quantization       Pruning
        │                │                │
        └────────────────┼────────────────┘
                         ↓
                  Candidate Models
                         │
                         ↓
                    ESP32-S3
                         │
             ┌───────────┼───────────┐
             ↓           ↓           ↓
          Accuracy    Latency      Memory
                                     │
                                     ↓
                                   Energy
                                     │
                                     ↓
                             Pareto Analysis
```
---
# 8. Phần cứng
## Target chính
**ESP32-S3**
ESP32-S3 có dual-core Xtensa LX7 tới 240 MHz, 512 KB SRAM và hỗ trợ vector instructions cho workload neural-network/DSP; các module có thể dùng external Flash/PSRAM. ([Espressif Systems][4])
### Nhưng nghiên cứu không khóa cứng vào ESP32-S3.
Về sau:
```text
ESP32-S3
    ↓
Raspberry Pi
    ↓
Jetson
    ↓
NPU / Edge accelerator
```
Cùng một research methodology có thể chuyển sang hardware khác.
---
# 9. Software stack
## Training
```text
Python
PyTorch
TorchVision
CUDA
```
## Model conversion

```text
PyTorch
   ↓
ONNX
```

## Edge deployment

```text
ONNX / PyTorch
       ↓
ESP-PPQ
       ↓
ESP-DL
       ↓
.espdl
       ↓
ESP32-S3
```

ESP-DL hiện hỗ trợ export model từ PyTorch/ONNX sang `.espdl` để triển khai trên ESP32-S3. ([Espressif Systems][5])

## Firmware

```text
ESP-IDF
FreeRTOS
ESP-DL
ESP-NN
```

---

# 10. Dataset Strategy

Không dùng ngay dataset ADAS lớn.

Chia thành 3 stage.

---

## Stage A — Research prototyping

### CIFAR-10

Mục tiêu:

```text
Fast experiments
Fast ablation
Fast iteration
```

---

## Stage B — Tiny Vision

### CIFAR-100 / Tiny ImageNet

Mục tiêu:

```text
Model complexity ↑
Classification difficulty ↑
```

---

## Stage C — Real Edge Vision

Chọn một bài toán thực tế.

Ưu tiên:

```text
Person
Vehicle
Obstacle
Traffic sign
Road object
```

Có thể dùng dataset ADAS/traffic phù hợp sau khi framework ổn định.

---

# 11. Model Strategy

Không tự thiết kế architecture ngay.

## Baseline

```text
ResNet18
```

Mục đích:

> reference model.

## Efficient models

```text
MobileNetV2
MobileNetV3
EfficientNet-Lite
GhostNet
```

MobileNetV2 là model rất thích hợp để bắt đầu vì ESP-DL có workflow chính thức cho quantization/deployment trên ESP32-S3. ([Espressif Systems][2])

---

# 12. Giai đoạn nghiên cứu 1 — Baseline

## Mục tiêu

Biết rõ:

```text
Accuracy
Parameters
FLOPs
Model size
```

của từng model.

### Experiment

```text
ResNet18
MobileNetV2
MobileNetV3
GhostNet
```

### Bảng kết quả

| Model       | Params | FLOPs | FP32 Size | Accuracy |
| ----------- | -----: | ----: | --------: | -------: |
| ResNet18    |        |       |           |          |
| MobileNetV2 |        |       |           |          |
| MobileNetV3 |        |       |           |          |
| GhostNet    |        |       |           |          |

### Deliverable

```text
baseline_models/
benchmark_baseline.csv
baseline_analysis.ipynb
```

---

# 13. Giai đoạn 2 — Efficient Architecture

Nghiên cứu:

```text
Standard Conv
Depthwise Conv
Pointwise Conv
Residual
Bottleneck
Channel width
Network depth
```

So sánh:

```text
Accuracy
FLOPs
Parameters
Latency
```

Mục tiêu không phải tạo model mới.

Mục tiêu:

> **Hiểu tại sao lightweight architecture hiệu quả.**

---

# 14. Giai đoạn 3 — Post Training Quantization

Thử:

```text
FP32
INT16
INT8
```

Đo:

```text
Accuracy
Model size
Latency
Memory
```

Pipeline:

```text
FP32
 ↓
PTQ
 ↓
INT8
 ↓
ESP32-S3
```

ESP-DL hiện sử dụng symmetric power-of-two per-tensor quantization trên ESP32-S3. ([Espressif Systems][6])

---

# 15. Giai đoạn 4 — Quantization Sensitivity

Đây là lúc nghiên cứu bắt đầu sâu.

Với mỗi layer:

```text
Layer 1
Layer 2
Layer 3
...
Layer N
```

thực hiện:

```text
FP32 → INT8
```

và đo:

```text
ΔAccuracy
Quantization error
Latency
Memory
```

Tạo:

```text
Layer Sensitivity Map
```

Ví dụ:

| Layer      |  Error | Accuracy Impact | Latency | Memory |
| ---------- | -----: | --------------: | ------: | -----: |
| Conv1      |    low |             low |         |        |
| Block2     | medium |          medium |         |        |
| Block5     |   high |            high |         |        |
| Classifier |   high |            high |         |        |

ESP-DL hiện đã cung cấp graph-wise quantization error analysis, và tài liệu ESP32-S3 cho thấy một số layer có noise-to-signal power ratio cao hơn rõ rệt. ([Espressif Systems][2])

**Điểm này rất quan trọng:** ta không được claim “layer sensitivity analysis” tự nó là novelty. Nó là **measurement foundation** để xây phương pháp mới.

---

# 16. Giai đoạn 5 — Knowledge Distillation

Teacher:

```text
ResNet18
```

Student:

```text
MobileNetV2
```

Training:

$$
L = \alpha L_{CE} + \beta L_{KD}
$$

Thử:

```text
Temperature:
T = 2
T = 4
T = 8
```

và:

```text
α / β
```

### Kết quả cần tìm

```text
Student baseline
      vs
Student + KD
```

---

# 17. Giai đoạn 6 — Pruning

Không ưu tiên unstructured pruning.

Ưu tiên:

> **Structured / channel pruning**

vì mục tiêu cuối là hardware.

Pipeline:

```text
MobileNet
    ↓
Channel importance
    ↓
Remove channels
    ↓
Fine-tune
    ↓
Benchmark
```

Thử:

```text
10%
20%
30%
40%
50%
```

Đo:

```text
Accuracy
FLOPs
Latency
Memory
```

---

# 18. Giai đoạn 7 — Joint Compression

Bây giờ mới kết hợp:

```text
                 Baseline
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
       KD        Pruning    Quantization
        │           │           │
        └───────────┼───────────┘
                    ↓
             Joint optimization
```

So sánh:

```text
A: Baseline
B: KD
C: Pruning
D: Quantization
E: KD + Pruning
F: KD + Quantization
G: Pruning + Quantization
H: KD + Pruning + Quantization
```

Đây là **ablation study quan trọng nhất**.

---

# 19. Giai đoạn 8 — Hardware Profiling

Đưa từng model lên ESP32-S3.

Đo thực tế:

```text
Inference latency
Peak RAM
PSRAM
Flash
FPS
CPU utilization
Power
Energy / inference
```

Không dùng:

```text
FLOPs ≈ latency
```

để thay cho measurement.

Phải:

> **Measure actual hardware latency.**

---

# 20. Giai đoạn 9 — Hardware Cost Model

Đây là bước chuyển từ:

> Efficient DL

sang:

> **Hardware-Aware DL**

Tạo dataset:

```text
Model architecture
      ↓
Layer configuration
      ↓
Hardware measurement
```

Ví dụ:

| Layer  | Channels | Kernel | Precision | Latency | SRAM |
| ------ | -------: | -----: | --------- | ------: | ---: |
| Conv1  |       16 |    3×3 | INT8      |         |      |
| Conv2  |       32 |    3×3 | INT8      |         |      |
| DWConv |       64 |    3×3 | INT8      |         |      |
| ...    |          |        |           |         |      |

Sau đó xây:

```text
Hardware Cost Predictor
```

Ví dụ:

$$
Latency = f(layer, channels, kernel, precision)
$$

$$
Memory = g(layer, channels, activation, precision)
$$

---

# 21. Giai đoạn 10 — Hardware-Aware Optimization

Đây mới là **research core**.

Input:

```text
Model
+
Hardware constraints
+
Accuracy constraint
```

Output:

```text
Optimal compressed model
```

---

## Objective

Có thể định nghĩa:

$$
J =
\lambda_a L_{accuracy}
+
\lambda_l L_{latency}
+
\lambda_m L_{memory}
+
\lambda_e L_{energy}
$$

subject to:

$$
Accuracy \geq A_{min}
$$

$$
Latency \leq L_{max}
$$

$$
Memory \leq M_{max}
$$

---

# 22. Giai đoạn 11 — Precision Allocation

Không đơn giản:

```text
All layers → INT8
```

Mà:

```text
Layer 1 → INT8
Layer 2 → INT8
Layer 3 → INT16
Layer 4 → INT8
Layer 5 → INT16
...
```

Hoặc nếu runtime hỗ trợ thực tế:

```text
INT4
INT8
INT16
```

Nhưng phải **đo xem mixed precision có thật sự mang lại lợi ích trên ESP32-S3**; không được giả định rằng giảm bit luôn làm giảm latency.

ESP-DL hiện đã hỗ trợ mixed-precision quantization, nên novelty không thể chỉ là “có mixed precision”; novelty phải nằm ở **cách lựa chọn precision dựa trên sensitivity + hardware cost + accuracy constraint**. ([Espressif Systems][3])

---

# 23. Proposed Algorithm

Phiên bản đầu tiên có thể là:

```text
Algorithm: Hardware-Aware Precision Allocation

Input:
    pretrained model M
    target hardware H
    precision set P
    accuracy constraint A_min
    memory limit M_max
    latency limit L_max

Step 1:
    Profile every layer on H

Step 2:
    Calculate quantization sensitivity

Step 3:
    Estimate accuracy degradation
    for each precision option

Step 4:
    Estimate latency and memory cost

Step 5:
    Generate candidate precision assignments

Step 6:
    Solve multi-objective optimization

Step 7:
    Fine-tune model using QAT

Step 8:
    Deploy to ESP32-S3

Step 9:
    Measure real latency/memory/energy

Step 10:
    Update hardware cost model
```

Đây là **phiên bản research prototype**, chưa phải algorithm cuối.

---

# 24. Giai đoạn 12 — Pareto Optimization

Không nhất thiết phải tìm:

> một model duy nhất tốt nhất.

Tìm:

> **Pareto-optimal models.**

Ví dụ:

```text
Accuracy
  ↑
  │                     ● A
  │               ● B
  │          ● C
  │      ● D
  │  ● E
  └────────────────────────→
             Latency
```

A có accuracy cao.

E có latency thấp.

C có trade-off tốt nhất.

Sau đó có thể chọn:

```text
High accuracy model
Balanced model
Ultra-low latency model
```

---

# 25. Giai đoạn 13 — So sánh với baseline

Phải có:

```text
Baseline 1:
Original FP32

Baseline 2:
Standard PTQ

Baseline 3:
QAT

Baseline 4:
KD

Baseline 5:
Pruning

Baseline 6:
Existing ESP-DL optimization

Proposed:
Hardware-aware joint optimization
```

Đặc biệt baseline **ESP-DL optimization** rất quan trọng vì framework hiện đã có nhiều quantization optimization capabilities. ([Espressif Systems][2])

---

# 26. Giai đoạn 14 — Ablation Study

Phải có bảng:

| Method               | Accuracy | Latency | Memory | Energy |
| -------------------- | -------: | ------: | -----: | -----: |
| Baseline             |          |         |        |        |
| + KD                 |          |         |        |        |
| + Quantization       |          |         |        |        |
| + Pruning            |          |         |        |        |
| + KD + Quantization  |          |         |        |        |
| + KD + Pruning       |          |         |        |        |
| + Joint Optimization |          |         |        |        |

Sau đó:

### Ablation hardware-awareness

```text
Hardware-agnostic
        vs
Hardware-aware
```

Đây là thí nghiệm **cực kỳ quan trọng** để chứng minh research question.

---

# 27. Giai đoạn 15 — Real-world Vision

Sau khi classification ổn định:

```text
Camera
  ↓
Tiny Vision Model
  ↓
ESP32-S3
```

Bài toán:

```text
Person
Vehicle
Obstacle
Traffic sign
```

Không cần làm ADAS hoàn chỉnh.

Chỉ cần:

> **Edge Vision perception module**

để chứng minh phương pháp hoạt động trên dữ liệu thực.

---

# 28. Giai đoạn 16 — ADAS extension

Sau paper đầu tiên mới mở rộng:

```text
Tiny Vision
      ↓
Vehicle Detection
      ↓
Obstacle Detection
      ↓
Traffic Sign
      ↓
Road Scene
```

Sau đó:

```text
ESP32-S3
    │
    ↓
Perception
    │
    ↓
CAN/TWAI
    │
    ↓
Raspberry Pi / Jetson / ECU
```

Như vậy ADAS trở thành **application domain**, không làm research question bị loãng.

---

# 29. Timeline cụ thể — 12 tháng

## Tháng 1 — Deep Learning foundation

### Học

```text
CNN
Convolution
Depthwise Conv
Residual
BatchNorm
Efficient CNN
```

### Code

```text
ResNet18
MobileNetV2
MobileNetV3
```

### Deliverable

```text
baseline_models/
```

---

# Tháng 2 — Model efficiency

Học:

```text
FLOPs
MACs
Parameters
Memory
Latency
Depthwise convolution
Bottleneck
```

Benchmark 4 models.

### Deliverable

```text
baseline_benchmark.csv
```

---

# Tháng 3 — Quantization

Học:

```text
PTQ
QAT
INT8
INT16
Calibration
Quantization error
```

Implement:

```text
FP32
INT8 PTQ
INT8 QAT
```

### Deliverable

```text
quantization_report.md
```

---

# Tháng 4 — Quantization sensitivity

Thực hiện:

```text
Layer-wise analysis
```

Tạo:

```text
sensitivity_map.csv
```

và biểu đồ:

```text
Layer
vs
Quantization error
```

---

# Tháng 5 — Knowledge Distillation

Implement:

```text
Teacher → Student
```

Thử:

```text
T=2
T=4
T=8
```

### Deliverable

```text
kd_experiments.csv
```

---

# Tháng 6 — Pruning

Implement:

```text
Structured pruning
Channel pruning
```

Thử:

```text
10%
20%
30%
40%
50%
```

### Deliverable

```text
pruning_results.csv
```

---

# Tháng 7 — Joint compression

Thử:

```text
KD
+
Pruning
+
Quantization
```

### Deliverable

```text
joint_compression_report.md
```

---

# Tháng 8 — ESP32-S3

Chuyển:

```text
PyTorch
 ↓
ONNX
 ↓
ESP-PPQ
 ↓
ESP-DL
 ↓
ESP32-S3
```

ESP-DL có sẵn workflow cho PyTorch/ONNX → `.espdl` và deployment trên ESP32-S3. ([Espressif Systems][5])

### Deliverable

```text
esp32_benchmark.csv
```

---

# Tháng 9 — Hardware profiling

Đo:

```text
Latency
Memory
FPS
Power
Energy
```

cho tất cả candidate models.

### Deliverable

```text
hardware_profile.csv
```

---

# Tháng 10 — Hardware-aware optimization

Xây:

```text
Hardware Cost Model
+
Sensitivity Model
+
Optimization algorithm
```

### Deliverable

```text
hardware_aware_optimizer/
```

---

# Tháng 11 — Main experiments

Chạy:

```text
Baseline
vs
Existing methods
vs
Proposed method
```

Tạo:

```text
Tables
Figures
Ablation
Pareto plots
```

---

# Tháng 12 — Paper

Viết:

```text
Introduction
Related Work
Method
Experiments
Results
Ablation
Discussion
Limitations
Conclusion
```

---

# 30. Research repository

Project hiện tại nên tiến dần thành:

```text
ESP32CAM-EdgeAI_Projects/

├── firmware/
│
├── ml/
│   ├── datasets/
│   ├── models/
│   ├── training/
│   ├── compression/
│   │   ├── quantization/
│   │   ├── pruning/
│   │   └── distillation/
│   ├── nas/
│   └── evaluation/
│
├── hardware/
│   ├── esp32s3/
│   └── measurement/
│
├── experiments/
│   ├── 01_baseline/
│   ├── 02_efficiency/
│   ├── 03_quantization/
│   ├── 04_sensitivity/
│   ├── 05_distillation/
│   ├── 06_pruning/
│   ├── 07_joint_compression/
│   ├── 08_hardware_profile/
│   ├── 09_hardware_aware/
│   └── 10_final/
│
├── benchmarks/
│
├── results/
│   ├── raw/
│   ├── processed/
│   ├── figures/
│   └── tables/
│
├── docs/
│   ├── literature_review/
│   ├── research_questions/
│   ├── methodology/
│   └── experiments/
│
└── paper/
    ├── figures/
    ├── tables/
    ├── references/
    └── manuscript/
```

---

# 31. Research log

Mỗi experiment phải ghi:

```text
Experiment ID:
Date:

Research Question:
Hypothesis:

Dataset:
Model:

Method:
Hyperparameters:

Hardware:
Software:

Accuracy:
Parameters:
FLOPs:
Model Size:
Latency:
RAM:
PSRAM:
Power:
Energy:

Observation:

Conclusion:

Next experiment:
```

Không được có tình trạng:

```text
"Chạy thử thấy nhanh hơn."
```

Mọi claim phải có số liệu.

---

# 32. Bộ benchmark cuối

Paper cuối phải có ít nhất:

### Model-level

```text
Parameters
FLOPs
Model size
Accuracy
```

### Hardware-level

```text
Latency
FPS
SRAM
PSRAM
Flash
CPU utilization
```

### Energy-level

```text
Power
Energy/inference
Energy/frame
```

### Research-level

```text
Accuracy degradation
Compression ratio
Speedup
Memory reduction
Energy reduction
Pareto efficiency
```

---

# 33. Các biểu đồ bắt buộc

## Figure 1 — Research architecture

```text
Model
 ↓
Optimization
 ↓
Hardware
 ↓
Measurement
 ↓
Feedback
```

## Figure 2 — Model architecture

## Figure 3 — Quantization sensitivity

```text
Layer → Quantization error
```

## Figure 4 — Accuracy vs latency

## Figure 5 — Accuracy vs memory

## Figure 6 — Accuracy vs energy

## Figure 7 — Pareto frontier

## Figure 8 — Ablation study

## Figure 9 — ESP32-S3 deployment pipeline

---

# 34. Tiêu chí để biết đề tài có thành công không

Không đặt mục tiêu:

> “Accuracy phải cao hơn 2%.”

Đặt mục tiêu:

> **Tạo ra Pareto frontier tốt hơn baseline.**

Ví dụ:

```text
                 Accuracy
                    ↑
                    │       Baseline
                    │         ●
                    │
                    │    ● Proposed
                    │
                    └────────────────→
                         Latency
```

Nếu proposed:

```text
Accuracy tương đương
+
Latency thấp hơn
+
Memory thấp hơn
+
Energy thấp hơn
```

thì đó là kết quả rất tốt.

---

# 35. Điều kiện để có thể viết paper

Trước khi viết paper phải trả lời được:

### Câu 1

> Phương pháp mới là gì?

### Câu 2

> Nó khác gì so với ESP-DL/quantization/KD/pruning hiện tại?

### Câu 3

> Tại sao nó hiệu quả?

### Câu 4

> Có baseline mạnh không?

### Câu 5

> Có ablation không?

### Câu 6

> Có real hardware validation không?

### Câu 7

> Kết quả có lặp lại được không?

### Câu 8

> Có limitation không?

Nếu chưa trả lời được → **chưa viết paper**.

---

# 36. Research ladder sau paper đầu tiên

Nếu paper đầu tiên thành công:

```text
Paper 1
Hardware-Aware Compression
        ↓
Paper 2
Hardware-Aware Mixed Precision
        ↓
Paper 3
Hardware-Aware NAS
        ↓
Paper 4
Dynamic / Adaptive Inference
        ↓
Paper 5
Continual Learning on Edge
        ↓
ADAS Edge Intelligence
```

Tức là **một research direction**, không phải năm project rời rạc.

---

# 37. Hướng nâng cấp mạnh nhất: Hardware-Aware NAS

Sau khi có hardware cost model:

```text
Architecture
     +
Precision
     +
Compression
     ↓
       NAS
     ↓
Candidate A
Candidate B
Candidate C
...
     ↓
ESP32-S3
     ↓
Real measurement
```

NAS sẽ tối ưu:

$$
Architecture + Precision + Resource
$$

thay vì chỉ:

$$
Architecture \rightarrow Accuracy
$$

Các nghiên cứu gần đây đang mở rộng hardware-aware NAS sang quantization và dynamic inference/early-exit, cho thấy đây là hướng nghiên cứu có chiều sâu chứ không chỉ là model compression thông thường. ([arXiv][7])

---

# 38. Điểm dừng của từng phase

Không chuyển phase vì “đã học xong”.

Chỉ chuyển khi có **deliverable**.

```text
Phase 1
Baseline benchmark
        ↓
Phase 2
Efficient model analysis
        ↓
Phase 3
Quantization benchmark
        ↓
Phase 4
Sensitivity map
        ↓
Phase 5
KD benchmark
        ↓
Phase 6
Pruning benchmark
        ↓
Phase 7
Joint compression
        ↓
Phase 8
ESP32-S3 profiling
        ↓
Phase 9
Hardware cost model
        ↓
Phase 10
Proposed optimizer
        ↓
Phase 11
Ablation
        ↓
Phase 12
Paper
```

---

# 39. Nhiệm vụ đầu tiên: 14 ngày

Không làm tất cả cùng lúc.

## Ngày 1–3

Đọc:

```text
TinyDL survey
Edge AI acceleration survey
Hardware-aware Edge AI
```

Mục tiêu:

```text
Architecture
Compression
NAS
Hardware-aware optimization
```

Survey TinyDL 2025 là tài liệu nền rất phù hợp để bắt đầu vì nó bao quát architecture, quantization, pruning, NAS, hardware và toolchain. ([arXiv][1])

---

## Ngày 4–6

Implement:

```text
ResNet18
MobileNetV2
MobileNetV3
```

trên PyTorch.

---

## Ngày 7–8

Benchmark:

```text
Parameters
FLOPs
Model size
Accuracy
```

---

## Ngày 9–10

Học:

```text
PTQ
QAT
INT8
```

---

## Ngày 11–12

Quantize:

```text
MobileNetV2
```

và phân tích:

```text
Accuracy
Quantization error
```

---

## Ngày 13

Đọc tài liệu ESP-DL.

Đặc biệt:

```text
ESP32-S3 quantization
MobileNetV2
Quantization error
```

ESP-DL hiện đã có ví dụ cụ thể cho MobileNetV2 trên ESP32-S3 và cho phép phân tích quantization error theo layer. ([Espressif Systems][2])

---

## Ngày 14

Viết:

```text
docs/
├── research_questions.md
├── literature_review.md
├── baseline.md
└── research_gap.md
```

---

# 40. Kết quả mong muốn sau 3 tháng

Không phải paper.

Mà phải có:

```text
✓ Hiểu Efficient CNN
✓ 3–4 baseline models
✓ PTQ
✓ QAT
✓ Quantization sensitivity
✓ Benchmark framework
✓ Literature matrix
✓ Research gap sơ bộ
```

---

# 41. Kết quả mong muốn sau 6 tháng

```text
✓ KD
✓ Structured pruning
✓ Quantization
✓ Joint compression
✓ Ablation
✓ Model benchmark
✓ Initial paper hypothesis
```

---

# 42. Kết quả mong muốn sau 9 tháng

```text
✓ ESP32-S3 deployment
✓ Hardware profiling
✓ Latency dataset
✓ Memory dataset
✓ Energy dataset
✓ Hardware cost model
```

---

# 43. Kết quả mong muốn sau 12 tháng

```text
✓ Hardware-aware optimizer
✓ Proposed method
✓ Strong baselines
✓ Ablation
✓ Pareto analysis
✓ Real hardware validation
✓ Reproducible repository
✓ Manuscript
```

---

# 44. Mục tiêu cuối cùng

Research pipeline hoàn chỉnh phải trở thành:

```text
                 DATA
                  │
                  ▼
             TRAIN MODEL
                  │
                  ▼
          EFFICIENT ARCHITECTURE
                  │
                  ▼
       ┌──────────┼──────────┐
       ↓          ↓          ↓
      KD       PRUNING    QUANTIZATION
       │          │          │
       └──────────┼──────────┘
                  ↓
          HARDWARE PROFILING
                  │
                  ▼
       HARDWARE-AWARE OPTIMIZER
                  │
                  ▼
           OPTIMAL MODEL SET
                  │
                  ▼
              ESP32-S3
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
    Accuracy   Latency    Memory
                             │
                             ↓
                           Energy
                             │
                             ▼
                    PARETO FRONTIER
                             │
                             ▼
                         PAPER
```

## Research thesis cuối cùng

> **Deep Learning model không nên được thiết kế độc lập với hardware.**

Thay vào đó:

> **Architecture, compression, numerical precision và hardware constraints phải được tối ưu cùng nhau.**

Đó là lõi của **Hardware-Aware Efficient Deep Learning**.

Và ESP32-S3 là một target rất tốt để chứng minh ý tưởng này vì nó có nguồn lực MCU rõ ràng, vector acceleration và hệ sinh thái ESP-DL đủ trưởng thành để thực hiện benchmark thực tế. ([Espressif Systems][4])

**Mốc đầu tiên cần đạt không phải “chạy AI trên ESP32-S3”, mà là hoàn thành `Baseline → Quantization → Layer Sensitivity → Hardware Profiling`.** Sau khi có bốn thứ này, mới có đủ dữ liệu để xác định chính xác **research gap và thuật toán đề xuất**, thay vì đoán novelty ngay từ đầu.

