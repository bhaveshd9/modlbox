# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1099, 821)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.main_header)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setMaximumSize(QSize(50, 16777215))
        self.menu_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_button.setStyleSheet(u"QPushButton {\n"
"	width: 50px;\n"
"	height: 50px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: none;\n"
"	background-color: rgb(52, 59, 72);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/resources/icons/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon)
        self.menu_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.menu_button)

        self.title_frame = QFrame(self.main_header)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.title_frame.setStyleSheet(u"QFrame {\n"
"    font-family: Geneva;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"	font-size: 18px;\n"
"    margin-left: 10px;	\n"
"}")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.title_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.window_title = QLabel(self.title_frame)
        self.window_title.setObjectName(u"window_title")

        self.horizontalLayout_4.addWidget(self.window_title)


        self.horizontalLayout_3.addWidget(self.title_frame)

        self.top_right_buttons = QFrame(self.main_header)
        self.top_right_buttons.setObjectName(u"top_right_buttons")
        self.top_right_buttons.setMaximumSize(QSize(150, 16777215))
        self.top_right_buttons.setCursor(QCursor(Qt.ArrowCursor))
        self.top_right_buttons.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}")
        self.top_right_buttons.setFrameShape(QFrame.StyledPanel)
        self.top_right_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_right_buttons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.top_right_buttons)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMaximumSize(QSize(40, 40))
        self.minimize_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/resources/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon1)
        self.minimize_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.maximize_button = QPushButton(self.top_right_buttons)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setMaximumSize(QSize(40, 40))
        self.maximize_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/resources/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.maximize_button)

        self.close_button = QPushButton(self.top_right_buttons)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMaximumSize(QSize(40, 40))
        self.close_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_button.setStyleSheet(u"QPushButton:hover {\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(255, 140, 140);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/resources/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout_3.addWidget(self.top_right_buttons, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_left_side_menu = QFrame(self.main_body)
        self.icon_left_side_menu.setObjectName(u"icon_left_side_menu")
        self.icon_left_side_menu.setMaximumSize(QSize(16777215, 16777215))
        self.icon_left_side_menu.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(33, 37, 43);\n"
"	width: 50px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 50px;\n"
"	width: 50px;\n"
"	border: none;\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(40, 44, 52);\n"
"}")
        self.icon_left_side_menu.setFrameShape(QFrame.StyledPanel)
        self.icon_left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.icon_left_side_menu)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.icon_button_vertical_layout = QVBoxLayout()
        self.icon_button_vertical_layout.setSpacing(0)
        self.icon_button_vertical_layout.setObjectName(u"icon_button_vertical_layout")
        self.file_icon_button = QPushButton(self.icon_left_side_menu)
        self.file_icon_button.setObjectName(u"file_icon_button")
        self.file_icon_button.setMaximumSize(QSize(16777215, 16777215))
        self.file_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.file_icon_button.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/resources/icons/cil-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.file_icon_button.setIcon(icon4)
        self.file_icon_button.setCheckable(True)
        self.file_icon_button.setAutoExclusive(True)

        self.icon_button_vertical_layout.addWidget(self.file_icon_button)

        self.setup_icon_button = QPushButton(self.icon_left_side_menu)
        self.setup_icon_button.setObjectName(u"setup_icon_button")
        self.setup_icon_button.setMaximumSize(QSize(16777215, 16777215))
        self.setup_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.setup_icon_button.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/resources/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setup_icon_button.setIcon(icon5)
        self.setup_icon_button.setCheckable(True)
        self.setup_icon_button.setAutoExclusive(True)

        self.icon_button_vertical_layout.addWidget(self.setup_icon_button)

        self.analyze_icon_button = QPushButton(self.icon_left_side_menu)
        self.analyze_icon_button.setObjectName(u"analyze_icon_button")
        self.analyze_icon_button.setMaximumSize(QSize(16777215, 16777215))
        self.analyze_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.analyze_icon_button.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/resources/icons/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.analyze_icon_button.setIcon(icon6)
        self.analyze_icon_button.setCheckable(True)
        self.analyze_icon_button.setAutoExclusive(True)

        self.icon_button_vertical_layout.addWidget(self.analyze_icon_button)

        self.about_icon_button = QPushButton(self.icon_left_side_menu)
        self.about_icon_button.setObjectName(u"about_icon_button")
        self.about_icon_button.setMaximumSize(QSize(16777215, 16777215))
        self.about_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_icon_button.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/resources/icons/cil-comment-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_icon_button.setIcon(icon7)
        self.about_icon_button.setCheckable(True)
        self.about_icon_button.setAutoExclusive(True)

        self.icon_button_vertical_layout.addWidget(self.about_icon_button)


        self.verticalLayout_12.addLayout(self.icon_button_vertical_layout)

        self.icon_button_vertical_spacer = QSpacerItem(20, 593, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.icon_button_vertical_spacer)


        self.horizontalLayout.addWidget(self.icon_left_side_menu, 0, Qt.AlignLeft)

        self.full_left_side_menu = QFrame(self.main_body)
        self.full_left_side_menu.setObjectName(u"full_left_side_menu")
        self.full_left_side_menu.setMaximumSize(QSize(16777215, 16777215))
        self.full_left_side_menu.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QPushButton {\n"
"	height: 50px;\n"
"	width: 150px;\n"
"	padding-left: 17px;\n"
"	border: none;\n"
"	text-align: left;\n"
"	color: white;\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(40, 44, 52);\n"
"}")
        self.full_left_side_menu.setFrameShape(QFrame.StyledPanel)
        self.full_left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.full_left_side_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.full_button_vertical_layout = QVBoxLayout()
        self.full_button_vertical_layout.setSpacing(0)
        self.full_button_vertical_layout.setObjectName(u"full_button_vertical_layout")
        self.file_full_button = QPushButton(self.full_left_side_menu)
        self.file_full_button.setObjectName(u"file_full_button")
        self.file_full_button.setMaximumSize(QSize(16777215, 16777215))
        self.file_full_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.file_full_button.setStyleSheet(u"")
        self.file_full_button.setIcon(icon4)
        self.file_full_button.setCheckable(True)
        self.file_full_button.setAutoExclusive(True)

        self.full_button_vertical_layout.addWidget(self.file_full_button)

        self.setup_full_button = QPushButton(self.full_left_side_menu)
        self.setup_full_button.setObjectName(u"setup_full_button")
        self.setup_full_button.setMaximumSize(QSize(16777215, 16777215))
        self.setup_full_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.setup_full_button.setStyleSheet(u"")
        self.setup_full_button.setIcon(icon5)
        self.setup_full_button.setCheckable(True)
        self.setup_full_button.setAutoExclusive(True)

        self.full_button_vertical_layout.addWidget(self.setup_full_button)

        self.analyze_full_button = QPushButton(self.full_left_side_menu)
        self.analyze_full_button.setObjectName(u"analyze_full_button")
        self.analyze_full_button.setMaximumSize(QSize(16777215, 16777215))
        self.analyze_full_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.analyze_full_button.setStyleSheet(u"")
        self.analyze_full_button.setIcon(icon6)
        self.analyze_full_button.setCheckable(True)
        self.analyze_full_button.setAutoExclusive(True)

        self.full_button_vertical_layout.addWidget(self.analyze_full_button)

        self.about_full_button = QPushButton(self.full_left_side_menu)
        self.about_full_button.setObjectName(u"about_full_button")
        self.about_full_button.setMaximumSize(QSize(16777215, 16777215))
        self.about_full_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_full_button.setStyleSheet(u"")
        self.about_full_button.setIcon(icon7)
        self.about_full_button.setCheckable(True)
        self.about_full_button.setAutoExclusive(True)

        self.full_button_vertical_layout.addWidget(self.about_full_button)


        self.verticalLayout_5.addLayout(self.full_button_vertical_layout)

        self.full_button_vertical_spacer = QSpacerItem(20, 593, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.full_button_vertical_spacer)


        self.horizontalLayout.addWidget(self.full_left_side_menu, 0, Qt.AlignLeft)

        self.content = QFrame(self.main_body)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.file_page = QWidget()
        self.file_page.setObjectName(u"file_page")
        self.stackedWidget.addWidget(self.file_page)
        self.setup_page = QWidget()
        self.setup_page.setObjectName(u"setup_page")
        self.setup_page.setEnabled(True)
        self.setup_page.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QComboBox:drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
" }\n"
"\n"
"QComboBox:drop-down {\n"
"	background-image: url(:/resources/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"Q"
                        "PushButton:pressed {\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"	background-color: rgb(35, 40, 49);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.setup_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.method_frame = QFrame(self.setup_page)
        self.method_frame.setObjectName(u"method_frame")
        self.method_frame.setMaximumSize(QSize(16777215, 150))
        self.method_frame.setFrameShape(QFrame.StyledPanel)
        self.method_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.method_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.method_selection_frame = QFrame(self.method_frame)
        self.method_selection_frame.setObjectName(u"method_selection_frame")
        self.method_selection_frame.setMaximumSize(QSize(16777215, 75))
        self.method_selection_frame.setStyleSheet(u"")
        self.method_selection_frame.setFrameShape(QFrame.StyledPanel)
        self.method_selection_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.method_selection_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.method_label = QLabel(self.method_selection_frame)
        self.method_label.setObjectName(u"method_label")

        self.verticalLayout_4.addWidget(self.method_label)

        self.method_comboBox = QComboBox(self.method_selection_frame)
        self.method_comboBox.addItem("")
        self.method_comboBox.addItem("")
        self.method_comboBox.setObjectName(u"method_comboBox")
        self.method_comboBox.setMaximumSize(QSize(500, 16777215))
        self.method_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.method_comboBox)


        self.verticalLayout_7.addWidget(self.method_selection_frame)

        self.detection_stage_selection_frame = QFrame(self.method_frame)
        self.detection_stage_selection_frame.setObjectName(u"detection_stage_selection_frame")
        self.detection_stage_selection_frame.setMaximumSize(QSize(16777215, 75))
        self.detection_stage_selection_frame.setStyleSheet(u"")
        self.detection_stage_selection_frame.setFrameShape(QFrame.StyledPanel)
        self.detection_stage_selection_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.detection_stage_selection_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.detection_stage_label = QLabel(self.detection_stage_selection_frame)
        self.detection_stage_label.setObjectName(u"detection_stage_label")

        self.verticalLayout_6.addWidget(self.detection_stage_label)

        self.detection_stage_comboBox = QComboBox(self.detection_stage_selection_frame)
        self.detection_stage_comboBox.addItem("")
        self.detection_stage_comboBox.addItem("")
        self.detection_stage_comboBox.setObjectName(u"detection_stage_comboBox")
        self.detection_stage_comboBox.setMaximumSize(QSize(500, 16777215))
        self.detection_stage_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.detection_stage_comboBox)


        self.verticalLayout_7.addWidget(self.detection_stage_selection_frame)


        self.verticalLayout_16.addWidget(self.method_frame)

        self.dataset_frame = QFrame(self.setup_page)
        self.dataset_frame.setObjectName(u"dataset_frame")
        self.dataset_frame.setMaximumSize(QSize(16777215, 225))
        self.dataset_frame.setFrameShape(QFrame.StyledPanel)
        self.dataset_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.dataset_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.dataset_selection_frame = QFrame(self.dataset_frame)
        self.dataset_selection_frame.setObjectName(u"dataset_selection_frame")
        self.dataset_selection_frame.setMaximumSize(QSize(300, 75))
        self.dataset_selection_frame.setFrameShape(QFrame.StyledPanel)
        self.dataset_selection_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.dataset_selection_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dataset_label = QLabel(self.dataset_selection_frame)
        self.dataset_label.setObjectName(u"dataset_label")

        self.verticalLayout_8.addWidget(self.dataset_label)

        self.dataset_comboBox = QComboBox(self.dataset_selection_frame)
        self.dataset_comboBox.addItem("")
        self.dataset_comboBox.addItem("")
        self.dataset_comboBox.setObjectName(u"dataset_comboBox")
        self.dataset_comboBox.setMaximumSize(QSize(500, 16777215))
        self.dataset_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.dataset_comboBox)


        self.verticalLayout_11.addWidget(self.dataset_selection_frame)

        self.default_dataset_frame = QFrame(self.dataset_frame)
        self.default_dataset_frame.setObjectName(u"default_dataset_frame")
        self.default_dataset_frame.setMaximumSize(QSize(16777215, 75))
        self.default_dataset_frame.setFrameShape(QFrame.StyledPanel)
        self.default_dataset_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.default_dataset_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.default_dataset_label = QLabel(self.default_dataset_frame)
        self.default_dataset_label.setObjectName(u"default_dataset_label")

        self.verticalLayout_9.addWidget(self.default_dataset_label)

        self.default_dataset_comboBox = QComboBox(self.default_dataset_frame)
        self.default_dataset_comboBox.setObjectName(u"default_dataset_comboBox")
        self.default_dataset_comboBox.setMaximumSize(QSize(500, 16777215))

        self.verticalLayout_9.addWidget(self.default_dataset_comboBox)


        self.verticalLayout_11.addWidget(self.default_dataset_frame)

        self.custom_dataset_frame = QFrame(self.dataset_frame)
        self.custom_dataset_frame.setObjectName(u"custom_dataset_frame")
        self.custom_dataset_frame.setMaximumSize(QSize(16777215, 75))
        self.custom_dataset_frame.setFrameShape(QFrame.StyledPanel)
        self.custom_dataset_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.custom_dataset_frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.custom_dataset_label = QLabel(self.custom_dataset_frame)
        self.custom_dataset_label.setObjectName(u"custom_dataset_label")

        self.verticalLayout_10.addWidget(self.custom_dataset_label)

        self.file_path_frame = QFrame(self.custom_dataset_frame)
        self.file_path_frame.setObjectName(u"file_path_frame")
        self.file_path_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"}")
        self.file_path_frame.setFrameShape(QFrame.StyledPanel)
        self.file_path_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.file_path_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.file_path_label = QLabel(self.file_path_frame)
        self.file_path_label.setObjectName(u"file_path_label")
        self.file_path_label.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_5.addWidget(self.file_path_label)

        self.open_file_button = QPushButton(self.file_path_frame)
        self.open_file_button.setObjectName(u"open_file_button")
        self.open_file_button.setMaximumSize(QSize(100, 35))
        self.open_file_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_file_button.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.open_file_button)


        self.verticalLayout_10.addWidget(self.file_path_frame)


        self.verticalLayout_11.addWidget(self.custom_dataset_frame)


        self.verticalLayout_16.addWidget(self.dataset_frame)

        self.gpu_frame = QFrame(self.setup_page)
        self.gpu_frame.setObjectName(u"gpu_frame")
        self.gpu_frame.setMaximumSize(QSize(16777215, 75))
        self.gpu_frame.setFrameShape(QFrame.StyledPanel)
        self.gpu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.gpu_frame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gpu_label = QLabel(self.gpu_frame)
        self.gpu_label.setObjectName(u"gpu_label")

        self.verticalLayout_13.addWidget(self.gpu_label)

        self.gpu_comboBox = QComboBox(self.gpu_frame)
        self.gpu_comboBox.addItem("")
        self.gpu_comboBox.addItem("")
        self.gpu_comboBox.addItem("")
        self.gpu_comboBox.addItem("")
        self.gpu_comboBox.setObjectName(u"gpu_comboBox")
        self.gpu_comboBox.setMaximumSize(QSize(500, 16777215))
        self.gpu_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.gpu_comboBox)


        self.verticalLayout_16.addWidget(self.gpu_frame)

        self.epoch_frame = QFrame(self.setup_page)
        self.epoch_frame.setObjectName(u"epoch_frame")
        self.epoch_frame.setMaximumSize(QSize(16777215, 75))
        self.epoch_frame.setFrameShape(QFrame.StyledPanel)
        self.epoch_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.epoch_frame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.epoch_label = QLabel(self.epoch_frame)
        self.epoch_label.setObjectName(u"epoch_label")

        self.verticalLayout_14.addWidget(self.epoch_label)

        self.epoch_lineEdit = QLineEdit(self.epoch_frame)
        self.epoch_lineEdit.setObjectName(u"epoch_lineEdit")
        self.epoch_lineEdit.setMaximumSize(QSize(16777215, 100))
        self.epoch_lineEdit.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout_14.addWidget(self.epoch_lineEdit)


        self.verticalLayout_16.addWidget(self.epoch_frame)

        self.backbone_frame = QFrame(self.setup_page)
        self.backbone_frame.setObjectName(u"backbone_frame")
        self.backbone_frame.setMaximumSize(QSize(16777215, 75))
        self.backbone_frame.setFrameShape(QFrame.StyledPanel)
        self.backbone_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.backbone_frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.backbone_label = QLabel(self.backbone_frame)
        self.backbone_label.setObjectName(u"backbone_label")

        self.verticalLayout_15.addWidget(self.backbone_label)

        self.backbone_comboBox = QComboBox(self.backbone_frame)
        self.backbone_comboBox.setObjectName(u"backbone_comboBox")
        self.backbone_comboBox.setMaximumSize(QSize(500, 16777215))
        self.backbone_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_15.addWidget(self.backbone_comboBox)


        self.verticalLayout_16.addWidget(self.backbone_frame)

        self.start_frame = QFrame(self.setup_page)
        self.start_frame.setObjectName(u"start_frame")
        self.start_frame.setMaximumSize(QSize(16777215, 75))
        self.start_frame.setFrameShape(QFrame.StyledPanel)
        self.start_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.start_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.start_pushButton = QPushButton(self.start_frame)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setMaximumSize(QSize(100, 35))
        self.start_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_pushButton.setStyleSheet(u"font: bold;")
        self.start_pushButton.setIcon(icon5)

        self.gridLayout.addWidget(self.start_pushButton, 0, 0, 1, 1)


        self.verticalLayout_16.addWidget(self.start_frame)

        self.stackedWidget.addWidget(self.setup_page)
        self.analyze_page = QWidget()
        self.analyze_page.setObjectName(u"analyze_page")
        self.stackedWidget.addWidget(self.analyze_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.stackedWidget.addWidget(self.about_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.content)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMaximumSize(QSize(16777215, 50))
        self.main_footer.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.main_footer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.test_label = QLabel(self.main_footer)
        self.test_label.setObjectName(u"test_label")
        self.test_label.setStyleSheet(u"color:white;")

        self.horizontalLayout_6.addWidget(self.test_label, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_button.toggled.connect(self.icon_left_side_menu.setHidden)
        self.menu_button.toggled.connect(self.full_left_side_menu.setVisible)
        self.file_icon_button.toggled.connect(self.file_full_button.setChecked)
        self.setup_icon_button.toggled.connect(self.setup_full_button.setChecked)
        self.analyze_icon_button.toggled.connect(self.analyze_full_button.setChecked)
        self.about_icon_button.toggled.connect(self.about_full_button.setChecked)
        self.file_full_button.toggled.connect(self.file_icon_button.setChecked)
        self.setup_full_button.toggled.connect(self.setup_icon_button.setChecked)
        self.analyze_full_button.toggled.connect(self.analyze_icon_button.setChecked)
        self.about_full_button.toggled.connect(self.about_icon_button.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_button.setText("")
        self.window_title.setText(QCoreApplication.translate("MainWindow", u"MODLBOX", None))
        self.minimize_button.setText("")
        self.maximize_button.setText("")
        self.close_button.setText("")
        self.file_icon_button.setText("")
        self.setup_icon_button.setText("")
        self.analyze_icon_button.setText("")
        self.about_icon_button.setText("")
        self.file_full_button.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.setup_full_button.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.analyze_full_button.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.about_full_button.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.method_label.setText(QCoreApplication.translate("MainWindow", u"METHOD:", None))
        self.method_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Classification", None))
        self.method_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Detection", None))

        self.detection_stage_label.setText(QCoreApplication.translate("MainWindow", u"DETECTION STAGE:", None))
        self.detection_stage_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.detection_stage_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))

        self.dataset_label.setText(QCoreApplication.translate("MainWindow", u"DATASET:", None))
        self.dataset_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Default Dataset", None))
        self.dataset_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Custom Dataset", None))

        self.default_dataset_label.setText(QCoreApplication.translate("MainWindow", u"CHOOSE DEFAULT DATASET:", None))
        self.custom_dataset_label.setText(QCoreApplication.translate("MainWindow", u"SELECT CUSTOM DATASET:", None))
        self.file_path_label.setText(QCoreApplication.translate("MainWindow", u"File:", None))
        self.open_file_button.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.gpu_label.setText(QCoreApplication.translate("MainWindow", u"GPU:", None))
        self.gpu_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.gpu_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.gpu_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))
        self.gpu_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"All", None))

        self.epoch_label.setText(QCoreApplication.translate("MainWindow", u"EPOCH:", None))
        self.backbone_label.setText(QCoreApplication.translate("MainWindow", u"BACKBONE:", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.test_label.setText(QCoreApplication.translate("MainWindow", u"File Page", None))
    # retranslateUi

