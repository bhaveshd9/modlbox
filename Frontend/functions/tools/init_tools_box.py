import os

from functions.previous_trains_list.update_previous_trains_list import PreviousTrainsList

from functions.tools.qpushbutton.reset_qpushbutton import ResetPushButton
from functions.tools.qpushbutton.start_qpushbutton import StartPushButton
from functions.tools.qpushbutton.stop_qpushButton import StopPushButton
from functions.tools.qpushbutton.predict_qpushButton import PredictPushButton
from functions.tools.qpushbutton.save_qpushbutton import SavePushButton
from functions.tools.qpushbutton.delete_qpushbutton import DeletePushButton
from functions.tools.qpushbutton.show_terminal_qpushbutton import ShowTerminalPushButton
from functions.tools.qpushbutton.hide_terminal_qpushbutton import HideTerminalPushButton
from functions.tools.qpushbutton.clear_terminal_qpushbutton import ClearTerminalPushButton

from functions.utils.files_modifiers import *

class Toolsbox:
    def initToolsBox(self):
        # SETUP
        self.stop_pushButton.setHidden(True)
        self.predict_pushButton.setHidden(True)
        self.save_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
        self.delete_detection_pushButton.setHidden(is_detection_runs_folder_empty(self))
        self.save_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
        self.delete_classification_pushButton.setHidden(is_classification_runs_folder_empty(self))
        self.show_terminal_pushButton.setHidden(True)
                
        # FUNCTIONS
        self.reset_pushButton.clicked.connect(lambda: ResetPushButton.resetOptions(self))
        
        self.start_pushButton.clicked.connect(lambda: StartPushButton.start(self, DEBUG=True))
        
        self.predict_pushButton.clicked.connect(lambda: PredictPushButton.predict(self))
        
        self.save_detection_pushButton.clicked.connect(lambda: SavePushButton.save_to_saved_folder(self, source_folder=os.path.join(self.project_path, "runs", "detect", "train"), destination_folder=os.path.join("saved", "detect")))
        self.save_detection_pushButton.clicked.connect(lambda: PreviousTrainsList.update_previous_detection_trains_list(self))
        
        self.save_classification_pushButton.clicked.connect(lambda: SavePushButton.save_to_saved_folder(self, source_folder=os.path.join(self.project_path, "runs", "classify", "train"), destination_folder=os.path.join("saved", "classify")))
        self.save_classification_pushButton.clicked.connect(lambda: PreviousTrainsList.update_previous_classification_trains_list(self))
        
        self.delete_detection_pushButton.clicked.connect(lambda: DeletePushButton.open_warning_box_for_deleting_folder(self, os.path.join(self.project_path, "runs", "detect", "train")))
        
        self.delete_classification_pushButton.clicked.connect(lambda: DeletePushButton.open_warning_box_for_deleting_folder(self, os.path.join(self.project_path, "runs", "classify", "train")))
        
        self.show_terminal_pushButton.clicked.connect(lambda: ShowTerminalPushButton.show_terminal(self))
        
        self.hide_terminal_pushButton_2.clicked.connect(lambda: HideTerminalPushButton.hide_terminal(self))
        
        self.clear_terminal_pushButton.clicked.connect(lambda: ClearTerminalPushButton.clear_terminal(self))
    