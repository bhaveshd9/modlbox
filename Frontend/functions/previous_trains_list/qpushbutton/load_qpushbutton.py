import os
import yaml

from PySide6.QtWidgets import QMessageBox

from functions.terminal.qtextbrowser.terminal_qtextbrowser import Terminal
from functions.tools.qpushbutton.save_qpushbutton import SavePushButton
from functions.tools.qpushbutton.predict_qpushButton import PredictPushButton
from functions.pages.prediction_page.qcombobox.prediction_method_selection_comboBox import PredictionMethodQComboBox
from functions.utils import *

class LoadPushButton:
    def load_saved_train_folder(self, train_path):
        full_source_path = os.path.join(self.project_path, train_path)
        outside_folder = os.path.basename((os.path.dirname(full_source_path)))
        full_dest_path = os.path.join(self.project_path, "runs", outside_folder, "train")
        if os.path.exists(full_dest_path):
            if (SavePushButton.check_if_folder_saved(full_dest_path)):
                delete_folder(self, full_dest_path)
                copy_folder(self, full_source_path, full_dest_path)
                self.predict_pushButton.setHidden(not PredictPushButton.is_predict_available(self))
                self.save_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
                self.delete_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
                self.save_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
                self.delete_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
                PredictionMethodQComboBox.addMethodOptions(self)
                
            else:
                LoadPushButton.open_information_box_for_loading(self)
        else:        
            copy_folder(self, full_source_path, full_dest_path)
            self.predict_pushButton.setHidden(not PredictPushButton.is_predict_available(self))
            self.save_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
            self.delete_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
            self.save_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
            self.delete_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
            PredictionMethodQComboBox.addMethodOptions(self)         
            
    def move_model_file(self, path_file):
        args_yaml_path = os.path.join(path_file, "args.yaml")
        with open(args_yaml_path, 'r') as file:
            data = yaml.safe_load(file)
        if data is None:
            pass
        model_name = data['model']
        model_path = os.path.join(path_file, model_name)
        model_dest_path = os.path.join(self.project_path, model_name)
        if (os.path.exists(model_dest_path)):
            os.remove(model_dest_path)
            shutil.move(model_path, model_dest_path)
            Terminal.append_text(self, model_name + " loaded.")
        else:
            shutil.move(model_path, model_dest_path)
            Terminal.append_text(self, model_name + " loaded.")
            
    @staticmethod
    def open_information_box_for_loading(self):
        QMessageBox.information(self, "Current train is not saved", "Please delete or save the current training before loading.", QMessageBox.Ok)