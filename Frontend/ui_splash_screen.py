# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import os
import resources_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(300, 300)
        SplashScreen.setMinimumSize(QSize(300, 300))
        SplashScreen.setMaximumSize(QSize(300, 300))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.circle_bg = QFrame(self.container)
        self.circle_bg.setObjectName(u"circle_bg")
        self.circle_bg.setStyleSheet(u"QFrame{\n"
" background-color: #282a36;\n"
" color: #f8f8f2;\n"
" border-radius: 120px;\n"
"	font: 9pt \"Segoe UI\";\n"
"}")
        self.circle_bg.setFrameShape(QFrame.NoFrame)
        self.circle_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.circle_bg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.text = QFrame(self.circle_bg)
        self.text.setObjectName(u"text")
        self.text.setMaximumSize(QSize(16777215, 220))
        self.text.setStyleSheet(u"background: none")
        self.text.setFrameShape(QFrame.NoFrame)
        self.text.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.text)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.text)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 110))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 10, 100, 100))
        self.pushButton.setMinimumSize(QSize(100, 100))
        self.pushButton.setMaximumSize(QSize(100, 100))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/resources/splash-screen.png", QSize(), QIcon.Normal)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(120, 110))

        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.loading = QLabel(self.text)
        self.loading.setObjectName(u"loading")
        self.loading.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.loading.setFont(font)
        self.loading.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.loading, 2, 0, 1, 1)

        self.frame = QFrame(self.text)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.frame)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(150, 40))
        self.version.setMaximumSize(QSize(200, 40))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setBold(True)
        font1.setItalic(False)
        self.version.setFont(font1)
        self.version.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    background-color: rgb(68, 71, 90);\n"
"    border-radius: 12px;\n"
"    font-family: \"Calibri\";\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.version.setTextFormat(Qt.AutoText)

        self.verticalLayout_5.addWidget(self.version, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.text)


        self.verticalLayout_2.addWidget(self.circle_bg)


        self.verticalLayout.addWidget(self.container)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Loading...", None))
        self.pushButton.setText("")
        self.loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.version.setText(QCoreApplication.translate("SplashScreen", u" MODLBOX", None))
    # retranslateUi

