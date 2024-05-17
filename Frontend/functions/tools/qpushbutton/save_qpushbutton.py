import os
import shutil
import yaml
import time

from datetime import datetime

from functions.terminal.qtextbrowser.terminal_qtextbrowser import Terminal
from functions.utils import *
from ui_mainwindow import Ui_MainWindow

class SavePushButton:
    
    @staticmethod
    def save_to_saved_folder(self, source_folder, destination_folder):
        source_folder = os.path.join(self.project_path, source_folder)
        destination_folder = os.path.join(self.project_path, destination_folder)
        try:
            if os.path.exists(source_folder):
                orginal_folder_name = source_folder.split(os.path.sep)[-1]
                final_folder_name = orginal_folder_name
                dest_folder = os.path.join(destination_folder, orginal_folder_name)
                if os.path.exists(dest_folder):
                    i = 2
                    while os.path.exists(dest_folder):
                        final_folder_name = f"{orginal_folder_name}_{i}"
                        dest_folder = os.path.join(destination_folder, final_folder_name)
                        i += 1
                SavePushButton.update_yaml_file_when_saved(source_folder, dest_folder)
                copy_folder(self, source_folder, dest_folder)

        except Exception as e:
            Terminal.append_text("Cannot save model:", str(e))
            
    
    @staticmethod
    def update_yaml_file_when_saved(source_file_path, dest_file_path):
        yaml_file_path = os.path.join(source_file_path, "args.yaml")
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)

        if data is not None and 'save_dir' in data:
            data['save_dir'] = dest_file_path
            data['saved_time'] = int(time.time())
            data['saved_time_iso8601'] = datetime.fromtimestamp(data['saved_time']).isoformat()
            
            formatted_saved_time_iso8601 = datetime.strptime(data['saved_time_iso8601'], "%Y-%m-%dT%H:%M:%S").strftime("%m/%d/%Y %H:%M:%S")
            data['saved_time_iso8601'] = formatted_saved_time_iso8601

        with open(yaml_file_path, 'w') as file:
            yaml.dump(data, file)
            

    @staticmethod
    def check_if_folder_saved(file_path):
        yaml_file_path = os.path.join(file_path, "args.yaml")
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)
        
        if data is not None and 'saved_time_iso8601' not in data:
            return False
        
        return True
    
    @staticmethod
    def get_latest_train(file_path):
        # Get the latest train folder from the given path
        latest_train = None
        latest_mod_time = 0
        for root, dirs, files in os.walk(file_path, topdown=True):
            for dir in dirs:
                if dir == "train":
                    train_path = os.path.join(root, dir)
                    mod_time = os.path.getmtime(train_path)
                    if mod_time > latest_mod_time:
                        latest_mod_time = mod_time
                        latest_train = train_path
        return latest_train