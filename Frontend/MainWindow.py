from PySide6.QtGui import QMouseEvent, QColor, QIcon
from ui_mainwindow import Ui_MainWindow
from ui_splash_screen import Ui_SplashScreen
from widgets import CircularProgress

from functions.pages.setup_page.init_setup_page import SetupPage
from functions.pages.graph_page.init_graph_page import GraphPage
from functions.pages.prediction_page.init_prediction_page import PredictionPage
from functions.pages.prediction_page.qcombobox.prediction_method_selection_comboBox import PredictionMethodQComboBox

from functions.tools.init_tools_box import Toolsbox

from functions.top_menu.switch_page import SwitchPage

from functions.previous_trains_list.update_previous_trains_list import PreviousTrainsList

from functions.tools.qpushbutton.hide_terminal_qpushbutton import HideTerminalPushButton

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QComboBox, QFileDialog, QSizeGrip, QGraphicsDropShadowEffect, QSplitter
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtWebEngineWidgets import QWebEngineView
import resources_rc

import os

widgets = None
counter = 0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # IMPORT CIRCULAR PROGRESS
        self.progress = CircularProgress()
        self.progress.width = 270
        self.progress.height = 270
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(15, 15)
        self.progress.font_size = 40
        self.progress.add_shadow(True)
        self.progress.progress_width = 5
        self.progress.bg_color = QColor(68, 71, 90, 140)
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()

        # ADD DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)

        # QTIMER 
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(35)

        self.show()

    # UPDATE PROGRESS BAR
    def update(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progress.set_value(counter)

        # CLOSE SPLASH SCREEN AND OPEN MAIN APP
        if counter >= 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MyMainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1
        
class MyMainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        

        # GET FOLDER LOCATION
        self.project_path =  os.getcwd()
        print("[MainWindow] Project Path: ", self.project_path)
        
        # SETUP RAW UI
        self.setupUi(self)     
        
        # DRAG WINDOW
        self.title_frame.mouseMoveEvent = self.moveWindow
        self.title_frame.mouseDoubleClickEvent = self.maximizeWindowForDoubleClick
                
        # INITIALIZE RESIZE GRIP
        self.sizegrip = QSizeGrip(self.size_grip_frame)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")
        
        # UPDATE PREVIOUS MODELS LIST
        PreviousTrainsList.update_previous_trains_list(self)
        
        # TOP RIGHT BUTTONS INTERACTION
        self.minimize_pushButton.clicked.connect(self.minimizeWindow)
        self.maximize_pushButton.clicked.connect(self.maximizeWindow)
        self.close_pushButton.clicked.connect(self.closeWindow)    
        
        # TOP MENU PAGE
        self.setup_page_pushButton.setChecked(True)
        self.setup_page_pushButton.clicked.connect(lambda: SwitchPage.switchToSetupPage(self))
        self.graph_page_pushButton.clicked.connect(lambda: SwitchPage.switchToGraphPage(self))
        self.prediction_page_pushButton.clicked.connect(lambda: SwitchPage.switchToPredictionPage(self))
        
        # PREVIOUS TRAINS LIST
        self.switch_previous_trains_list_pushButton.clicked.connect(lambda: PreviousTrainsList.switchToPreviousDetectionTrainsListPage(self))
        self.switch_previous_trains_list_pushButton_2.clicked.connect(lambda: PreviousTrainsList.switchPreviousClassificationTrainsListPage(self))
        
        
        # TOOLS
        Toolsbox.initToolsBox(self)
        
        # TERMINAL
        self.hide_terminal_pushButton.clicked.connect(lambda: HideTerminalPushButton.hide_terminal(self))
        
        # APPLY SPLITTER
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.page_list)
        splitter.addWidget(self.terminal_frame)
        self.pageFrameVerticalLayout.addWidget(splitter)
        
        # SETUP PAGE
        self.custom_dataset_frame.setHidden(True)
        self.detection_stage_frame.setHidden(True)
        SetupPage.initSetupPage(self)
        
        # GRAPH PAGE
        GraphPage.initGraphPage(self.webEngineView)
        self.webEngineView.setHidden(True)
        
        # PREDICT PAGE
        PredictionPage.initPredictionPage(self)
        PredictionMethodQComboBox.addMethodOptions(self)


    
    def moveWindow(self, event):
        if self.isMaximized()  == False:
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
                
    
    def maximizeWindowForDoubleClick(self, event):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        event.accept()
                
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    
    def minimizeWindow(self):
        self.showMinimized()

    def maximizeWindow(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        
    def closeWindow(self):
        self.close()
