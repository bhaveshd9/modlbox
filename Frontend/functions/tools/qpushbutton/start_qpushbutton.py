import subprocess

from functions.model_threads.alexnet_thread import alexnet_thread

logdir = "runs"  # specify your log directory here
port = 6006
tensorboard_cmd = f"tensorboard --logdir={logdir} --port={port}" 
subprocess.Popen(tensorboard_cmd, shell=True)


from PySide6.QtCore import QSize, QThread
from PySide6.QtWidgets import QMessageBox
import os

from functions.model_threads.alexnet_thread import alexnet_thread
from functions.model_threads.yolo_thread import yolo_train_thread
from functions.top_menu.switch_page import SwitchPage
from functions.terminal.qtextbrowser.terminal_qtextbrowser import Terminal
from functions.terminal.qprogressbar.train_progressbar import Progress_Bar_Thread, TrainProgressBar
from functions.tools.qpushbutton.save_qpushbutton import SavePushButton
from functions.pages.prediction_page.qcombobox.prediction_method_selection_comboBox import PredictionMethodQComboBox
from functions.utils import *

import sys
import time



# Datasets avalible for use for models instantiated by torchvision
# datasets = {
#                 "Flowers102": data.Flowers102,
#                 "Country211": data.Country211,
#                 "VOC": data.VOCDetection,
#                 "COCO": data.CocoDetection
#             }

# Datasets availbile for use for YOLO models
ultralytics_datasets = {
    "COCO8": "coco8.yaml",
    "DOTA8": "dota8.yaml",
    "VOC": "VOC.yaml",
    "GlobalWheat2020": "GlobalWheat2020.yaml",
    "VisDrone": "VisDrone.yaml",
    "ImageNet10": "imagenet10",
    "ImageWoof320": "imagewoof320",
}

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


#================================



class StartPushButton:
    saved_model_info = {}
    
    @staticmethod
    def start(self, DEBUG=False):
        self.train_progressBar.setValue(0)
        if DEBUG:
            print("DEBUG: Starting the training setup process.")

        # Get user input values
        method = self.method_comboBox.currentText()
        model = self.model_comboBox.currentText()
        detection_stage = self.detection_stage_comboBox.currentText()
        gpu = self.gpu_comboBox.currentText()
        epochs = self.epochs_spinBox.value()
        selected_dataset = self.default_dataset_comboBox.currentText()
        batch_size = self.batch_size_spinBox.value()
        path_to_folder = self.file_path_label.text()
        
        selected_device = "cpu" if gpu == "cpu" else int(gpu)

        if DEBUG:
            print(f"DEBUG: User Input - Method: {method}, Model: {model}, Detection Stage: {detection_stage}, GPU: {gpu}, "
                f"Epochs: {epochs}, Dataset: {selected_dataset}, Batch Size: {batch_size}, Path: {path_to_folder}")

        # Initialize progress bar thread
        self.progress_bar_thread = Progress_Bar_Thread(method, selected_dataset)
        self.progress_bar_thread.progress.connect(lambda value: TrainProgressBar.update_progress_bar(self, value))
        self.train_thread = QThread()

        # Run thread based on method and model
        try:
            if method == "Classification":
                if model == "AlexNet":
                    self.train_thread = alexnet_thread(path_to_folder, epochs, batch_size, selected_dataset)
                    self.train_thread.progress.connect(lambda value: TrainProgressBar.update_progress_bar(self, value))
                    
                else:
                    dataset_yaml = ultralytics_datasets.get(selected_dataset)     
                    self.train_thread = yolo_train_thread(method, "yolov8n-cls.pt", dataset=dataset_yaml, epochs=epochs, device=selected_device, batch_size=batch_size)
                    

            elif method == "Detection":
                model_config = {
                    "YOLOv3": "yolov3.pt",
                    "YOLOv8": "yolov8n.pt",
                    "YOLOv5": "yolov5n.pt",
                    "YOLOv6": "yolov6n.yaml",
                    "YOLOv9": "yolov9c.pt"
                }
                if model in model_config:
                    dataset_yaml = ultralytics_datasets.get(selected_dataset)
                    if dataset_yaml is None:
                        if DEBUG:
                            print(f"DEBUG: Dataset not found for model {model}.")
                        QMessageBox.information(self, "Dataset not found", "The selected dataset is not available for this model.", QMessageBox.Ok)
                        return
                    if selected_dataset == "DOTA8":
                        method = "obb"
                    self.train_thread = yolo_train_thread(method, model_config[model], dataset=dataset_yaml, epochs=epochs, device=selected_device, batch_size=batch_size)
          
            self.train_thread.started.connect(lambda: StartPushButton.thread_start(self))
            self.train_thread.finished.connect(self.train_thread.deleteLater)
            self.train_thread.on_train_finished.connect(lambda: StartPushButton.thread_finish(self))
            self.train_thread.text.connect(lambda text: Terminal.append_text(self, text))
            
        except Exception as e:
            if DEBUG:
                print(f"DEBUG: An error occurred while setting up the training threads: {e}")

        # Determine the folder path based on the training method
        folder_path = ""
        if method == "Classification":
            folder_path = os.path.join(self.project_path, "runs", "classify", "train")
        else:
            folder_path = os.path.join(self.project_path, "runs", "detect", "train")

        if DEBUG:
            print(f"DEBUG: Computed run directory path: {folder_path}")

        # Check the existence and status of the target folder
        try:
            if os.path.exists(folder_path):
                if SavePushButton.check_if_folder_saved(folder_path):
                    delete_folder(self, folder_path)
                    SwitchPage.switchToGraphPage(self)
                    self.train_thread.start()
                else:
                    StartPushButton.open_information_box_for_running(self)
            else:
                if DEBUG:
                    print(f"DEBUG: The folder {folder_path} does not exist, switching to graph page.")
                SwitchPage.switchToGraphPage(self)
                self.train_thread.start()
        except Exception as e:
            if DEBUG:
                print(f"DEBUG: An error occurred while checking or manipulating the folder: {folder_path}. Error: {e}")

                
            
    def thread_start(self):
        print("Thread start")
        self.progress_bar_thread.start()
        self.start_pushButton.setHidden(True)
        self.save_detection_pushButton.setHidden(True)
        self.delete_detection_pushButton.setHidden(True)
        self.save_classification_pushButton.setHidden(True)
        self.delete_classification_pushButton.setHidden(True)
        self.open_image_file_pushButton.setEnabled(False)
        self.webEngineView.setHidden(False)
        
        
    def thread_finish(self):
        print("Thread finish")
        self.train_thread.quit()
        self.progress_bar_thread.stop()
        self.progress_bar_thread.quit()
        self.start_pushButton.setHidden(False)
        self.save_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
        self.delete_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
        self.save_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
        self.delete_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
        self.open_image_file_pushButton.setEnabled(True)
        
        PredictionMethodQComboBox.addMethodOptions(self)
        
    @staticmethod
    def open_information_box_for_running(self):
        QMessageBox.information(self, "Current train is not saved", "Please delete or save the current training before running a new one.", QMessageBox.Ok)
# ----------------------------TorchVision exp------------------
