import torch
import torchvision
import numpy as np
import cv2
from PIL import Image


def main():
    print("=== Environment Check ===")
    print(f"PyTorch:     {torch.__version__}")
    print(f"Torchvision: {torchvision.__version__}")
    print(f"NumPy:       {np.__version__}")
    print(f"OpenCV:      {cv2.__version__}")
    print(f"CUDA:        {torch.cuda.is_available()}")

    x = torch.randn(1, 3, 96, 96)

    print(f"Input shape: {x.shape}")
    print("Environment OK!")


if __name__ == "__main__":
    main()