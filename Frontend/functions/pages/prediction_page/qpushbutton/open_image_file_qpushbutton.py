from ast import main
import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog
from functions.tools.qpushbutton.predict_qpushButton import PredictPushButton
from ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import Qt
from functions.utils import delete_folder


class OpenImageFileButton:
    def openImageFile(main_window: Ui_MainWindow):
        mw = main_window
        main_window.imgdirname, _ = QFileDialog.getOpenFileName(main_window, "Open Image", "", "Image Files (*.jpg *.jpeg *.png)")
        if main_window.imgdirname:
            PredictPushButton.imgdirname = main_window.imgdirname
            main_window.prediction_file_path_label.setText(f"File: {main_window.imgdirname}")
            main_window.predict_pushButton.setHidden(not PredictPushButton.is_predict_available(main_window))
                     
            pixmap = QPixmap(main_window.imgdirname)
            if not pixmap.isNull():
                main_window.source_label.setPixmap(pixmap.scaled(mw.source_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

            else:
                main_window.source_label.setText("Invalid image file")
