import torch

try:
    # Attempt to import PyTorch
    import torch
    print("PyTorch is installed. Version:", torch.__version__)
except ImportError:
    # Print an error message if PyTorch is not installed
    print("PyTorch is not installed.")
    
try:
    # Attempt to import TensorBoard
    import tensorboard
    print("TensorBoard is installed.", tensorboard.__version__)
except ImportError:
    # Print an error message if TensorBoard is not installed
    print("TensorBoard is not installed.")
    
try:
    # Attempt to import PySide6
    from PySide6.QtWidgets import QApplication
    import PySide6
    print("PySide6 is installed.", PySide6.__version__)
except ImportError:
    # Print an error message if PySide6 is not installed
    print("PySide6 is not installed.")
