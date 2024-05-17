from ast import main
from gettext import find
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os
import torch
import torchvision
from torchvision import transforms
from PIL import Image
import json
from ultralytics import YOLO
import scipy
import torchvision.models as models
from functions.model_threads.alexnet_thread import alexnet_thread
from functions.model_threads.yolo_thread import yolo_predict_thread
from functions.terminal.qtextbrowser.terminal_qtextbrowser import Terminal

from functions.utils import *

import sys
# from mainwindow_ui import Ui_MainWindow

class PredictPushButton:
    imgdirname = ""
    
    @staticmethod
    def predict(main_window):
        
        selected_model = main_window.prediction_model_selection_comboBox.currentText()
        if PredictPushButton.imgdirname == "":
            mw.prediction_label.setText("Please select an image file.")
            return
        mw = main_window
        mw.prediction_label.setText("")
        # print("Predicting...")
        input_image_path = PredictPushButton.imgdirname
        print("Input image path: ", PredictPushButton.imgdirname)
        if (selected_model == "alexnet_model.pth"):
            class_names = [
            "pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", 
            "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle", "snapdragon", 
            "colt's foot", "king protea", "spear thistle", "yellow iris", "globe-flower", "purple coneflower", 
            "peruvian lily", "balloon flower", "giant white arum lily", "fire lily", "pincushion flower", 
            "fritillary", "red ginger", "grape hyacinth", "corn poppy", "prince of wales feathers", 
            "stemless gentian", "artichoke", "sweet william", "carnation", "garden phlox", "love in the mist", 
            "mexican aster", "alpine sea holly", "ruby-lipped cattleya", "cape flower", "great masterwort", 
            "siam tulip", "lenten rose", "barbeton daisy", "daffodil", "sword lily", "poinsettia", 
            "bolero deep blue", "wallflower", "marigold", "buttercup", "daisy", "common dandelion", 
            "petunia", "wild pansy", "primula", "sunflower", "pelargonium", "bishop of llandaff", 
            "geranium", "orange dahlia", "pink-yellow dahlia", "cauliflower", "cape dandelion", "orange daisy", 
            "mexican aster", "butterbur", "oxeye daisy", "common dandelion", "shasta daisy", "yellow iris", 
            "japanese anemone", "black-eyed susan", "silky primrose", "fire lily", "pincushion flower", 
            "petunia", "prince of wales feathers", "moon orchid", "globe thistle", "coralbean", 
            "blackberry lily", "spear thistle", "balloon flower", "blanket flower", "trumpet creeper", 
            "blackberry lily", "snapdragon", "camellia", "king protea", "spear thistle", "yellow iris", 
            "globe-flower", "globe thistle", "purple coneflower", "peruvian lily", "ball moss", "foxglove", 
            "bougainvillea", "camellia", "mallow", "mexican petunia", "bromelia", "blanket flower"
        ]

            mw = main_window
            if PredictPushButton.imgdirname == "":
                mw.prediction_label.setText("Please select an image file.")
                return
            else:
                mw.prediction_label.setText("")
            input_image_path = PredictPushButton.imgdirname

            # Load the pre-trained AlexNet model
            # alexnet = torchvision.models.alexnet(pretrained=True)

            # Load the pre-trained AlexNet model
            alexnet = models.alexnet(pretrained=True)

            # Define the number of output classes in your specific task
            num_classes = 102  # Change this to the number of classes in your task

            # Modify the final fully connected layer to have the desired number of output features
            alexnet.classifier[6] = torch.nn.Linear(4096, num_classes)

            # Define the filename of the pretrained model
            pretrained_model_filename = "alexnet_model.pth"

            # Construct the full path to the pretrained model file
            pretrained_model_path = os.path.join(main_window.project_path, "runs", "classify", "train", pretrained_model_filename)

            # Check if the file exists
            if os.path.exists(pretrained_model_path):
                print("Pretrained model file exists. Loading...")
                # Load the pretrained model state dictionary
                state_dict = torch.load(pretrained_model_path)
                
                # Check if the state_dict contains the correct keys for the modified model
                if 'classifier.6.weight' in state_dict and 'classifier.6.bias' in state_dict:
                    # Load only the parameters of the final fully connected layer
                    alexnet.classifier[6].weight.data.copy_(state_dict['classifier.6.weight'])
                    alexnet.classifier[6].bias.data.copy_(state_dict['classifier.6.bias'])
                    
                    print("Pretrained model weights loaded successfully.")
                else:
                    print("Pretrained model does not contain necessary keys for the modified model.")
            else:
                print(f"Pretrained model file '{pretrained_model_path}' does not exist.")

            # Set the model to evaluation mode
            alexnet.eval()

            # Define transformation for input images
            transform = transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])

            # Function to predict the class of an input image
            def predict_image_class(image_path, model, transform):
                image = Image.open(image_path)
                image = transform(image).unsqueeze(0)  # Add a batch dimension
                with torch.no_grad():
                    output = model(image)
                probabilities = torch.nn.functional.softmax(output[0], dim=0)
                predicted_class_index = torch.argmax(probabilities).item()
                return predicted_class_index, probabilities[predicted_class_index]

            # Path to the input image
            image_path = input_image_path

            # Perform prediction
            predicted_class_index, confidence = predict_image_class(image_path, alexnet, transform)
            parent_directory = os.getcwd() # Get the parent directory of the current working directory
            file_path = os.path.join(parent_directory, 'datasets/flowers-102/imagelabels.mat')
            imagenet_classes_mat = scipy.io.loadmat(file_path)
            labels = imagenet_classes_mat['labels'][0]
            print(f"Image label: {class_names[predicted_class_index]}")
            print(f"Predicted class label index: {predicted_class_index}")
            print(f"Confidence: {confidence.item():.3f}")
            print(f"Confidence: {confidence.item() * 100:.3f}%")
            Terminal.append_text(main_window,f"Image label: {class_names[predicted_class_index]}")
            Terminal.append_text(main_window,f"Predicted class label index: {predicted_class_index}")
            Terminal.append_text(main_window,f"Confidence: {confidence.item():.3f}")
            Terminal.append_text(main_window,f"Confidence in percentage: {confidence.item() * 100:.3f}%")

        else:
            model_path = None
            if (selected_model == "yolov8n-cls.pt"):
                model_path = "runs/classify/train/weights/best.pt"

            elif (selected_model == "yolov3.pt" or selected_model == "yolov8n.pt" or selected_model == "yolov5n.pt" or selected_model == "yolov6n.yaml" or selected_model == "yolov9c.pt" or selected_model == "yolov8n-obb.pt"):
                model_path = "runs/detect/train/weights/best.pt"
            
            print("Model path: ", model_path)
            model_path = model_path if os.path.exists(model_path) else None
            # if main_window.train_thread is not None and (main_window.train_thread.isRunning() or not main_window.train_thread.isFinished()):
            #     Terminal.append_text(main_window, "Error: Please wait for the training to finish.")
            #     return
            main_window.ypthread = yolo_predict_thread(model_path, input_image_path, imgsz=640)
            main_window.ypthread.on_predict_finished.connect(lambda: PredictPushButton.display_predict_image(main_window))
            main_window.ypthread.finished.connect(main_window.ypthread.deleteLater)
            main_window.ypthread.text.connect(lambda text: Terminal.append_text(main_window, text))
            main_window.ypthread.started.connect(lambda: Terminal.append_text(main_window, "Performing prediction..."))
            main_window.ypthread.start()

            # model = YOLO(model_path)
            # model.predict(input_image_path, save=True, imgsz=640)
       
        
        
    def display_predict_image(main_window):
       
        mw = main_window
        latest_detection = PredictPushButton.find_latest_image("runs/detect", ignore=["train"])
        latest_obb = PredictPushButton.find_latest_image("runs/obb", ignore=["train"])
        latest_classification = PredictPushButton.find_latest_image("runs/classify", ignore=["train"])
        latest_classified = PredictPushButton.find_latest_image("alexnet_model.pth", ignore=["train"])
        
        
        # if latest_detection is None and latest_obb is None and latest_classified is None:
        #     Terminal.append_text(mw, "Error: No prediction image found.")
        #     return
        # if latest_detection is None and latest_obb is None:
        #     latest_prediction = latest_classified
        # elif latest_detection is None:
        #     latest_prediction = PredictPushButton.last_modified_time(latest_obb, latest_classified)
        # elif latest_obb is None:
        #     latest_prediction = PredictPushButton.last_modified_time(latest_detection, latest_classified)
        # else:
        latest_prediction = PredictPushButton.last_modified_time(latest_detection, latest_obb)
        latest_prediction = PredictPushButton.last_modified_time(latest_prediction, latest_classified)
        latest_prediction = PredictPushButton.last_modified_time(latest_prediction, latest_classification)
        image_path = latest_prediction

        print(image_path)
    
        print("Displaying prediction image")
        print("Image path: ", image_path)
        if os.path.exists(image_path):
            mw.original_pixmap = QPixmap(image_path)
            mw.prediction_label.setPixmap(mw.original_pixmap.scaled(mw.prediction_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            Terminal.append_text(mw, "Error: Image file not found.")
                 
    def find_latest_image(directory, ignore=None):
        if directory is None or not os.path.exists(directory):
            return None
        if ignore is None:
            ignore = []

        latest_image = None
        latest_mod_time = 0

        # Walk through all directories and files in the given directory
        for root, dirs, files in os.walk(directory, topdown=True):
            # Filter out the directories to ignore
            dirs[:] = [d for d in dirs if d not in ignore]

            for file in files:
                # Check for common image file extensions
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                    file_path = os.path.join(root, file)
                    mod_time = os.path.getmtime(file_path)

                    # Update the latest image if this file is newer
                    if mod_time > latest_mod_time:
                        latest_mod_time = mod_time
                        latest_image = file_path

        return latest_image
    
    
    def last_modified_time(file_path1, file_path2, DEBUG=False):
        # Debugging log for initial paths
        if DEBUG:
            print(f"Received file_path1: {file_path1}")
            print(f"Received file_path2: {file_path2}")
        if file_path1 is None and file_path2 is None:
            if DEBUG:
                print("Both file paths are None")
            return None
        if file_path1 is None:
            if DEBUG:
                print("file_path1 is None")
            return file_path2
        if not os.path.exists(file_path1):
            if DEBUG:
                print(f"file_path1 does not exist: {file_path1}")
            return file_path2

        if file_path2 is None:
            if DEBUG:
                print("file_path2 is None")
            return file_path1
        if not os.path.exists(file_path2):
            if DEBUG:
                print(f"file_path2 does not exist: {file_path2}")
            return file_path1

        file_path1_mtime = os.path.getmtime(file_path1)
        file_path2_mtime = os.path.getmtime(file_path2)

        if DEBUG:
            print(f"Modification time for file_path1: {file_path1_mtime}")
            print(f"Modification time for file_path2: {file_path2_mtime}")

        # Determine which file is newer based on modification time
        if file_path1_mtime > file_path2_mtime:
            if DEBUG:
                print(f"Returning file_path1: {file_path1}")
            return file_path1
        else:
            if DEBUG:
                print(f"Returning file_path2: {file_path2}")
            return file_path2
        
    
    def is_predict_available(self):
        is_image_available = self.prediction_file_path_label.text() != "File:"
        is_model_available =  os.path.exists(os.path.join(self.project_path, "runs", "classify", "train")) \
                           or os.path.exists(os.path.join(self.project_path, "runs", "detect", "train"))
        return (is_image_available and is_model_available)
