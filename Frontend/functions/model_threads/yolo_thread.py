import string
from PySide6.QtCore import QThread, Signal
from numpy import string_
from sympy import true
from ultralytics import YOLO
import sys


import subprocess, time



class yolo_train_thread(QThread):
    started = Signal()
    on_train_finished = Signal()
    text = Signal(str)
    # stdout = Signal(str)
    # linescount = Signal(int)
    on_predict_finished = Signal()
    on_export_finished = Signal()

    def __init__(self, method, model_name, dataset, epochs: int, device, **kwargs):
        super().__init__()

        self.model_name = model_name
        self.method = method
        self.kwargs = kwargs
        self.dataset = dataset
        self.epochs = epochs
        self.device = device
        self.batch_size = kwargs.get("batch_size", 16)
        
    def run(self):
        print("Performing training...")
        print("dataset: ", self.dataset, "model: ", self.model_name, "epochs: ", self.epochs, "device: ", self.device, "batch_size: ", self.batch_size)

        self.started.emit()
        # ----------------------------------------
        # filters output
        
        if self.method == "Detection":
            proc = subprocess.Popen(["yolo", "detect", "train", f"data={self.dataset}", f"model={self.model_name}", f"epochs={self.epochs}", f"device={self.device}", "imgsz=640", f"batch={self.batch_size}", "project=runs/detect"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')

            
        elif self.method == "Classification":
            proc = subprocess.Popen([ "yolo", "classify", "train", f"data={self.dataset}", f"model={self.model_name}", f"epochs={self.epochs}",f"device={self.device}", "imgsz=224", f"batch={self.batch_size}", "project=runs/classify"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
        
        elif self.method == "obb":
            yolo_obb_model = "yolov8n-obb.pt"
            proc = subprocess.Popen([ "yolo", self.method, "train", f"data={self.dataset}", f"model={yolo_obb_model}", f"epochs={self.epochs}",f"device={self.device}", "imgsz=640", f"batch={self.batch_size}", "project=runs/detect"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
    
            
        for line in iter(proc.stdout.readline, ''):
            self.text.emit(line)
        
        proc.wait()

        self.on_train_finished.emit()




# init assumes model is already trained
class yolo_predict_thread(QThread):
    started = Signal()
    finished = Signal()
    stdout = Signal(str)
    text = Signal(str)
    on_predict_finished = Signal()
    linescount = Signal(int)
    # on_predict_finished = Signal()

    def __init__(self, model_name, source, **kwargs):
        super().__init__()
        self.model_name = model_name
        self.source = source
        self.kwargs = kwargs
        

    def run(self):
        # This is being USED
        # ----------------------------------------
        # filters output
        # proc = subprocess.Popen([ "yolo", "detect", "predict", f"model={self.model_name}", f"source={self.source}"], stdout=subprocess.PIPE,)
        
        # # WELL, THESE FOR THE TERMINAL SO FAR
        # for line in iter(proc.stdout.readline, ""):
        #     self.text.emit(line.strip())
            
        # self.text.emit("Prediction finished")
        # proc.wait()
        # time.sleep(5)  # Sleep for a short time before checking again

        model = YOLO(self.model_name)
        results = model.predict(self.source, save=True)
        self.text.emit("Prediction results \n")
       
        time.sleep(2)  # Sleep for a short time before checking again
        self.on_predict_finished.emit()
        
    
        # how to wait for the process to finish?
        # time.sleep(5)

        

        # the real code does filtering here


class yolo_export_thread(QThread):
    started = Signal()
    finished = Signal()
    stdout = Signal(str)
    text = Signal(str)
    linescount = Signal(int)
    on_export_finished = Signal()

    def __init__(self, model_name,format, **kwargs):
        super().__init__()
        self.model_name = model_name
        self.format = format
        self.kwargs = kwargs


    def run(self):
        # This is being USED
        self.started.emit()
        # ----------------------------------------
        # filters output
        proc = subprocess.Popen(["yolo", "export", f"model={self.model_name}", f"format={self.format}"], stdout=subprocess.PIPE,)
        
       # WELL, THESE FOR THE TERMINAL SO FAR
        for line in iter(proc.stdout.readline, ""):
            self.text.emit(line.strip())

        proc.wait()
        self.finished.emit()
        self.on_export_finished.emit()
        # the real code does filtering here
        # ----------------------------------------
