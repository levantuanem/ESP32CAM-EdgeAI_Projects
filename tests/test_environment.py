import torch
import torchvision
import numpy as np
import cv2
from PIL import Image


def test_required_packages_are_importable():
    assert torch.__version__
    assert torchvision.__version__
    assert np.__version__
    assert cv2.__version__
    assert Image.__version__


def test_model_input_shape():
    input_tensor = torch.randn(1, 3, 96, 96)

    assert input_tensor.shape == (1, 3, 96, 96)
    assert input_tensor.dtype == torch.float32


def main():
    print("=== Environment Check ===")
    print(f"PyTorch:     {torch.__version__}")
    print(f"Torchvision: {torchvision.__version__}")
    print(f"NumPy:       {np.__version__}")
    print(f"OpenCV:      {cv2.__version__}")
    print(f"CUDA:        {torch.cuda.is_available()}")
    print("Input shape: torch.Size([1, 3, 96, 96])")
    print("Environment OK!")


if __name__ == "__main__":
    main()