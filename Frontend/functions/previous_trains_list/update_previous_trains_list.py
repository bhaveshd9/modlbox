import os
import yaml

from PySide6.QtGui import QCursor
from PySide6.QtCore import QSize, Qt, QCoreApplication
from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox

from functions.previous_trains_list.qpushbutton.load_qpushbutton import LoadPushButton
from functions.previous_trains_list.qpushbutton.open_location_folder_qpushbutton import OpenLocationFolderButton

from functions.terminal.qtextbrowser.terminal_qtextbrowser import Terminal

from functions.utils import *

class PreviousTrainsList:
    @staticmethod
    def update_previous_trains_list(self):
        PreviousTrainsList.update_previous_detection_trains_list(self)
        PreviousTrainsList.update_previous_classification_trains_list(self)
        
    @staticmethod
    def update_previous_detection_trains_list(self):
        layout = self.previousDetectionTrainsListVerticalLayout
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                sublayout = child.layout()
                while sublayout.count():
                    subchild = sublayout.takeAt(0)
                    if subchild.widget():
                        subchild.widget().deleteLater()
                        
        saved_detect_path = "saved/detect"
        
        
        if not os.path.exists(saved_detect_path):
            try:
                new_dir_path = os.path.join(self.project_path, "saved", "detect")
                os.makedirs(new_dir_path)
                Terminal.append_text(self, f"New directory created: {new_dir_path}")
            except OSError as e:
                Terminal.append_text(self, f"Error: {e.strerror}")
                                  
        folders = [f.name for f in os.scandir(saved_detect_path) if f.is_dir()]
        
        if not folders:
            return
        

        previous_detection_trains_list_label = QLabel(self.previous_detection_trains_list)
        previous_detection_trains_list_label.setObjectName(u"previous_detection_trains_list_label")
        previous_detection_trains_list_label.setText(QCoreApplication.translate("MainWindow", u"DETECTION", None))
        self.previousDetectionTrainsListVerticalLayout.addWidget(previous_detection_trains_list_label, 0, Qt.AlignLeft|Qt.AlignTop)
        
        for folder in folders:
            args_yaml_path = os.path.join(saved_detect_path, folder, "args.yaml")
            if not os.path.exists(args_yaml_path):
                continue
            
            with open(args_yaml_path, 'r') as file:
                data = yaml.safe_load(file)
                
            if data is None:
                continue
            
            model_name = data['model']
            dataset_name = data['data']
            saved_time = data['saved_time_iso8601']
            file_path = data['save_dir']
            
            
            
            previous_model_frame = QFrame(self.previous_detection_trains_list)
            previous_model_frame.setObjectName(folder + "_frame")
            previous_model_frame.setFrameShape(QFrame.StyledPanel)
            previous_model_frame.setFrameShadow(QFrame.Raised)
            previous_model_frame.setStyleSheet("QFrame {background-color: rgb(40, 44, 52);}")
            previousModelFrameverticalLayout = QVBoxLayout(previous_model_frame)
            previousModelFrameverticalLayout.setSpacing(5)
            previousModelFrameverticalLayout.setObjectName(u"previousModelFrameverticalLayout")
            previousModelFrameverticalLayout.setContentsMargins(5, 5, 5, 5)
            
            model_name_label = QLabel(previous_model_frame)
            model_name_label.setObjectName(folder +"_model_name_label")
            model_name_label.setText("Model: " + model_name)
            previousModelFrameverticalLayout.addWidget(model_name_label)
            
            dataset_name_label = QLabel(previous_model_frame)
            dataset_name_label.setObjectName(folder +"_data_name_label")
            dataset_name_label.setText("Dataset: " + dataset_name)
            previousModelFrameverticalLayout.addWidget(dataset_name_label)
            
            saved_time_label = QLabel(previous_model_frame)
            saved_time_label.setObjectName(folder +"_saved_time_label")
            saved_time_label.setText("Saved time: " + saved_time)
            previousModelFrameverticalLayout.addWidget(saved_time_label)
                        
            previous_model_tools_frame = QFrame(previous_model_frame)
            previous_model_tools_frame.setObjectName(folder + "_tools_frame")
            previous_model_tools_frame.setFrameShape(QFrame.StyledPanel)
            previous_model_tools_frame.setFrameShadow(QFrame.Raised)
            previousModelToolsFrameHorizontalLayout = QHBoxLayout(previous_model_tools_frame)
            previousModelToolsFrameHorizontalLayout.setObjectName(folder + "PreviousModelToolsFrameHorizontalLayout")
            previousModelToolsFrameHorizontalLayout.setSpacing(1)
            previousModelToolsFrameHorizontalLayout.setContentsMargins(0, 0, 0, 0)
            
            load_pushButton = QPushButton(previous_model_tools_frame)
            load_pushButton.setObjectName(folder + "_load_pushButton")
            load_pushButton.setMaximumSize(QSize(16777215, 16777215))
            load_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
            load_pushButton.setText(u"Load")
            
            def on_load_button_click(path=file_path):
                return lambda: LoadPushButton.load_saved_train_folder(self, path)
            
            load_pushButton.clicked.connect(on_load_button_click())
            previousModelToolsFrameHorizontalLayout.addWidget(load_pushButton)
            
            location_pushButton = QPushButton(previous_model_tools_frame)
            location_pushButton.setObjectName(folder + "_location_pushButton")
            location_pushButton.setMaximumSize(QSize(16777215, 16777215))
            location_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
            location_pushButton.setText(u"Location")

            def on_location_button_click(path=file_path):
                return lambda: OpenLocationFolderButton.open_saved_train_folder(self, path)

            location_pushButton.clicked.connect(on_location_button_click())
            previousModelToolsFrameHorizontalLayout.addWidget(location_pushButton)
            
            delete_pushButton = QPushButton(previous_model_tools_frame)
            delete_pushButton.setObjectName(folder + "_delete_pushButton")
            delete_pushButton.setMaximumSize(QSize(16777215, 16777215))
            delete_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
            delete_pushButton.setText(u"Delete")
            
            def on_delete_button_click(path=file_path):
                return lambda: PreviousTrainsList.open_warning_box_for_deleting_saved_folder(self, path)
               
            delete_pushButton.clicked.connect(on_delete_button_click())
            
            
            previousModelToolsFrameHorizontalLayout.addWidget(delete_pushButton)
            
            previousModelFrameverticalLayout.addWidget(previous_model_tools_frame)
            
            self.previousDetectionTrainsListVerticalLayout.addWidget(previous_model_frame, 0, Qt.AlignTop)

        detection_verticalSpacer = QSpacerItem(20, 254, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.previousDetectionTrainsListVerticalLayout.addItem(detection_verticalSpacer)
           
    @staticmethod
    def update_previous_classification_trains_list(self):
        layout = self.previousClassificationTrainsListVerticalLayout
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                sublayout = child.layout()
                while sublayout.count():
                    subchild = sublayout.takeAt(0)
                    if subchild.widget():
                        subchild.widget().deleteLater()
                        
        saved_clas_path = "saved/classify"
        
        if not os.path.exists(saved_clas_path):
            try:
                new_dir_path = os.path.join(self.project_path, "saved", "classify")
                os.makedirs(new_dir_path)
                Terminal.append_text(self, f"New directory created: {new_dir_path}")
            except OSError as e:
                Terminal.append_text(self, f"Error: {e.strerror}")
                                  
        folders = [f.name for f in os.scandir(saved_clas_path) if f.is_dir()]
        
        if not folders:
            return
        

        previous_classification_trains_list_label = QLabel(self.previous_classification_trains_list)
        previous_classification_trains_list_label.setObjectName(u"previous_classification_trains_list_label")
        previous_classification_trains_list_label.setText(QCoreApplication.translate("MainWindow", u"CLASSIFICATION", None))
        self.previousClassificationTrainsListVerticalLayout.addWidget(previous_classification_trains_list_label, 0, Qt.AlignLeft|Qt.AlignTop)    
            
        for folder in folders:
            args_yaml_path = os.path.join(saved_clas_path, folder, "args.yaml")
            if not os.path.exists(args_yaml_path):
                continue
            
            with open(args_yaml_path, 'r') as file:
                data = yaml.safe_load(file)
                
            if data is None:
                continue
            
            model_name = data['model']
            dataset_name = data['data']
            saved_time = data['saved_time_iso8601']
            file_path = data['save_dir']
            
            previous_model_frame = QFrame(self.previous_classification_trains_list)
            previous_model_frame.setObjectName(folder + "_frame")
            previous_model_frame.setFrameShape(QFrame.StyledPanel)
            previous_model_frame.setFrameShadow(QFrame.Raised)
            previous_model_frame.setStyleSheet("QFrame {background-color: rgb(40, 44, 52);}")
            previousModelFrameverticalLayout = QVBoxLayout(previous_model_frame)
            previousModelFrameverticalLayout.setSpacing(5)
            previousModelFrameverticalLayout.setObjectName(u"previousModelFrameverticalLayout")
            previousModelFrameverticalLayout.setContentsMargins(5, 5, 5, 5)
            
            model_name_label = QLabel(previous_model_frame)
            model_name_label.setObjectName(folder +"_model_name_label")
            model_name_label.setText("Model: " + model_name)
            previousModelFrameverticalLayout.addWidget(model_name_label)
            
            dataset_name_label = QLabel(previous_model_frame)
            dataset_name_label.setObjectName(folder +"_data_name_label")
            dataset_name_label.setText("Dataset: " + dataset_name)
            previousModelFrameverticalLayout.addWidget(dataset_name_label)
            
            saved_time_label = QLabel(previous_model_frame)
            saved_time_label.setObjectName(folder +"_saved_time_label")
            saved_time_label.setText("Saved time: " + saved_time)
            previousModelFrameverticalLayout.addWidget(saved_time_label)
                        
            previous_model_tools_frame = QFrame(previous_model_frame)
            previous_model_tools_frame.setObjectName(folder + "_tools_frame")
            previous_model_tools_frame.setFrameShape(QFrame.StyledPanel)
            previous_model_tools_frame.setFrameShadow(QFrame.Raised)
            previousModelToolsFrameHorizontalLayout = QHBoxLayout(previous_model_tools_frame)
            previousModelToolsFrameHorizontalLayout.setObjectName(folder + "PreviousModelToolsFrameHorizontalLayout")
            previousModelToolsFrameHorizontalLayout.setSpacing(1)
            previousModelToolsFrameHorizontalLayout.setContentsMargins(0, 0, 0, 0)
            
            load_pushButton = QPushButton(previous_model_tools_frame)
            load_pushButton.setObjectName(folder + "_load_pushButton")
            load_pushButton.setMaximumSize(QSize(16777215, 16777215))
            load_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
            load_pushButton.setText(u"Load")
            
            def on_load_button_click(path=file_path):
                return lambda: LoadPushButton.load_saved_train_folder(self, path)
            
            load_pushButton.clicked.connect(on_load_button_click())
            previousModelToolsFrameHorizontalLayout.addWidget(load_pushButton)
            
            location_pushButton = QPushButton(previous_model_tools_frame)
            location_pushButton.setObjectName(folder + "_location_pushButton")
            location_pushButton.setMaximumSize(QSize(16777215, 16777215))
            location_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
            location_pushButton.setText(u"Location")

            def on_location_button_click(path=file_path):
                return lambda: OpenLocationFolderButton.open_saved_train_folder(self, path)

            location_pushButton.clicked.connect(on_location_button_click())
            previousModelToolsFrameHorizontalLayout.addWidget(location_pushButton)
            
            delete_pushButton = QPushButton(previous_model_tools_frame)
            delete_pushButton.setObjectName(folder + "_delete_pushButton")
            delete_pushButton.setMaximumSize(QSize(16777215, 16777215))
            delete_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
            delete_pushButton.setText(u"Delete")
            
            def on_delete_button_click(path=file_path):
                return lambda: PreviousTrainsList.open_warning_box_for_deleting_saved_folder(self, path)
               
            delete_pushButton.clicked.connect(on_delete_button_click())
            
            
            previousModelToolsFrameHorizontalLayout.addWidget(delete_pushButton)
            
            previousModelFrameverticalLayout.addWidget(previous_model_tools_frame)
            
            self.previousClassificationTrainsListVerticalLayout.addWidget(previous_model_frame)

        classification_verticalSpacer = QSpacerItem(20, 254, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.previousClassificationTrainsListVerticalLayout.addItem(classification_verticalSpacer)
    
    @staticmethod

    
    # WHEN SWITCH PAGE BUTTONS CLICKED
    def switchToPreviousDetectionTrainsListPage(self):
        self.previous_trains_list.setCurrentIndex(0)
        self.previous_trains_list_label.setText("DETECTION TRAINS LIST")
        
        
    def switchPreviousClassificationTrainsListPage(self):
        self.previous_trains_list.setCurrentIndex(1)
        self.previous_trains_list_label.setText("CLASSIFICATION TRAINS LIST")
    
    # WHEN DELETE BUTTON CLICKED    
    def delete_saved_folder(self, train_path):
        delete_folder(self, train_path)
        PreviousTrainsList.update_previous_trains_list(self)
    
    def open_warning_box_for_deleting_saved_folder(self, path):
        ret = QMessageBox.warning(self, "Delete folder", "Are you sure you want to delete this folder?", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            full_path = os.path.join(self.project_path, path)
            PreviousTrainsList.delete_saved_folder(self, full_path)