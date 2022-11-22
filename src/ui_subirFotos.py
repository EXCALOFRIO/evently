# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subirFotos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(510, 362)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(219, 175, 255);")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_Seleccionar_Imagen = QPushButton(self.centralwidget)
        self.pushButton_Seleccionar_Imagen.setObjectName(u"pushButton_Seleccionar_Imagen")
        self.pushButton_Seleccionar_Imagen.setGeometry(QRect(330, 80, 161, 41))
        self.pushButton_Seleccionar_Imagen.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_Cancelar = QPushButton(self.centralwidget)
        self.pushButton_Cancelar.setObjectName(u"pushButton_Cancelar")
        self.pushButton_Cancelar.setGeometry(QRect(330, 180, 161, 41))
        self.pushButton_Cancelar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_Foto = QLabel(self.centralwidget)
        self.label_Foto.setObjectName(u"label_Foto")
        self.label_Foto.setGeometry(QRect(10, 30, 311, 271))
        self.label_Foto.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_Subir_Imagen = QPushButton(self.centralwidget)
        self.pushButton_Subir_Imagen.setObjectName(u"pushButton_Subir_Imagen")
        self.pushButton_Subir_Imagen.setGeometry(QRect(330, 130, 161, 41))
        self.pushButton_Subir_Imagen.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 510, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_Seleccionar_Imagen.clicked.connect(self.label_Foto.clear)
        self.pushButton_Cancelar.clicked.connect(self.label_Foto.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_Seleccionar_Imagen.setText(QCoreApplication.translate("MainWindow", u"Seleccionar imagen", None))
        self.pushButton_Cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_Foto.setText("")
        self.pushButton_Subir_Imagen.setText(QCoreApplication.translate("MainWindow", u"Subir imagen", None))
    # retranslateUi

