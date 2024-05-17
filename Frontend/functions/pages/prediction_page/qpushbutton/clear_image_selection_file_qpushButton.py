from ast import main
from PySide6.QtWidgets import QFileDialog
from sympy import N
from functions.tools.qpushbutton.predict_qpushButton import PredictPushButton


class ClearImageFileSelectionButton:
    
    def clearImageSelection(self):
        self.imgdirname = ""
        PredictPushButton.imgdirname = ""
        self.predict_pushButton.setHidden(True)
        
        self.prediction_file_path_label.setText("File:")
        self.source_label.clear()
        self.prediction_label.clear()