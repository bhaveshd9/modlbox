import os

from functions.utils import *

class OpenLocationFolderButton:
    def open_saved_train_folder(self, train_path):
        full_path = os.path.join(self.project_path, train_path)
        open_file_location(full_path)