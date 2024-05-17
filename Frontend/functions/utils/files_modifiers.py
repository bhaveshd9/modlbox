import os
import shutil
import platform
import subprocess

from functions.terminal.qtextbrowser.terminal_qtextbrowser import Terminal

@staticmethod
def open_file_location(path):
        os_name = platform.system()
        if os_name == 'Windows':
            subprocess.run(['explorer', path])
        elif os_name == 'Darwin':
            subprocess.run(['open', path])
        elif os_name == 'Linux':
            subprocess.run(['xdg-open', path])
        else:
            raise OSError("Unsupported operating system")

@staticmethod        
def copy_folder(self, source, destination):
    try:
        shutil.copytree(source, destination)
        Terminal.append_text(self, f"Folder copied from '{source}' to '{destination}'")
    except OSError as e:
        Terminal.append_text(self, f"Error: {e.strerror}")
        
@staticmethod
def move_folder(source, destination):
    try:
        shutil.move(source, destination)
        Terminal.append_text(f"Folder moved from '{source}' to '{destination}'")
    except OSError as e:
        Terminal.append_text(f"Error: {e.strerror}")

@staticmethod        
def delete_folder(self, path):
    try:
        shutil.rmtree(path)
        Terminal.append_text(self, f"Deleted folder: {path}")
    except OSError as e:
        Terminal.append_text(self, f"Error: {path} : {e.strerror}")
        
@staticmethod
def delete_file(self, file_path):
    try:
        os.remove(file_path)
        Terminal.append_text(self, f"Deleted file: {file_path}")
    except OSError as e:
        Terminal.append_text(self, f"Error: {file_path} : {e.strerror}")
        
@staticmethod    
def is_detection_runs_folder_empty(self):
    print("[files_modifiers.py] is_detection_runs_folder_empty() project_path: ", self.project_path)
    
    path = os.path.join(self.project_path, "runs", "detect", "train")
    if os.path.exists(path):
        return False
    return True

@staticmethod
def is_classification_runs_folder_empty(self):
    print("[files_modifiers.py] is_classification_runs_folder_empty() project_path: ", self.project_path)
    path = os.path.join(self.project_path, "runs", "classify", "train")
    if os.path.exists(path):
        return False
    return True
    

