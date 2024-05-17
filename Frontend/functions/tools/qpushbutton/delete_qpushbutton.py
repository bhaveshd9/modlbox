from PySide6.QtWidgets import QMessageBox
from functions.tools.qpushbutton.predict_qpushButton import PredictPushButton
from functions.pages.prediction_page.qcombobox.prediction_method_selection_comboBox import PredictionMethodQComboBox
from functions.utils import *

class DeletePushButton:
    @staticmethod
    def open_warning_box_for_deleting_folder(self, path):
        ret = QMessageBox.warning(self, "Delete folder", "Are you sure you want to delete this folder?", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            delete_folder(self, path)
            self.predict_pushButton.setHidden(not PredictPushButton.is_predict_available(self))
            self.save_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
            self.delete_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
            self.save_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
            self.delete_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
            
            PredictionMethodQComboBox.addMethodOptions(self)
            
    @staticmethod
    def open_warning_box_for_deleting_file(self, file_path):
        ret = QMessageBox.warning(self, "Delete file", "Are you sure you want to delete this file?", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            delete_file(self, file_path)
            self.predict_pushButton.setHidden(not PredictPushButton.is_predict_available(self))
            self.save_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
            self.delete_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
            self.save_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
            self.delete_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
            PredictionMethodQComboBox.addMethodOptions(self)