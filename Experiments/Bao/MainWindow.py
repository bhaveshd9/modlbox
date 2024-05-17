from ui_mainwindow import Ui_MainWindow
from functions.header.top_right_buttons import TopRightButtons
from functions.body.left_menu.switch_page import SwitchPage
from functions.body.pages.setup_page import SetupPage

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QComboBox, QFileDialog
from PySide6.QtCore import Qt

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)        
        self.icon_left_side_menu.setHidden(True)
        self.detection_stage_selection_frame.setEnabled(False)
        self.detection_stage_selection_frame.setStyleSheet("""
            QFrame {
                color: rgba(255, 255, 255, 0.1);
            }
            QComboBox{
	            background-color: rgba(27, 29, 35, 0.1);
            }                                      
        """)        
        self.default_dataset_frame.setEnabled(False)
        self.default_dataset_frame.setStyleSheet("""
            QFrame {
                color: rgba(255, 255, 255, 0.1);
            }
            QComboBox{
	            background-color: rgba(27, 29, 35, 0.1);
            }                                      
        """)
        self.custom_dataset_frame.setEnabled(True)
        self.custom_dataset_frame.setStyleSheet("""
            QFrame {
                color: rgba(255, 255, 255, 0.1);
            }
            QPushButton {
                background-color: rgba(52, 59, 72, 0.1);
            }
            QLineEdit{
	            background-color: rgba(33, 37, 43, 0.1);
            }                                      
        """)
        
        #TOP RIGHT BUTTONS INTERACTION
        self.minimize_button.clicked.connect(lambda: TopRightButtons.minimize_window(self))
        self.maximize_button.clicked.connect(lambda: TopRightButtons.maximize_window(self))
        self.close_button.clicked.connect(lambda: TopRightButtons.close_window(self))        

        #LEFT MENU PAGE
        self.file_full_button.clicked.connect(lambda: SwitchPage.switch_to_filePage(self))
        self.file_icon_button.clicked.connect(lambda: SwitchPage.switch_to_filePage(self))
        self.setup_full_button.clicked.connect(lambda: SwitchPage.switch_to_setupPage(self))
        self.setup_icon_button.clicked.connect(lambda: SwitchPage.switch_to_setupPage(self))
        self.analyze_full_button.clicked.connect(lambda: SwitchPage.switch_to_analyzePage(self))
        self.analyze_icon_button.clicked.connect(lambda: SwitchPage.switch_to_analyzePage(self))
        self.about_full_button.clicked.connect(lambda: SwitchPage.switch_to_aboutPage(self))
        self.about_icon_button.clicked.connect(lambda: SwitchPage.switch_to_aboutPage(self))
        
        #SETUP PAGE
        self.open_file_button.clicked.connect(lambda: SetupPage.open_file(self))

        
