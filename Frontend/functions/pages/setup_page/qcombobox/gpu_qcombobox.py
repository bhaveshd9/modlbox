import subprocess
import torch

class GPUQComboBox:
    def updateGPUOptions(self):
        
        self.gpu_comboBox.clear()
        self.gpu_comboBox.addItem("cpu")
        if torch.cuda.is_available():
            device_count = torch.cuda.device_count()
            for i in range(device_count):
                self.gpu_comboBox.addItem(str(i))
        
