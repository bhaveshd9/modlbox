# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1295, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.centralwidgetLayout = QVBoxLayout(self.centralwidget)
        self.centralwidgetLayout.setSpacing(0)
        self.centralwidgetLayout.setObjectName(u"centralwidgetLayout")
        self.centralwidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.mainHeaderHorizontalLayout = QHBoxLayout(self.main_header)
        self.mainHeaderHorizontalLayout.setSpacing(0)
        self.mainHeaderHorizontalLayout.setObjectName(u"mainHeaderHorizontalLayout")
        self.mainHeaderHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(self.main_header)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setStyleSheet(u"QFrame {\n"
"    font-family: Geneva;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"	font-size: 25px;\n"
"	border: 0;\n"
"}")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.titleHorizontalLayout = QHBoxLayout(self.title_frame)
        self.titleHorizontalLayout.setSpacing(10)
        self.titleHorizontalLayout.setObjectName(u"titleHorizontalLayout")
        self.titleHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo_pushbutton = QPushButton(self.title_frame)
        self.logo_pushbutton.setObjectName(u"logo_pushbutton")
        self.logo_pushbutton.setMinimumSize(QSize(25, 25))
        self.logo_pushbutton.setMaximumSize(QSize(40, 40))
        self.logo_pushbutton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/resources/modl-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_pushbutton.setIcon(icon)
        self.logo_pushbutton.setIconSize(QSize(40, 40))

        self.titleHorizontalLayout.addWidget(self.logo_pushbutton)

        self.window_title_label = QLabel(self.title_frame)
        self.window_title_label.setObjectName(u"window_title_label")
        self.window_title_label.setAutoFillBackground(False)
        self.window_title_label.setStyleSheet(u"")

        self.titleHorizontalLayout.addWidget(self.window_title_label)


        self.mainHeaderHorizontalLayout.addWidget(self.title_frame)

        self.top_right_buttons_frame = QFrame(self.main_header)
        self.top_right_buttons_frame.setObjectName(u"top_right_buttons_frame")
        self.top_right_buttons_frame.setMaximumSize(QSize(150, 16777215))
        self.top_right_buttons_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.top_right_buttons_frame.setStyleSheet(u"QFrame {\n"
"border: 0\n"
"}\n"
"QPushButton {\n"
"	border-radius: 5px;\n"
"	border: 0\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 133, 200);\n"
"}\n"
"")
        self.top_right_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.top_right_buttons_frame.setFrameShadow(QFrame.Raised)
        self.topRightButtonsHorizontalLayout = QHBoxLayout(self.top_right_buttons_frame)
        self.topRightButtonsHorizontalLayout.setSpacing(0)
        self.topRightButtonsHorizontalLayout.setObjectName(u"topRightButtonsHorizontalLayout")
        self.topRightButtonsHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minimize_pushButton = QPushButton(self.top_right_buttons_frame)
        self.minimize_pushButton.setObjectName(u"minimize_pushButton")
        self.minimize_pushButton.setMaximumSize(QSize(40, 40))
        self.minimize_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_pushButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/resources/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_pushButton.setIcon(icon1)
        self.minimize_pushButton.setIconSize(QSize(40, 40))

        self.topRightButtonsHorizontalLayout.addWidget(self.minimize_pushButton)

        self.maximize_pushButton = QPushButton(self.top_right_buttons_frame)
        self.maximize_pushButton.setObjectName(u"maximize_pushButton")
        self.maximize_pushButton.setMaximumSize(QSize(40, 40))
        self.maximize_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/resources/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_pushButton.setIcon(icon2)
        self.maximize_pushButton.setIconSize(QSize(40, 40))

        self.topRightButtonsHorizontalLayout.addWidget(self.maximize_pushButton)

        self.close_pushButton = QPushButton(self.top_right_buttons_frame)
        self.close_pushButton.setObjectName(u"close_pushButton")
        self.close_pushButton.setMaximumSize(QSize(40, 40))
        self.close_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_pushButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(255, 140, 140);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/resources/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_pushButton.setIcon(icon3)
        self.close_pushButton.setIconSize(QSize(40, 40))

        self.topRightButtonsHorizontalLayout.addWidget(self.close_pushButton)


        self.mainHeaderHorizontalLayout.addWidget(self.top_right_buttons_frame, 0, Qt.AlignVCenter)


        self.centralwidgetLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: \"Segoe UI\";\n"
"font-size: 12px;")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.mainBodyHorizontalLayout = QHBoxLayout(self.main_body)
        self.mainBodyHorizontalLayout.setSpacing(50)
        self.mainBodyHorizontalLayout.setObjectName(u"mainBodyHorizontalLayout")
        self.mainBodyHorizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.tools_frame = QFrame(self.main_body)
        self.tools_frame.setObjectName(u"tools_frame")
        self.tools_frame.setMinimumSize(QSize(190, 0))
        self.tools_frame.setMaximumSize(QSize(16777215, 16777215))
        self.tools_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(33, 37, 43);\n"
"	color: white;\n"
"	border: 0\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-left: 8px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	color: white;\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 8px solid rgb(57, 65, 80);\n"
"	background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 8px solid rgb(0, 133, 200);\n"
"	background-color: rgb(0, 133, 200);\n"
"}")
        self.tools_frame.setFrameShape(QFrame.StyledPanel)
        self.tools_frame.setFrameShadow(QFrame.Raised)
        self.toolsFrameVerticalLayout = QVBoxLayout(self.tools_frame)
        self.toolsFrameVerticalLayout.setSpacing(15)
        self.toolsFrameVerticalLayout.setObjectName(u"toolsFrameVerticalLayout")
        self.toolsFrameVerticalLayout.setContentsMargins(0, 10, 0, 0)
        self.line_5 = QFrame(self.tools_frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(16777215, 16777215))
        self.line_5.setFrameShadow(QFrame.Raised)
        self.line_5.setLineWidth(1)
        self.line_5.setFrameShape(QFrame.HLine)

        self.toolsFrameVerticalLayout.addWidget(self.line_5)

        self.setup_buttons_frame = QFrame(self.tools_frame)
        self.setup_buttons_frame.setObjectName(u"setup_buttons_frame")
        self.setup_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.setup_buttons_frame.setFrameShadow(QFrame.Raised)
        self.setupButtonsFrameVerticalLayout = QVBoxLayout(self.setup_buttons_frame)
        self.setupButtonsFrameVerticalLayout.setSpacing(10)
        self.setupButtonsFrameVerticalLayout.setObjectName(u"setupButtonsFrameVerticalLayout")
        self.setupButtonsFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.setup_buttons_label = QLabel(self.setup_buttons_frame)
        self.setup_buttons_label.setObjectName(u"setup_buttons_label")

        self.setupButtonsFrameVerticalLayout.addWidget(self.setup_buttons_label)

        self.reset_pushButton = QPushButton(self.setup_buttons_frame)
        self.reset_pushButton.setObjectName(u"reset_pushButton")
        self.reset_pushButton.setMaximumSize(QSize(190, 16777215))
        self.reset_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/reset.png);")

        self.setupButtonsFrameVerticalLayout.addWidget(self.reset_pushButton)


        self.toolsFrameVerticalLayout.addWidget(self.setup_buttons_frame)

        self.line = QFrame(self.tools_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.toolsFrameVerticalLayout.addWidget(self.line)

        self.model_buttons_frame = QFrame(self.tools_frame)
        self.model_buttons_frame.setObjectName(u"model_buttons_frame")
        self.model_buttons_frame.setStyleSheet(u"")
        self.model_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.model_buttons_frame.setFrameShadow(QFrame.Raised)
        self.modelButtonsFrameVerticalLayout = QVBoxLayout(self.model_buttons_frame)
        self.modelButtonsFrameVerticalLayout.setSpacing(10)
        self.modelButtonsFrameVerticalLayout.setObjectName(u"modelButtonsFrameVerticalLayout")
        self.modelButtonsFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.model_buttons_label = QLabel(self.model_buttons_frame)
        self.model_buttons_label.setObjectName(u"model_buttons_label")

        self.modelButtonsFrameVerticalLayout.addWidget(self.model_buttons_label)

        self.start_pushButton = QPushButton(self.model_buttons_frame)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setMaximumSize(QSize(190, 16777215))
        self.start_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/start.png);")

        self.modelButtonsFrameVerticalLayout.addWidget(self.start_pushButton)

        self.stop_pushButton = QPushButton(self.model_buttons_frame)
        self.stop_pushButton.setObjectName(u"stop_pushButton")
        self.stop_pushButton.setMaximumSize(QSize(190, 16777215))
        self.stop_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/stop.png);")

        self.modelButtonsFrameVerticalLayout.addWidget(self.stop_pushButton)

        self.predict_pushButton = QPushButton(self.model_buttons_frame)
        self.predict_pushButton.setObjectName(u"predict_pushButton")
        self.predict_pushButton.setMaximumSize(QSize(190, 16777215))
        self.predict_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.predict_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/predict.png);")

        self.modelButtonsFrameVerticalLayout.addWidget(self.predict_pushButton)

        self.save_detection_pushButton = QPushButton(self.model_buttons_frame)
        self.save_detection_pushButton.setObjectName(u"save_detection_pushButton")
        self.save_detection_pushButton.setMaximumSize(QSize(190, 16777215))
        self.save_detection_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_detection_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/save.png);")

        self.modelButtonsFrameVerticalLayout.addWidget(self.save_detection_pushButton)

        self.save_classification_pushButton = QPushButton(self.model_buttons_frame)
        self.save_classification_pushButton.setObjectName(u"save_classification_pushButton")
        self.save_classification_pushButton.setMaximumSize(QSize(190, 16777215))
        self.save_classification_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_classification_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/save.png);")

        self.modelButtonsFrameVerticalLayout.addWidget(self.save_classification_pushButton)

        self.delete_detection_pushButton = QPushButton(self.model_buttons_frame)
        self.delete_detection_pushButton.setObjectName(u"delete_detection_pushButton")
        self.delete_detection_pushButton.setMaximumSize(QSize(190, 16777215))
        self.delete_detection_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_detection_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/delete.png);")

        self.modelButtonsFrameVerticalLayout.addWidget(self.delete_detection_pushButton)

        self.delete_classification_pushButton = QPushButton(self.model_buttons_frame)
        self.delete_classification_pushButton.setObjectName(u"delete_classification_pushButton")
        self.delete_classification_pushButton.setMaximumSize(QSize(190, 16777215))
        self.delete_classification_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_classification_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/delete.png);")

        self.modelButtonsFrameVerticalLayout.addWidget(self.delete_classification_pushButton)


        self.toolsFrameVerticalLayout.addWidget(self.model_buttons_frame)

        self.line_3 = QFrame(self.tools_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Raised)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.toolsFrameVerticalLayout.addWidget(self.line_3)

        self.terminal_buttons_frame = QFrame(self.tools_frame)
        self.terminal_buttons_frame.setObjectName(u"terminal_buttons_frame")
        self.terminal_buttons_frame.setStyleSheet(u"")
        self.terminal_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.terminal_buttons_frame.setFrameShadow(QFrame.Raised)
        self.terminalButtonsVerticalLayout = QVBoxLayout(self.terminal_buttons_frame)
        self.terminalButtonsVerticalLayout.setSpacing(10)
        self.terminalButtonsVerticalLayout.setObjectName(u"terminalButtonsVerticalLayout")
        self.terminalButtonsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.terminal_buttons_label = QLabel(self.terminal_buttons_frame)
        self.terminal_buttons_label.setObjectName(u"terminal_buttons_label")

        self.terminalButtonsVerticalLayout.addWidget(self.terminal_buttons_label)

        self.show_terminal_pushButton = QPushButton(self.terminal_buttons_frame)
        self.show_terminal_pushButton.setObjectName(u"show_terminal_pushButton")
        self.show_terminal_pushButton.setMaximumSize(QSize(190, 16777215))
        self.show_terminal_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_terminal_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/show-hide-terminal.png);")

        self.terminalButtonsVerticalLayout.addWidget(self.show_terminal_pushButton)

        self.hide_terminal_pushButton_2 = QPushButton(self.terminal_buttons_frame)
        self.hide_terminal_pushButton_2.setObjectName(u"hide_terminal_pushButton_2")
        self.hide_terminal_pushButton_2.setMaximumSize(QSize(190, 16777215))
        self.hide_terminal_pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.hide_terminal_pushButton_2.setStyleSheet(u"background-image: url(:/newPrefix/resources/show-hide-terminal.png);")

        self.terminalButtonsVerticalLayout.addWidget(self.hide_terminal_pushButton_2)

        self.clear_terminal_pushButton = QPushButton(self.terminal_buttons_frame)
        self.clear_terminal_pushButton.setObjectName(u"clear_terminal_pushButton")
        self.clear_terminal_pushButton.setMaximumSize(QSize(190, 16777215))
        self.clear_terminal_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_terminal_pushButton.setStyleSheet(u"background-image: url(:/newPrefix/resources/clear.png);")

        self.terminalButtonsVerticalLayout.addWidget(self.clear_terminal_pushButton)


        self.toolsFrameVerticalLayout.addWidget(self.terminal_buttons_frame)

        self.line_4 = QFrame(self.tools_frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Raised)
        self.line_4.setLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)

        self.toolsFrameVerticalLayout.addWidget(self.line_4)

        self.tools_frame_verticalSpacer = QSpacerItem(20, 468, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.toolsFrameVerticalLayout.addItem(self.tools_frame_verticalSpacer)


        self.mainBodyHorizontalLayout.addWidget(self.tools_frame)

        self.out_of_name_frame = QFrame(self.main_body)
        self.out_of_name_frame.setObjectName(u"out_of_name_frame")
        self.out_of_name_frame.setStyleSheet(u"")
        self.out_of_name_frame.setFrameShape(QFrame.StyledPanel)
        self.out_of_name_frame.setFrameShadow(QFrame.Raised)
        self.outOfNameVerticalLayout = QVBoxLayout(self.out_of_name_frame)
        self.outOfNameVerticalLayout.setSpacing(0)
        self.outOfNameVerticalLayout.setObjectName(u"outOfNameVerticalLayout")
        self.outOfNameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_side_menu = QFrame(self.out_of_name_frame)
        self.top_side_menu.setObjectName(u"top_side_menu")
        self.top_side_menu.setMaximumSize(QSize(16777215, 16777215))
        self.top_side_menu.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 0\n"
"}\n"
"\n"
"QPushButton {\n"
"	width: 150px;\n"
"	border: none;\n"
"	border-bottom: 4px solid rgba(0, 0, 0, 0);\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	background-color: transparent;\n"
"	color: rgb(170, 170, 170);\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 133, 200);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	border-bottom: 4px solid qlineargradient(spread:pad, x1:0.454545, y1:1, x2:0.454, y2:0.664773, stop:0.948864 rgba(0, 171, 255, 255), stop:1 rgb(33, 37, 43));\n"
"	background-color: rgb(33, 37, 43);\n"
"	color: rgb(255, 255, 255);	\n"
"}")
        self.top_side_menu.setFrameShape(QFrame.StyledPanel)
        self.top_side_menu.setFrameShadow(QFrame.Raised)
        self.TpideMenuHorizontalLayout = QHBoxLayout(self.top_side_menu)
        self.TpideMenuHorizontalLayout.setSpacing(0)
        self.TpideMenuHorizontalLayout.setObjectName(u"TpideMenuHorizontalLayout")
        self.TpideMenuHorizontalLayout.setContentsMargins(0, 20, 0, 0)
        self.setup_page_pushButton = QPushButton(self.top_side_menu)
        self.setup_page_pushButton.setObjectName(u"setup_page_pushButton")
        self.setup_page_pushButton.setMaximumSize(QSize(120, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.setup_page_pushButton.setFont(font)
        self.setup_page_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.setup_page_pushButton.setIconSize(QSize(16, 16))
        self.setup_page_pushButton.setCheckable(True)
        self.setup_page_pushButton.setAutoExclusive(True)

        self.TpideMenuHorizontalLayout.addWidget(self.setup_page_pushButton)

        self.graph_page_pushButton = QPushButton(self.top_side_menu)
        self.graph_page_pushButton.setObjectName(u"graph_page_pushButton")
        self.graph_page_pushButton.setMaximumSize(QSize(120, 50))
        self.graph_page_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.graph_page_pushButton.setIconSize(QSize(30, 30))
        self.graph_page_pushButton.setCheckable(True)
        self.graph_page_pushButton.setAutoExclusive(True)

        self.TpideMenuHorizontalLayout.addWidget(self.graph_page_pushButton)

        self.prediction_page_pushButton = QPushButton(self.top_side_menu)
        self.prediction_page_pushButton.setObjectName(u"prediction_page_pushButton")
        self.prediction_page_pushButton.setMaximumSize(QSize(120, 50))
        self.prediction_page_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.prediction_page_pushButton.setIconSize(QSize(25, 30))
        self.prediction_page_pushButton.setCheckable(True)
        self.prediction_page_pushButton.setAutoExclusive(True)

        self.TpideMenuHorizontalLayout.addWidget(self.prediction_page_pushButton)

        self.top_menu_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TpideMenuHorizontalLayout.addItem(self.top_menu_horizontalSpacer)


        self.outOfNameVerticalLayout.addWidget(self.top_side_menu)

        self.content = QFrame(self.out_of_name_frame)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(16777215, 16777215))
        self.content.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 0\n"
"\n"
"}\n"
"\n"
"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(40, 44, 52);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(0, 133, 200);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"	height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"	height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar"
                        "::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(40, 44, 52);\n"
"    height: 8px;\n"
"    margin: 0 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {    \n"
"    background: rgb(0, 133, 200);\n"
"    min-width: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin:"
                        " margin;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QComboBox:drop-down {\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
" }\n"
"\n"
"QComboBox::drop-down {\n"
"	background-image: url(:/newPrefix/resources/arrow-down.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72)"
                        ";\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border: 2px solid rgb(0, 133, 200);\n"
"	background-color: rgb(0, 133, 200);\n"
"}\n"
"\n"
"QSpinBox {\n"
"	border: 2px solid rgb(46, 44, 45);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QSpinBox::down-arrow, QSpinBox::up-arrow {\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	background: transparent;\n"
"	subcontrol-origin: content;\n"
"	subcontrol-position: left center;\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"	image: url(:/newPrefix/resources/arrow-left.png);\n"
"}\n"
"\n"
"QSpinBox::up-arrow{\n"
"	image: url(:/newPrefix/resources/arrow-right.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow:hover {\n"
"	image: url(:/newPrefix/resources/arrow-left-hover.png);\n"
"}\n"
"\n"
"Q"
                        "SpinBox::up-arrow:hover {\n"
"	image: url(:/newPrefix/resources/arrow-right-hover.png);\n"
"}\n"
"\n"
"QSpinBox::down-arrow:pressed {\n"
"	image: url(:/newPrefix/resources/arrow-left-pressed.png);\n"
"}\n"
"\n"
"QSpinBox::up-arrow:pressed {\n"
"	image: url(:/newPrefix/resources/arrow-right-pressed.png);\n"
"}\n"
"\n"
"QSpinBox::down-button, QSpinBox::up-button {\n"
"	width: 14px;\n"
"	height: 12px;\n"
"	background: transparent;\n"
"	border: none;\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: center right;\n"
"}\n"
"\n"
"QSpinBox::down-button{\n"
"	margin: 0 0 0 12px;\n"
"	padding: 0 14px 0 -12px;\n"
"}")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.contentHorizontalLayout = QHBoxLayout(self.content)
        self.contentHorizontalLayout.setSpacing(30)
        self.contentHorizontalLayout.setObjectName(u"contentHorizontalLayout")
        self.contentHorizontalLayout.setContentsMargins(0, 20, 0, 0)
        self.pages_frame = QFrame(self.content)
        self.pages_frame.setObjectName(u"pages_frame")
        self.pages_frame.setStyleSheet(u"")
        self.pages_frame.setFrameShape(QFrame.StyledPanel)
        self.pages_frame.setFrameShadow(QFrame.Raised)
        self.pageFrameVerticalLayout = QVBoxLayout(self.pages_frame)
        self.pageFrameVerticalLayout.setSpacing(5)
        self.pageFrameVerticalLayout.setObjectName(u"pageFrameVerticalLayout")
        self.pageFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.page_list = QStackedWidget(self.pages_frame)
        self.page_list.setObjectName(u"page_list")
        self.page_list.setMinimumSize(QSize(0, 50))
        self.page_list.setStyleSheet(u"")
        self.setup_page = QWidget()
        self.setup_page.setObjectName(u"setup_page")
        self.setup_page.setEnabled(True)
        self.setup_page.setStyleSheet(u"")
        self.setupPageVerticalLayout = QVBoxLayout(self.setup_page)
        self.setupPageVerticalLayout.setSpacing(15)
        self.setupPageVerticalLayout.setObjectName(u"setupPageVerticalLayout")
        self.setupPageVerticalLayout.setContentsMargins(10, 10, 10, 10)
        self.new_setup_label = QLabel(self.setup_page)
        self.new_setup_label.setObjectName(u"new_setup_label")
        self.new_setup_label.setMinimumSize(QSize(0, 20))
        self.new_setup_label.setMaximumSize(QSize(16777215, 16777215))
        self.new_setup_label.setStyleSheet(u"font-size: 15px;")

        self.setupPageVerticalLayout.addWidget(self.new_setup_label)

        self.setup_options_list = QScrollArea(self.setup_page)
        self.setup_options_list.setObjectName(u"setup_options_list")
        self.setup_options_list.setWidgetResizable(True)
        self.setup_content = QWidget()
        self.setup_content.setObjectName(u"setup_content")
        self.setup_content.setGeometry(QRect(0, 0, 743, 454))
        self.setupContentVerticalLayout = QVBoxLayout(self.setup_content)
        self.setupContentVerticalLayout.setSpacing(25)
        self.setupContentVerticalLayout.setObjectName(u"setupContentVerticalLayout")
        self.setupContentVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.method_frame = QFrame(self.setup_content)
        self.method_frame.setObjectName(u"method_frame")
        self.method_frame.setMaximumSize(QSize(16777215, 80))
        self.method_frame.setStyleSheet(u"")
        self.method_frame.setFrameShape(QFrame.StyledPanel)
        self.method_frame.setFrameShadow(QFrame.Raised)
        self.methodFrameVerticalLayout = QVBoxLayout(self.method_frame)
        self.methodFrameVerticalLayout.setSpacing(10)
        self.methodFrameVerticalLayout.setObjectName(u"methodFrameVerticalLayout")
        self.methodFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.method_label = QLabel(self.method_frame)
        self.method_label.setObjectName(u"method_label")

        self.methodFrameVerticalLayout.addWidget(self.method_label)

        self.method_comboBox = QComboBox(self.method_frame)
        self.method_comboBox.setObjectName(u"method_comboBox")
        self.method_comboBox.setMaximumSize(QSize(500, 16777215))
        self.method_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.methodFrameVerticalLayout.addWidget(self.method_comboBox)


        self.setupContentVerticalLayout.addWidget(self.method_frame)

        self.specifications_frame = QFrame(self.setup_content)
        self.specifications_frame.setObjectName(u"specifications_frame")
        self.specifications_frame.setMaximumSize(QSize(16777215, 100))
        self.specifications_frame.setStyleSheet(u"")
        self.specifications_frame.setFrameShape(QFrame.StyledPanel)
        self.specifications_frame.setFrameShadow(QFrame.Raised)
        self.specifications_frame.setLineWidth(0)
        self.specificationsFrameVerticalLayout = QVBoxLayout(self.specifications_frame)
        self.specificationsFrameVerticalLayout.setSpacing(10)
        self.specificationsFrameVerticalLayout.setObjectName(u"specificationsFrameVerticalLayout")
        self.specificationsFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.specification_label = QLabel(self.specifications_frame)
        self.specification_label.setObjectName(u"specification_label")

        self.specificationsFrameVerticalLayout.addWidget(self.specification_label)

        self.specification_options_frame = QFrame(self.specifications_frame)
        self.specification_options_frame.setObjectName(u"specification_options_frame")
        self.specification_options_frame.setMaximumSize(QSize(16777215, 75))
        self.specification_options_frame.setFrameShape(QFrame.StyledPanel)
        self.specification_options_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.specification_options_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.epochs_frame = QFrame(self.specification_options_frame)
        self.epochs_frame.setObjectName(u"epochs_frame")
        self.epochs_frame.setMaximumSize(QSize(16777215, 16777215))
        self.epochs_frame.setFrameShape(QFrame.StyledPanel)
        self.epochs_frame.setFrameShadow(QFrame.Raised)
        self.epochsFrameVerticalLayout = QVBoxLayout(self.epochs_frame)
        self.epochsFrameVerticalLayout.setSpacing(10)
        self.epochsFrameVerticalLayout.setObjectName(u"epochsFrameVerticalLayout")
        self.epochsFrameVerticalLayout.setContentsMargins(0, 0, 20, 0)
        self.epochs_label = QLabel(self.epochs_frame)
        self.epochs_label.setObjectName(u"epochs_label")
        self.epochs_label.setTextFormat(Qt.AutoText)
        self.epochs_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.epochsFrameVerticalLayout.addWidget(self.epochs_label)

        self.epochs_spinBox = QSpinBox(self.epochs_frame)
        self.epochs_spinBox.setObjectName(u"epochs_spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.epochs_spinBox.sizePolicy().hasHeightForWidth())
        self.epochs_spinBox.setSizePolicy(sizePolicy)
        self.epochs_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.epochs_spinBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.epochs_spinBox.setMinimum(1)
        self.epochs_spinBox.setMaximum(10000)
        self.epochs_spinBox.setValue(10)

        self.epochsFrameVerticalLayout.addWidget(self.epochs_spinBox)


        self.gridLayout.addWidget(self.epochs_frame, 0, 2, 1, 1)

        self.gpu_frame = QFrame(self.specification_options_frame)
        self.gpu_frame.setObjectName(u"gpu_frame")
        self.gpu_frame.setMaximumSize(QSize(16777215, 16777215))
        self.gpu_frame.setFrameShape(QFrame.StyledPanel)
        self.gpu_frame.setFrameShadow(QFrame.Raised)
        self.gpuFrameVerticalLayout = QVBoxLayout(self.gpu_frame)
        self.gpuFrameVerticalLayout.setSpacing(10)
        self.gpuFrameVerticalLayout.setObjectName(u"gpuFrameVerticalLayout")
        self.gpuFrameVerticalLayout.setContentsMargins(0, 0, 20, 0)
        self.gpu_label = QLabel(self.gpu_frame)
        self.gpu_label.setObjectName(u"gpu_label")
        self.gpu_label.setTextFormat(Qt.AutoText)
        self.gpu_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gpuFrameVerticalLayout.addWidget(self.gpu_label)

        self.gpu_comboBox = QComboBox(self.gpu_frame)
        self.gpu_comboBox.setObjectName(u"gpu_comboBox")
        self.gpu_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.gpu_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.gpuFrameVerticalLayout.addWidget(self.gpu_comboBox)


        self.gridLayout.addWidget(self.gpu_frame, 0, 1, 1, 1)

        self.batch_size_frame = QFrame(self.specification_options_frame)
        self.batch_size_frame.setObjectName(u"batch_size_frame")
        self.batch_size_frame.setMaximumSize(QSize(16777215, 16777215))
        self.batch_size_frame.setFrameShape(QFrame.StyledPanel)
        self.batch_size_frame.setFrameShadow(QFrame.Raised)
        self.batchSizeFrameVerticalLayout = QVBoxLayout(self.batch_size_frame)
        self.batchSizeFrameVerticalLayout.setSpacing(10)
        self.batchSizeFrameVerticalLayout.setObjectName(u"batchSizeFrameVerticalLayout")
        self.batchSizeFrameVerticalLayout.setContentsMargins(0, 0, 20, 0)
        self.batch_size_label = QLabel(self.batch_size_frame)
        self.batch_size_label.setObjectName(u"batch_size_label")
        self.batch_size_label.setTextFormat(Qt.AutoText)
        self.batch_size_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.batchSizeFrameVerticalLayout.addWidget(self.batch_size_label)

        self.batch_size_spinBox = QSpinBox(self.batch_size_frame)
        self.batch_size_spinBox.setObjectName(u"batch_size_spinBox")
        self.batch_size_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.batch_size_spinBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.batch_size_spinBox.setMinimum(1)
        self.batch_size_spinBox.setMaximum(100)

        self.batchSizeFrameVerticalLayout.addWidget(self.batch_size_spinBox)


        self.gridLayout.addWidget(self.batch_size_frame, 0, 3, 1, 1)

        self.detection_stage_frame = QFrame(self.specification_options_frame)
        self.detection_stage_frame.setObjectName(u"detection_stage_frame")
        self.detection_stage_frame.setMaximumSize(QSize(16777215, 16777215))
        self.detection_stage_frame.setFrameShape(QFrame.StyledPanel)
        self.detection_stage_frame.setFrameShadow(QFrame.Raised)
        self.detectionStageFrameVerticalLayout = QVBoxLayout(self.detection_stage_frame)
        self.detectionStageFrameVerticalLayout.setSpacing(10)
        self.detectionStageFrameVerticalLayout.setObjectName(u"detectionStageFrameVerticalLayout")
        self.detectionStageFrameVerticalLayout.setContentsMargins(0, 0, 20, 0)
        self.detection_stage_label = QLabel(self.detection_stage_frame)
        self.detection_stage_label.setObjectName(u"detection_stage_label")
        self.detection_stage_label.setTextFormat(Qt.AutoText)
        self.detection_stage_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.detectionStageFrameVerticalLayout.addWidget(self.detection_stage_label)

        self.detection_stage_comboBox = QComboBox(self.detection_stage_frame)
        self.detection_stage_comboBox.setObjectName(u"detection_stage_comboBox")
        self.detection_stage_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.detection_stage_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.detectionStageFrameVerticalLayout.addWidget(self.detection_stage_comboBox)


        self.gridLayout.addWidget(self.detection_stage_frame, 0, 0, 1, 1)


        self.specificationsFrameVerticalLayout.addWidget(self.specification_options_frame)


        self.setupContentVerticalLayout.addWidget(self.specifications_frame)

        self.model_frame = QFrame(self.setup_content)
        self.model_frame.setObjectName(u"model_frame")
        self.model_frame.setMaximumSize(QSize(16777215, 80))
        self.model_frame.setStyleSheet(u"")
        self.model_frame.setFrameShape(QFrame.StyledPanel)
        self.model_frame.setFrameShadow(QFrame.Raised)
        self.modelFrameVerticalLayout = QVBoxLayout(self.model_frame)
        self.modelFrameVerticalLayout.setSpacing(10)
        self.modelFrameVerticalLayout.setObjectName(u"modelFrameVerticalLayout")
        self.modelFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.model_label = QLabel(self.model_frame)
        self.model_label.setObjectName(u"model_label")

        self.modelFrameVerticalLayout.addWidget(self.model_label)

        self.model_comboBox = QComboBox(self.model_frame)
        self.model_comboBox.setObjectName(u"model_comboBox")
        self.model_comboBox.setMaximumSize(QSize(500, 16777215))
        self.model_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.modelFrameVerticalLayout.addWidget(self.model_comboBox)


        self.setupContentVerticalLayout.addWidget(self.model_frame)

        self.dataset_frame = QFrame(self.setup_content)
        self.dataset_frame.setObjectName(u"dataset_frame")
        self.dataset_frame.setMaximumSize(QSize(16777215, 160))
        self.dataset_frame.setStyleSheet(u"")
        self.dataset_frame.setFrameShape(QFrame.StyledPanel)
        self.dataset_frame.setFrameShadow(QFrame.Raised)
        self.datasetFrameVerticalLayout = QVBoxLayout(self.dataset_frame)
        self.datasetFrameVerticalLayout.setSpacing(10)
        self.datasetFrameVerticalLayout.setObjectName(u"datasetFrameVerticalLayout")
        self.datasetFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dataset_selection_frame = QFrame(self.dataset_frame)
        self.dataset_selection_frame.setObjectName(u"dataset_selection_frame")
        self.dataset_selection_frame.setMaximumSize(QSize(16777215, 75))
        self.dataset_selection_frame.setFrameShape(QFrame.StyledPanel)
        self.dataset_selection_frame.setFrameShadow(QFrame.Raised)
        self.datasetSelectionFrameVerticalLayout = QVBoxLayout(self.dataset_selection_frame)
        self.datasetSelectionFrameVerticalLayout.setSpacing(10)
        self.datasetSelectionFrameVerticalLayout.setObjectName(u"datasetSelectionFrameVerticalLayout")
        self.datasetSelectionFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dataset_label = QLabel(self.dataset_selection_frame)
        self.dataset_label.setObjectName(u"dataset_label")

        self.datasetSelectionFrameVerticalLayout.addWidget(self.dataset_label)

        self.dataset_comboBox = QComboBox(self.dataset_selection_frame)
        self.dataset_comboBox.setObjectName(u"dataset_comboBox")
        self.dataset_comboBox.setMaximumSize(QSize(500, 16777215))
        self.dataset_comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.dataset_comboBox.setMaxCount(2147483646)

        self.datasetSelectionFrameVerticalLayout.addWidget(self.dataset_comboBox)


        self.datasetFrameVerticalLayout.addWidget(self.dataset_selection_frame)

        self.default_dataset_frame = QFrame(self.dataset_frame)
        self.default_dataset_frame.setObjectName(u"default_dataset_frame")
        self.default_dataset_frame.setMaximumSize(QSize(16777215, 75))
        self.default_dataset_frame.setFrameShape(QFrame.StyledPanel)
        self.default_dataset_frame.setFrameShadow(QFrame.Raised)
        self.defaultDatasetFrameVerticalLayout = QVBoxLayout(self.default_dataset_frame)
        self.defaultDatasetFrameVerticalLayout.setSpacing(10)
        self.defaultDatasetFrameVerticalLayout.setObjectName(u"defaultDatasetFrameVerticalLayout")
        self.defaultDatasetFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.default_dataset_label = QLabel(self.default_dataset_frame)
        self.default_dataset_label.setObjectName(u"default_dataset_label")

        self.defaultDatasetFrameVerticalLayout.addWidget(self.default_dataset_label)

        self.default_dataset_comboBox = QComboBox(self.default_dataset_frame)
        self.default_dataset_comboBox.setObjectName(u"default_dataset_comboBox")
        self.default_dataset_comboBox.setMaximumSize(QSize(500, 16777215))
        self.default_dataset_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.defaultDatasetFrameVerticalLayout.addWidget(self.default_dataset_comboBox)


        self.datasetFrameVerticalLayout.addWidget(self.default_dataset_frame)

        self.custom_dataset_frame = QFrame(self.dataset_frame)
        self.custom_dataset_frame.setObjectName(u"custom_dataset_frame")
        self.custom_dataset_frame.setMaximumSize(QSize(16777215, 75))
        self.custom_dataset_frame.setFrameShape(QFrame.StyledPanel)
        self.custom_dataset_frame.setFrameShadow(QFrame.Raised)
        self.customDatasetFrameVerticalLayout = QVBoxLayout(self.custom_dataset_frame)
        self.customDatasetFrameVerticalLayout.setSpacing(10)
        self.customDatasetFrameVerticalLayout.setObjectName(u"customDatasetFrameVerticalLayout")
        self.customDatasetFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.custom_dataset_label = QLabel(self.custom_dataset_frame)
        self.custom_dataset_label.setObjectName(u"custom_dataset_label")

        self.customDatasetFrameVerticalLayout.addWidget(self.custom_dataset_label)

        self.file_path_frame = QFrame(self.custom_dataset_frame)
        self.file_path_frame.setObjectName(u"file_path_frame")
        self.file_path_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"}")
        self.file_path_frame.setFrameShape(QFrame.StyledPanel)
        self.file_path_frame.setFrameShadow(QFrame.Raised)
        self.filePathFrameHorizontalLayout = QHBoxLayout(self.file_path_frame)
        self.filePathFrameHorizontalLayout.setSpacing(0)
        self.filePathFrameHorizontalLayout.setObjectName(u"filePathFrameHorizontalLayout")
        self.filePathFrameHorizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.file_path_label = QLabel(self.file_path_frame)
        self.file_path_label.setObjectName(u"file_path_label")
        self.file_path_label.setMaximumSize(QSize(16777215, 16777215))

        self.filePathFrameHorizontalLayout.addWidget(self.file_path_label)

        self.open_file_pushButton = QPushButton(self.file_path_frame)
        self.open_file_pushButton.setObjectName(u"open_file_pushButton")
        self.open_file_pushButton.setMaximumSize(QSize(150, 35))
        self.open_file_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_file_pushButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/resources/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_file_pushButton.setIcon(icon4)
        self.open_file_pushButton.setIconSize(QSize(20, 20))

        self.filePathFrameHorizontalLayout.addWidget(self.open_file_pushButton)


        self.customDatasetFrameVerticalLayout.addWidget(self.file_path_frame)


        self.datasetFrameVerticalLayout.addWidget(self.custom_dataset_frame)


        self.setupContentVerticalLayout.addWidget(self.dataset_frame)

        self.setup_verticalSpacer = QSpacerItem(58, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.setupContentVerticalLayout.addItem(self.setup_verticalSpacer)

        self.setup_options_list.setWidget(self.setup_content)

        self.setupPageVerticalLayout.addWidget(self.setup_options_list)

        self.page_list.addWidget(self.setup_page)
        self.graph_page = QWidget()
        self.graph_page.setObjectName(u"graph_page")
        self.graphPageVerticalLayout = QVBoxLayout(self.graph_page)
        self.graphPageVerticalLayout.setSpacing(10)
        self.graphPageVerticalLayout.setObjectName(u"graphPageVerticalLayout")
        self.graphPageVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.webEngineView = QWebEngineView(self.graph_page)
        self.webEngineView.setObjectName(u"webEngineView")

        self.graphPageVerticalLayout.addWidget(self.webEngineView)

        self.page_list.addWidget(self.graph_page)
        self.prediction_page = QWidget()
        self.prediction_page.setObjectName(u"prediction_page")
        self.prediction_page.setStyleSheet(u"")
        self.predictionPageVerticalLayout = QVBoxLayout(self.prediction_page)
        self.predictionPageVerticalLayout.setSpacing(0)
        self.predictionPageVerticalLayout.setObjectName(u"predictionPageVerticalLayout")
        self.predictionPageVerticalLayout.setContentsMargins(10, 10, 10, 10)
        self.prediction_pages_scrollArea = QScrollArea(self.prediction_page)
        self.prediction_pages_scrollArea.setObjectName(u"prediction_pages_scrollArea")
        self.prediction_pages_scrollArea.setWidgetResizable(True)
        self.prediction_pages_contents = QWidget()
        self.prediction_pages_contents.setObjectName(u"prediction_pages_contents")
        self.prediction_pages_contents.setGeometry(QRect(0, 0, 117, 28))
        self.predictionPagesContentsVerticalLayout = QVBoxLayout(self.prediction_pages_contents)
        self.predictionPagesContentsVerticalLayout.setSpacing(0)
        self.predictionPagesContentsVerticalLayout.setObjectName(u"predictionPagesContentsVerticalLayout")
        self.predictionPagesContentsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.prediction_image_frame = QFrame(self.prediction_pages_contents)
        self.prediction_image_frame.setObjectName(u"prediction_image_frame")
        self.prediction_image_frame.setFrameShape(QFrame.StyledPanel)
        self.prediction_image_frame.setFrameShadow(QFrame.Raised)
        self.predictionImageFrameHorizontalLayout = QHBoxLayout(self.prediction_image_frame)
        self.predictionImageFrameHorizontalLayout.setSpacing(5)
        self.predictionImageFrameHorizontalLayout.setObjectName(u"predictionImageFrameHorizontalLayout")
        self.predictionImageFrameHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.source_label_frame = QFrame(self.prediction_image_frame)
        self.source_label_frame.setObjectName(u"source_label_frame")
        self.source_label_frame.setMinimumSize(QSize(0, 0))
        self.source_label_frame.setFrameShape(QFrame.StyledPanel)
        self.source_label_frame.setFrameShadow(QFrame.Raised)
        self.sourceLabelFrameVerticalLayout = QVBoxLayout(self.source_label_frame)
        self.sourceLabelFrameVerticalLayout.setSpacing(0)
        self.sourceLabelFrameVerticalLayout.setObjectName(u"sourceLabelFrameVerticalLayout")
        self.sourceLabelFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.original_title_label = QLabel(self.source_label_frame)
        self.original_title_label.setObjectName(u"original_title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.original_title_label.sizePolicy().hasHeightForWidth())
        self.original_title_label.setSizePolicy(sizePolicy1)
        self.original_title_label.setMaximumSize(QSize(16777215, 20))
        self.original_title_label.setTextFormat(Qt.MarkdownText)
        self.original_title_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.sourceLabelFrameVerticalLayout.addWidget(self.original_title_label)

        self.source_label = QLabel(self.source_label_frame)
        self.source_label.setObjectName(u"source_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.source_label.sizePolicy().hasHeightForWidth())
        self.source_label.setSizePolicy(sizePolicy2)

        self.sourceLabelFrameVerticalLayout.addWidget(self.source_label)


        self.predictionImageFrameHorizontalLayout.addWidget(self.source_label_frame)

        self.prediction_label_frame = QFrame(self.prediction_image_frame)
        self.prediction_label_frame.setObjectName(u"prediction_label_frame")
        self.prediction_label_frame.setFrameShape(QFrame.StyledPanel)
        self.prediction_label_frame.setFrameShadow(QFrame.Raised)
        self.predictionLabelFrameVerticalLayout = QVBoxLayout(self.prediction_label_frame)
        self.predictionLabelFrameVerticalLayout.setSpacing(0)
        self.predictionLabelFrameVerticalLayout.setObjectName(u"predictionLabelFrameVerticalLayout")
        self.predictionLabelFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.prediction_title_label = QLabel(self.prediction_label_frame)
        self.prediction_title_label.setObjectName(u"prediction_title_label")
        self.prediction_title_label.setMaximumSize(QSize(16777215, 20))
        self.prediction_title_label.setAlignment(Qt.AlignCenter)

        self.predictionLabelFrameVerticalLayout.addWidget(self.prediction_title_label)

        self.prediction_label = QLabel(self.prediction_label_frame)
        self.prediction_label.setObjectName(u"prediction_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(6)
        sizePolicy3.setHeightForWidth(self.prediction_label.sizePolicy().hasHeightForWidth())
        self.prediction_label.setSizePolicy(sizePolicy3)
        self.prediction_label.setScaledContents(False)

        self.predictionLabelFrameVerticalLayout.addWidget(self.prediction_label)


        self.predictionImageFrameHorizontalLayout.addWidget(self.prediction_label_frame)


        self.predictionPagesContentsVerticalLayout.addWidget(self.prediction_image_frame)

        self.prediction_pages_scrollArea.setWidget(self.prediction_pages_contents)

        self.predictionPageVerticalLayout.addWidget(self.prediction_pages_scrollArea)

        self.prediction_page_tools_frame = QFrame(self.prediction_page)
        self.prediction_page_tools_frame.setObjectName(u"prediction_page_tools_frame")
        self.prediction_page_tools_frame.setMaximumSize(QSize(16777215, 60))
        self.prediction_page_tools_frame.setFrameShape(QFrame.StyledPanel)
        self.prediction_page_tools_frame.setFrameShadow(QFrame.Raised)
        self.predictionPageToolsFrameVerticalLayout = QVBoxLayout(self.prediction_page_tools_frame)
        self.predictionPageToolsFrameVerticalLayout.setSpacing(5)
        self.predictionPageToolsFrameVerticalLayout.setObjectName(u"predictionPageToolsFrameVerticalLayout")
        self.predictionPageToolsFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.prediction_model_selection_frame = QFrame(self.prediction_page_tools_frame)
        self.prediction_model_selection_frame.setObjectName(u"prediction_model_selection_frame")
        self.prediction_model_selection_frame.setMaximumSize(QSize(16777215, 30))
        self.prediction_model_selection_frame.setFrameShape(QFrame.StyledPanel)
        self.prediction_model_selection_frame.setFrameShadow(QFrame.Raised)
        self.predictionModelSelectionFrameHorizontalLayout = QHBoxLayout(self.prediction_model_selection_frame)
        self.predictionModelSelectionFrameHorizontalLayout.setSpacing(10)
        self.predictionModelSelectionFrameHorizontalLayout.setObjectName(u"predictionModelSelectionFrameHorizontalLayout")
        self.predictionModelSelectionFrameHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.prediction_model_selection_label = QLabel(self.prediction_model_selection_frame)
        self.prediction_model_selection_label.setObjectName(u"prediction_model_selection_label")

        self.predictionModelSelectionFrameHorizontalLayout.addWidget(self.prediction_model_selection_label, 0, Qt.AlignLeft)

        self.prediction_model_selection_comboBox = QComboBox(self.prediction_model_selection_frame)
        self.prediction_model_selection_comboBox.setObjectName(u"prediction_model_selection_comboBox")
        self.prediction_model_selection_comboBox.setMinimumSize(QSize(250, 0))

        self.predictionModelSelectionFrameHorizontalLayout.addWidget(self.prediction_model_selection_comboBox)

        self.prediction_model_selection_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.predictionModelSelectionFrameHorizontalLayout.addItem(self.prediction_model_selection_horizontalSpacer)


        self.predictionPageToolsFrameVerticalLayout.addWidget(self.prediction_model_selection_frame)

        self.prediction_file_path_frame = QFrame(self.prediction_page_tools_frame)
        self.prediction_file_path_frame.setObjectName(u"prediction_file_path_frame")
        self.prediction_file_path_frame.setMaximumSize(QSize(16777215, 20))
        self.prediction_file_path_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"}")
        self.prediction_file_path_frame.setFrameShape(QFrame.StyledPanel)
        self.prediction_file_path_frame.setFrameShadow(QFrame.Raised)
        self.predictionFilePathHorizontalLayout = QHBoxLayout(self.prediction_file_path_frame)
        self.predictionFilePathHorizontalLayout.setSpacing(5)
        self.predictionFilePathHorizontalLayout.setObjectName(u"predictionFilePathHorizontalLayout")
        self.predictionFilePathHorizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.prediction_file_path_label = QLabel(self.prediction_file_path_frame)
        self.prediction_file_path_label.setObjectName(u"prediction_file_path_label")
        self.prediction_file_path_label.setMaximumSize(QSize(16777215, 16777215))

        self.predictionFilePathHorizontalLayout.addWidget(self.prediction_file_path_label)

        self.clear_image_selection_file_pushButton = QPushButton(self.prediction_file_path_frame)
        self.clear_image_selection_file_pushButton.setObjectName(u"clear_image_selection_file_pushButton")
        self.clear_image_selection_file_pushButton.setMaximumSize(QSize(150, 35))
        self.clear_image_selection_file_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_image_selection_file_pushButton.setStyleSheet(u"")
        self.clear_image_selection_file_pushButton.setIconSize(QSize(20, 20))

        self.predictionFilePathHorizontalLayout.addWidget(self.clear_image_selection_file_pushButton)

        self.open_image_file_pushButton = QPushButton(self.prediction_file_path_frame)
        self.open_image_file_pushButton.setObjectName(u"open_image_file_pushButton")
        self.open_image_file_pushButton.setMaximumSize(QSize(150, 35))
        self.open_image_file_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_image_file_pushButton.setStyleSheet(u"")
        self.open_image_file_pushButton.setIcon(icon4)
        self.open_image_file_pushButton.setIconSize(QSize(20, 20))

        self.predictionFilePathHorizontalLayout.addWidget(self.open_image_file_pushButton)


        self.predictionPageToolsFrameVerticalLayout.addWidget(self.prediction_file_path_frame)


        self.predictionPageVerticalLayout.addWidget(self.prediction_page_tools_frame)

        self.page_list.addWidget(self.prediction_page)

        self.pageFrameVerticalLayout.addWidget(self.page_list)

        self.terminal_frame = QFrame(self.pages_frame)
        self.terminal_frame.setObjectName(u"terminal_frame")
        self.terminal_frame.setMinimumSize(QSize(0, 100))
        self.terminal_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 133, 200);\n"
"}\n"
"\n"
"QTextBrowser {\n"
"	border: none;\n"
"	font-family: \"Courier New\", \"Consolas\", monospace;\n"
"	font-size : 10pt;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid grey;\n"
"    border-radius: 5px;\n"
"    background-color: lightgrey;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(0, 133, 200);\n"
"}")
        self.terminal_frame.setFrameShape(QFrame.StyledPanel)
        self.terminal_frame.setFrameShadow(QFrame.Raised)
        self.terminalVerticalLayout = QVBoxLayout(self.terminal_frame)
        self.terminalVerticalLayout.setSpacing(0)
        self.terminalVerticalLayout.setObjectName(u"terminalVerticalLayout")
        self.terminalVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.terminal_status_frame = QFrame(self.terminal_frame)
        self.terminal_status_frame.setObjectName(u"terminal_status_frame")
        self.terminal_status_frame.setStyleSheet(u"")
        self.terminal_status_frame.setFrameShape(QFrame.StyledPanel)
        self.terminal_status_frame.setFrameShadow(QFrame.Raised)
        self.terminalStatusFrameHorizontalLayout = QHBoxLayout(self.terminal_status_frame)
        self.terminalStatusFrameHorizontalLayout.setSpacing(0)
        self.terminalStatusFrameHorizontalLayout.setObjectName(u"terminalStatusFrameHorizontalLayout")
        self.terminalStatusFrameHorizontalLayout.setContentsMargins(20, 10, 5, 15)
        self.terminal_pushButton = QPushButton(self.terminal_status_frame)
        self.terminal_pushButton.setObjectName(u"terminal_pushButton")
        self.terminal_pushButton.setMaximumSize(QSize(100, 16777215))
        self.terminal_pushButton.setStyleSheet(u"border-bottom: 2px solid qlineargradient(spread:pad, x1:0.454545, y1:1, x2:0.454, y2:0.664773, stop:0.948864 rgba(0, 171, 255, 255), stop:1 rgb(33, 37, 43));")

        self.terminalStatusFrameHorizontalLayout.addWidget(self.terminal_pushButton, 0, Qt.AlignLeft)

        self.hide_terminal_pushButton = QPushButton(self.terminal_status_frame)
        self.hide_terminal_pushButton.setObjectName(u"hide_terminal_pushButton")
        self.hide_terminal_pushButton.setMaximumSize(QSize(50, 50))
        self.hide_terminal_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.hide_terminal_pushButton.setStyleSheet(u"")
        self.hide_terminal_pushButton.setIcon(icon3)

        self.terminalStatusFrameHorizontalLayout.addWidget(self.hide_terminal_pushButton, 0, Qt.AlignRight)


        self.terminalVerticalLayout.addWidget(self.terminal_status_frame)

        self.terminal_textBrowser = QTextBrowser(self.terminal_frame)
        self.terminal_textBrowser.setObjectName(u"terminal_textBrowser")
        self.terminal_textBrowser.setStyleSheet(u"")

        self.terminalVerticalLayout.addWidget(self.terminal_textBrowser)

        self.train_progressBar = QProgressBar(self.terminal_frame)
        self.train_progressBar.setObjectName(u"train_progressBar")
        self.train_progressBar.setMaximumSize(QSize(16777215, 20))
        self.train_progressBar.setValue(0)
        self.train_progressBar.setAlignment(Qt.AlignCenter)
        self.train_progressBar.setTextVisible(True)
        self.train_progressBar.setOrientation(Qt.Horizontal)

        self.terminalVerticalLayout.addWidget(self.train_progressBar)


        self.pageFrameVerticalLayout.addWidget(self.terminal_frame)


        self.contentHorizontalLayout.addWidget(self.pages_frame)

        self.previous_trains_frame = QFrame(self.content)
        self.previous_trains_frame.setObjectName(u"previous_trains_frame")
        self.previous_trains_frame.setMinimumSize(QSize(250, 0))
        self.previous_trains_frame.setMaximumSize(QSize(250, 16777215))
        self.previous_trains_frame.setStyleSheet(u"QPushButton {\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.previous_trains_frame.setFrameShape(QFrame.StyledPanel)
        self.previous_trains_frame.setFrameShadow(QFrame.Raised)
        self.previousTrainsFrameVerticalLayout = QVBoxLayout(self.previous_trains_frame)
        self.previousTrainsFrameVerticalLayout.setSpacing(0)
        self.previousTrainsFrameVerticalLayout.setObjectName(u"previousTrainsFrameVerticalLayout")
        self.previousTrainsFrameVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.previous_trains_label_frame = QFrame(self.previous_trains_frame)
        self.previous_trains_label_frame.setObjectName(u"previous_trains_label_frame")
        self.previous_trains_label_frame.setStyleSheet(u"")
        self.previous_trains_label_frame.setFrameShape(QFrame.StyledPanel)
        self.previous_trains_label_frame.setFrameShadow(QFrame.Raised)
        self.previousTrainsListLabelFrameHorizontalLayout = QHBoxLayout(self.previous_trains_label_frame)
        self.previousTrainsListLabelFrameHorizontalLayout.setSpacing(5)
        self.previousTrainsListLabelFrameHorizontalLayout.setObjectName(u"previousTrainsListLabelFrameHorizontalLayout")
        self.previousTrainsListLabelFrameHorizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.switch_previous_trains_list_pushButton = QPushButton(self.previous_trains_label_frame)
        self.switch_previous_trains_list_pushButton.setObjectName(u"switch_previous_trains_list_pushButton")
        self.switch_previous_trains_list_pushButton.setMinimumSize(QSize(22, 22))
        self.switch_previous_trains_list_pushButton.setMaximumSize(QSize(22, 22))
        self.switch_previous_trains_list_pushButton.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/newPrefix/resources/arrow-left.png);\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/newPrefix/resources/arrow-left-hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-image: url(:/newPrefix/resources/arrow-left-pressed.png);\n"
"}")

        self.previousTrainsListLabelFrameHorizontalLayout.addWidget(self.switch_previous_trains_list_pushButton)

        self.previous_trains_list_label = QLabel(self.previous_trains_label_frame)
        self.previous_trains_list_label.setObjectName(u"previous_trains_list_label")
        self.previous_trains_list_label.setMaximumSize(QSize(16777215, 25))
        self.previous_trains_list_label.setStyleSheet(u"font-size: 12px;")
        self.previous_trains_list_label.setAlignment(Qt.AlignCenter)

        self.previousTrainsListLabelFrameHorizontalLayout.addWidget(self.previous_trains_list_label)

        self.switch_previous_trains_list_pushButton_2 = QPushButton(self.previous_trains_label_frame)
        self.switch_previous_trains_list_pushButton_2.setObjectName(u"switch_previous_trains_list_pushButton_2")
        self.switch_previous_trains_list_pushButton_2.setMinimumSize(QSize(22, 22))
        self.switch_previous_trains_list_pushButton_2.setMaximumSize(QSize(22, 22))
        self.switch_previous_trains_list_pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/newPrefix/resources/arrow-right.png);\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/newPrefix/resources/arrow-right-hover.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-image: url(:/newPrefix/resources/arrow-right-pressed.png);\n"
"}")

        self.previousTrainsListLabelFrameHorizontalLayout.addWidget(self.switch_previous_trains_list_pushButton_2)


        self.previousTrainsFrameVerticalLayout.addWidget(self.previous_trains_label_frame)

        self.previous_trains_list = QStackedWidget(self.previous_trains_frame)
        self.previous_trains_list.setObjectName(u"previous_trains_list")
        self.previous_detection_trains_list_page = QWidget()
        self.previous_detection_trains_list_page.setObjectName(u"previous_detection_trains_list_page")
        self.previousDetectTrainsListPageVerticalLayout = QVBoxLayout(self.previous_detection_trains_list_page)
        self.previousDetectTrainsListPageVerticalLayout.setSpacing(0)
        self.previousDetectTrainsListPageVerticalLayout.setObjectName(u"previousDetectTrainsListPageVerticalLayout")
        self.previousDetectTrainsListPageVerticalLayout.setContentsMargins(10, 10, 10, 0)
        self.previous_detection_trains_list_scrollArea = QScrollArea(self.previous_detection_trains_list_page)
        self.previous_detection_trains_list_scrollArea.setObjectName(u"previous_detection_trains_list_scrollArea")
        self.previous_detection_trains_list_scrollArea.setWidgetResizable(True)
        self.previous_detection_trains_list = QWidget()
        self.previous_detection_trains_list.setObjectName(u"previous_detection_trains_list")
        self.previous_detection_trains_list.setGeometry(QRect(0, 0, 230, 542))
        self.previousDetectionTrainsListVerticalLayout = QVBoxLayout(self.previous_detection_trains_list)
        self.previousDetectionTrainsListVerticalLayout.setSpacing(5)
        self.previousDetectionTrainsListVerticalLayout.setObjectName(u"previousDetectionTrainsListVerticalLayout")
        self.previousDetectionTrainsListVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.previous_detection_trains_list_scrollArea.setWidget(self.previous_detection_trains_list)

        self.previousDetectTrainsListPageVerticalLayout.addWidget(self.previous_detection_trains_list_scrollArea)

        self.previous_trains_list.addWidget(self.previous_detection_trains_list_page)
        self.previous_classification_trains_list_page = QWidget()
        self.previous_classification_trains_list_page.setObjectName(u"previous_classification_trains_list_page")
        self.previousClassificationTrainsListPageVerticalLayout = QVBoxLayout(self.previous_classification_trains_list_page)
        self.previousClassificationTrainsListPageVerticalLayout.setSpacing(0)
        self.previousClassificationTrainsListPageVerticalLayout.setObjectName(u"previousClassificationTrainsListPageVerticalLayout")
        self.previousClassificationTrainsListPageVerticalLayout.setContentsMargins(10, 10, 10, 0)
        self.previous_classification_trains_list_scrollArea = QScrollArea(self.previous_classification_trains_list_page)
        self.previous_classification_trains_list_scrollArea.setObjectName(u"previous_classification_trains_list_scrollArea")
        self.previous_classification_trains_list_scrollArea.setWidgetResizable(True)
        self.previous_classification_trains_list = QWidget()
        self.previous_classification_trains_list.setObjectName(u"previous_classification_trains_list")
        self.previous_classification_trains_list.setGeometry(QRect(0, 0, 230, 542))
        self.previousClassificationTrainsListVerticalLayout = QVBoxLayout(self.previous_classification_trains_list)
        self.previousClassificationTrainsListVerticalLayout.setSpacing(5)
        self.previousClassificationTrainsListVerticalLayout.setObjectName(u"previousClassificationTrainsListVerticalLayout")
        self.previousClassificationTrainsListVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.previous_classification_trains_list_scrollArea.setWidget(self.previous_classification_trains_list)

        self.previousClassificationTrainsListPageVerticalLayout.addWidget(self.previous_classification_trains_list_scrollArea)

        self.previous_trains_list.addWidget(self.previous_classification_trains_list_page)

        self.previousTrainsFrameVerticalLayout.addWidget(self.previous_trains_list)


        self.contentHorizontalLayout.addWidget(self.previous_trains_frame)


        self.outOfNameVerticalLayout.addWidget(self.content)


        self.mainBodyHorizontalLayout.addWidget(self.out_of_name_frame)


        self.centralwidgetLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMaximumSize(QSize(16777215, 50))
        self.main_footer.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.mainFooterHorizontalLayout = QHBoxLayout(self.main_footer)
        self.mainFooterHorizontalLayout.setSpacing(0)
        self.mainFooterHorizontalLayout.setObjectName(u"mainFooterHorizontalLayout")
        self.mainFooterHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.page_follow_label = QLabel(self.main_footer)
        self.page_follow_label.setObjectName(u"page_follow_label")
        self.page_follow_label.setStyleSheet(u"color: white;")

        self.mainFooterHorizontalLayout.addWidget(self.page_follow_label)

        self.size_grip_frame = QFrame(self.main_footer)
        self.size_grip_frame.setObjectName(u"size_grip_frame")
        self.size_grip_frame.setMinimumSize(QSize(20, 0))
        self.size_grip_frame.setMaximumSize(QSize(20, 16777215))
        self.size_grip_frame.setStyleSheet(u"background-image: url(:/newPrefix/resources/resize.png);\n"
"background-repeat: no-repeat;\n"
"background-position: right bottm;")
        self.size_grip_frame.setFrameShape(QFrame.StyledPanel)
        self.size_grip_frame.setFrameShadow(QFrame.Raised)

        self.mainFooterHorizontalLayout.addWidget(self.size_grip_frame)


        self.centralwidgetLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.page_list.setCurrentIndex(0)
        self.previous_trains_list.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_pushbutton.setText("")
        self.window_title_label.setText(QCoreApplication.translate("MainWindow", u"MODLBOX", None))
        self.minimize_pushButton.setText("")
        self.maximize_pushButton.setText("")
        self.close_pushButton.setText("")
        self.setup_buttons_label.setText(QCoreApplication.translate("MainWindow", u"     SETUP", None))
        self.reset_pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.model_buttons_label.setText(QCoreApplication.translate("MainWindow", u"     TRAIN", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.predict_pushButton.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.save_detection_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Detection Train", None))
        self.save_classification_pushButton.setText(QCoreApplication.translate("MainWindow", u"Save Classification Train", None))
        self.delete_detection_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete Detection Train", None))
        self.delete_classification_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete Classification Train", None))
        self.terminal_buttons_label.setText(QCoreApplication.translate("MainWindow", u"     TERMINAL", None))
        self.show_terminal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.hide_terminal_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.clear_terminal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.setup_page_pushButton.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.graph_page_pushButton.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.prediction_page_pushButton.setText(QCoreApplication.translate("MainWindow", u"Prediction", None))
        self.new_setup_label.setText(QCoreApplication.translate("MainWindow", u"NEW SETUP", None))
        self.method_label.setText(QCoreApplication.translate("MainWindow", u"METHOD", None))
        self.specification_label.setText(QCoreApplication.translate("MainWindow", u"SPECIFICATIONS", None))
        self.epochs_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">EPOCHS</span></p></body></html>", None))
        self.gpu_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">GPU</span></p></body></html>", None))
        self.batch_size_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">BATCH SIZE</span></p></body></html>", None))
        self.detection_stage_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>DETECTION STAGE</p></body></html>", None))
        self.model_label.setText(QCoreApplication.translate("MainWindow", u"MODEL", None))
        self.dataset_label.setText(QCoreApplication.translate("MainWindow", u"DATASET", None))
        self.dataset_comboBox.setCurrentText("")
        self.default_dataset_label.setText(QCoreApplication.translate("MainWindow", u"CHOOSE DEFAULT DATASET:", None))
        self.custom_dataset_label.setText(QCoreApplication.translate("MainWindow", u"SELECT CUSTOM DATASET", None))
        self.file_path_label.setText(QCoreApplication.translate("MainWindow", u"File:", None))
        self.open_file_pushButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.original_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Original </span></p></body></html>", None))
        self.source_label.setText("")
        self.prediction_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Prediction</span></p></body></html>", None))
        self.prediction_label.setText("")
        self.prediction_model_selection_label.setText(QCoreApplication.translate("MainWindow", u"METHOD", None))
        self.prediction_file_path_label.setText(QCoreApplication.translate("MainWindow", u"File:", None))
        self.clear_image_selection_file_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Selection", None))
        self.open_image_file_pushButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.terminal_pushButton.setText(QCoreApplication.translate("MainWindow", u"TERMINAL", None))
        self.hide_terminal_pushButton.setText("")
        self.switch_previous_trains_list_pushButton.setText("")
        self.previous_trains_list_label.setText(QCoreApplication.translate("MainWindow", u"DETECTION TRAINS LIST", None))
        self.switch_previous_trains_list_pushButton_2.setText("")
        self.page_follow_label.setText(QCoreApplication.translate("MainWindow", u"Setup Page", None))
    # retranslateUi

