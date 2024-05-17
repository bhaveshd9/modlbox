from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QComboBox, QFileDialog

class SetupPage:
    def open_file(main_window):
        dirname = QFileDialog.getExistingDirectory(main_window, "Open Directory", "c:\\", QFileDialog.ShowDirsOnly)
        if dirname:
            main_window.file_path_label.setText(dirname)