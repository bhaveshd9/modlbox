import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from PySide6.QtCore import QThread, Signal
from torchvision import models
import subprocess
from torch.utils.tensorboard import SummaryWriter  # Added this import
import os
import yaml

from functions.terminal.qprogressbar.train_progressbar import Progress_Bar_Thread, TrainProgressBar

class alexnet_thread(QThread):
    started = Signal()
    finished = Signal()
    stdout = Signal(str)
    text = Signal(str)
    linescount = Signal(int)
    progress = Signal(int)

    def __init__(self, path_to_folder: str, epochs: int, batch_size: int, dataset: str, **kwargs):
        super().__init__()
        self.path_to_folder = path_to_folder
        self.epochs = epochs
        self.batch_size = batch_size
        self.dataset = dataset
        self.kwargs = kwargs
           
    def run(self):
        print("model: alexnet", " dataset: ", self.dataset, "epochs: ", self.epochs, "batch_size: ", self.batch_size)
        self.started.emit()
        
        # TensorBoard setup
        logdir = "runs"  # specify your log directory here

        # Connect stdout of subprocess to emit its output
        # for line in iter(proc.stdout.readline, ""):
        #     self.text.emit(line.strip())

        writer = SummaryWriter(logdir)  # Ensure that writer is a SummaryWriter object

        # Data preprocessing
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        current_directory = os.getcwd()

        # Use the home directory as the root for the dataset
        default_path = os.path.join(current_directory, "datasets")

        set_dataset =  torchvision.datasets.Flowers102(root=default_path, split='train', download=True, transform=transform)

        # train_dataset = torchvision.datasets.Flowers102(root=self.path_to_folder, split='train', download=True, transform=transform)
        train_loader = torch.utils.data.DataLoader(set_dataset, batch_size=self.batch_size, shuffle=True)

        # Model setup
        alexnet = models.alexnet(pretrained=True)
        num_classes = 102  # Modify this according to your dataset
        alexnet.classifier[6] = nn.Linear(4096, num_classes)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(alexnet.parameters(), lr=0.001, momentum=0.9)

        # Training loop
        for epoch in range(self.epochs):
            running_loss = 0.0
            # TrainProgressBar.update_progress_bar(self, epoch)
            self.progress.emit(epoch)
            for i, data in enumerate(train_loader, 0):
                inputs, labels = data
                optimizer.zero_grad()
                outputs = alexnet(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()
                running_loss += loss.item()
                total_size = 0
                total_instances = 0
                gpu_memory = 0

                if torch.cuda.is_available():
                    gpu_memory += torch.cuda.memory_allocated()  # GPU memory usage in bytes

                        # Assuming each instance is one batch
                total_instances += inputs.size(0)

                        # Size of the inputs in bytes
                input_size_bytes = inputs.element_size() * inputs.nelement()
                total_size += input_size_bytes

                if torch.cuda.is_available():
                    # Convert GPU memory usage to megabytes for better readability
                    gpu_memory_mb = gpu_memory / (1024 * 1024)
                else:
                    gpu_memory_mb = 0

                if i % 255 == 254:  # Print every 255 mini-batches
                    avg_loss = running_loss / 255
                    self.text.emit('[%d, %5d] loss: %.3f | GPU_mem: %.3f MB | Instances: %d | Size: %d bytes' %
                      (epoch + 1, i + 1, avg_loss, gpu_memory_mb, total_instances, total_size))
                    writer.add_scalar('Training Loss', avg_loss, epoch * len(train_loader) + i)  # Log the training loss

                    running_loss = 0.0

        self.progress.emit(self.epochs)
        # Save the entire model (architecture + parameters) to a file
        # torch.save(alexnet, 'alexnet_model.pth')
        project_folder = os.getcwd()
        directory = os.path.join(project_folder, "runs", "classify", "train")
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        # torch.save(alexnet.state_dict(), 'alexnet_model.pth')
        torch.save(alexnet.state_dict(), os.path.join(directory, 'alexnet_model.pth'))

        # GENERATE ARGS FILE
        args = {
            'model': "alexnet_model.pth",
            'data': self.dataset,
            'epochs': self.epochs,
            'save_dir': "runs\classify\train"
        }
        yaml_file_path = os.path.join(directory, 'args.yaml')
        with open(yaml_file_path, 'w') as file:
            yaml.dump(args, file)
                    
        writer.close()

        print("Training complete.")
        self.finished.emit()
