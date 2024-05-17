from PySide6.QtWidgets import QFileDialog

class OpenFileQPushButton:
    def openFile(self):
        self.dirname = QFileDialog.getExistingDirectory(self, "Open Directory", "c:\\", QFileDialog.ShowDirsOnly)
        if self.dirname:
            self.file_path_label.setText(f"File: {self.dirname}")