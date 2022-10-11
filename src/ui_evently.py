# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/daguerre/C433-E15C/CEU/3º/1º_Cuatri/Ing_Software/evently/src/evently.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QInputDialog, QFileDialog
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.uic import loadUi
import pyglet
import webview

from baseDatosPrueba import datosUsuario, insertarFiesta, insertarValoracion, variableUsuarioSimp


pyglet.font.add_file('fuentes/productSans.ttf')  # ABeeZee


        
class Ui_MainWindow(object):
        #BOTON DE AÑADIR DISCOTECA
        def annadirDiscoteca(self):
                insertarFiesta(self.lineEdit_nombreDiscoteca.text(), self.lineEdit_calleDiscoteca.text(),self.lineEdit_numeroDiscoteca.text(), self.lineEdit_zonaDiscoteca.text(), 'data')

        #BOTON DE AÑADIR FIESTA
        def annadirFiesta(self):
                insertarFiesta(self.lineEdit_nombreFiesta.text(), self.lineEdit_calleFiesta.text(),self.lineEdit_numeroFiesta.text(), self.lineEdit_zonaFiesta.text(), 'data')

        #BOTON DE AÑADIR RESEÑA
        def annadirResenna(self):
                #comprueba que radioButton_ esta seleccionado
                if self.radioButton_1estrella.isChecked():
                        valoracion = 1
                elif self.radioButton_2estrellas .isChecked():
                        valoracion = 2
                elif self.radioButton_3estrellas.isChecked():
                        valoracion = 3
                elif self.radioButton_4estrellas.isChecked():
                        valoracion = 4
                elif self.radioButton_5estrellas.isChecked():
                        valoracion = 5
                else:
                        valoracion = 0
                insertarValoracion(datosUsuario('usuario'),self.lineEdit_2.text(),valoracion,self.textEdit.toPlainText(), 'data')


        #BOTON DE BUSQUEDA
        def busquedaFilter(self):
                print("busqueda filter")


        def buttonMapa(self):
                self.stackedWidget.setCurrentWidget(self.page_mapa)
                #import mapViewer
                webview.create_window('Evently - Mapa de discotecas', '../mapa.html')
                webview.start()
                print("he selecionado el boton MAPA")
        
        def buttonFiltrado(self):
                self.stackedWidget.setCurrentWidget(self.page_filtrado)
                print("he selecionado el boton FILTRADO")

        def buttonDiscotecas(self):
                self.stackedWidget.setCurrentWidget(self.page_AddDiscoteca)
                print("he selecionado el boton DISCOTECAS")
        
        def buttonFiesta(self):
                self.stackedWidget.setCurrentWidget(self.page_AddFiesta)
                print("he selecionado el boton FIESTA")     
                
        
        def buttonResenna(self):
                self.stackedWidget.setCurrentWidget(self.page_AddResenna)
                print("he selecionado el boton RESEÑA")
    
        

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(812, 533)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_12.setSpacing(0)
                self.verticalLayout_12.setObjectName("verticalLayout_12")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setStyleSheet("background-color: rgb(36, 31, 49);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
                self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.frame_superior = QtWidgets.QFrame(self.frame)
                self.frame_superior.setMinimumSize(QtCore.QSize(0, 42))
                self.frame_superior.setStyleSheet("QFrame{\n"
"    background-color: rgb(87, 227, 137);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #000000ff;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton: hover{\n"
"    background-color: rgb(61, 61, 61);\n"
"    border-radius: 20px\n"
"}")

        
#crea una funcion para cuando se pulse el boton pushButton_aceptarFiesta
#llama a esa funcion cuando se pulsar pushButton_aceptarFiesta




                """FRAME DONDE ESTA DODO MENOS LA BARRA DE ARRIBA"""
                self.frame_contenido = QtWidgets.QFrame(self.frame)
                self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_contenido.setObjectName("frame_contenido")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_contenido)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.frame_control = QtWidgets.QFrame(self.frame_contenido)
                self.frame_control.setMinimumSize(QtCore.QSize(300, 0))
                self.frame_control.setMaximumSize(QtCore.QSize(1000, 16777215))
                self.frame_control.setStyleSheet("QFrame{\n"
"    background-color: rgb(87, 227, 137);\n"
"}\n"
"\n"
" QPushButton{\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    color: rgb(255,255,255);\n"
"    font: 77 12pt \"Arial Black\";\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"    background-color: white;\n"
"    border-top-left-radius: 20px;\n"
"    border-bottom-left-radius: 20px;\n"
"    color: rgb(0,0,0);\n"
"    font: 77 12pt \"Arial Black\";\n"
"}")
                """FRAME DONDE ESTA EL MENU"""
                self.frame_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_control.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_control.setObjectName("frame_control")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_control)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.pushButton_Mapa = QtWidgets.QPushButton(self.frame_control)
                self.pushButton_Mapa.setEnabled(True)
                self.pushButton_Mapa.setMinimumSize(QtCore.QSize(0, 40))
                self.pushButton_Mapa.clicked.connect(self.buttonMapa)
                self.pushButton_Mapa.setObjectName("pushButton_Mapa")
                self.verticalLayout_3.addWidget(self.pushButton_Mapa)
                self.pushButton_Filtrado = QtWidgets.QPushButton(self.frame_control)
                self.pushButton_Filtrado.setEnabled(True)
                self.pushButton_Filtrado.setMinimumSize(QtCore.QSize(0, 40))
                self.pushButton_Filtrado.clicked.connect(self.buttonFiltrado)
                self.pushButton_Filtrado.setObjectName("pushButton_Filtrado")
                self.verticalLayout_3.addWidget(self.pushButton_Filtrado)
                self.pushButton_Discoteca = QtWidgets.QPushButton(self.frame_control)
                self.pushButton_Discoteca.setEnabled(True)
                self.pushButton_Discoteca.setMinimumSize(QtCore.QSize(0, 40))
                self.pushButton_Discoteca.clicked.connect(self.buttonDiscotecas)
                self.pushButton_Discoteca.setObjectName("pushButton_Discoteca")
                self.verticalLayout_3.addWidget(self.pushButton_Discoteca)
                self.pushButton_Fiesta = QtWidgets.QPushButton(self.frame_control)
                self.pushButton_Fiesta.setEnabled(True)
                self.pushButton_Fiesta.setMinimumSize(QtCore.QSize(0, 40))
                self.pushButton_Fiesta.clicked.connect(self.buttonFiesta)
                self.pushButton_Fiesta.setObjectName("pushButton_Fiesta")
                self.verticalLayout_3.addWidget(self.pushButton_Fiesta)
                self.pushButton_Resenna = QtWidgets.QPushButton(self.frame_control)
                self.pushButton_Resenna.setEnabled(True)
                self.pushButton_Resenna.setMinimumSize(QtCore.QSize(0, 40))
                self.pushButton_Resenna.clicked.connect(self.buttonResenna)
                self.pushButton_Resenna.setObjectName("pushButton_Resenna")
                self.verticalLayout_3.addWidget(self.pushButton_Resenna)
                self.horizontalLayout.addWidget(self.frame_control)
                self.frame_paginas = QtWidgets.QFrame(self.frame_contenido)
                self.frame_paginas.setStyleSheet("QFrame{\n"
"    background-color: rgb(87, 227, 137);\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 87 12pt \"Arial Black\";    \n"
"    background-color:#000000ff;\n"
"    color: rgb(87, 227, 137);\n"
"    border: 0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border:0px;\n"
"    color: rbg(255,255,255);\n"
"    border-bottom: 2px solid rgb(0,0,0);\n"
"    font: 75 12pt \"ABeeZee\";\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 0,0);\n"
"    border-radius: 15px;\n"
"    color: rgb(255,255,255);\n"
"    font : 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(87, 227, 137);\n"
"    border-radius: 15px;\n"
"    color: rgb(0,0,0);\n"
"    font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"\n"
"")
                """DONDE ESTA LO DE A LA DERECHA DE LA PARTE DONDE ESTÁ EL MENÚ, ES DECIR DONDE VA A APARECER EL RESTO DE PÁGINAS"""
                self.frame_paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_paginas.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_paginas.setObjectName("frame_paginas")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_paginas)
                self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
                self.verticalLayout_4.setSpacing(1)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.stackedWidget = QtWidgets.QStackedWidget(self.frame_paginas)
                self.stackedWidget.setObjectName("stackedWidget")
                
                """PÁGINA DEL MAPA"""
                self.page_mapa = QtWidgets.QWidget()
                self.page_mapa.setObjectName("page_mapa")
                self.stackedWidget.addWidget(self.page_mapa)
                self.page_filtrado = QtWidgets.QWidget()
                
                """PÁGINA DEL FILTRADO"""
                self.page_filtrado.setObjectName("page_filtrado")
                self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_filtrado)
                self.verticalLayout_13.setObjectName("verticalLayout_13")
                self.label_6 = QtWidgets.QLabel(self.page_filtrado)
                self.label_6.setAlignment(QtCore.Qt.AlignCenter)
                self.label_6.setObjectName("label_6")
                self.verticalLayout_13.addWidget(self.label_6)
                self.comboBox = QtWidgets.QComboBox(self.page_filtrado)
                self.comboBox.setStyleSheet("color: rgb(87, 227, 137);\n"
"background-color: #000000ff;")
                self.comboBox.setObjectName("comboBox")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.comboBox.addItem("")
                self.verticalLayout_13.addWidget(self.comboBox)
                self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_9.setObjectName("horizontalLayout_9")
                self.lineEdit_BusquedaFiltrado = QtWidgets.QLineEdit(self.page_filtrado)
                self.lineEdit_BusquedaFiltrado.setStyleSheet("color: rgb(87, 227, 137);")
                self.lineEdit_BusquedaFiltrado.setObjectName("lineEdit_BusquedaFiltrado")
                self.horizontalLayout_9.addWidget(self.lineEdit_BusquedaFiltrado)
                spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_9.addItem(spacerItem1)
                self.pushButton_BuscarFiltrado = QtWidgets.QPushButton(self.page_filtrado)
                self.pushButton_BuscarFiltrado.setObjectName("pushButton_BuscarFiltrado")
                self.pushButton_BuscarFiltrado.clicked.connect(self.busquedaFilter)
                self.horizontalLayout_9.addWidget(self.pushButton_BuscarFiltrado)
                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_9.addItem(spacerItem2)
                self.verticalLayout_13.addLayout(self.horizontalLayout_9)
                self.textBrowser_Fltrado = QtWidgets.QTextBrowser(self.page_filtrado)
                self.textBrowser_Fltrado.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.textBrowser_Fltrado.setObjectName("textBrowser_Fltrado")
                self.verticalLayout_13.addWidget(self.textBrowser_Fltrado)
                self.stackedWidget.addWidget(self.page_filtrado)
                
                """PÁGINA DE DISCOTECAS"""           
                self.page_AddDiscoteca = QtWidgets.QWidget()
                self.page_AddDiscoteca.setObjectName("page_AddDiscoteca")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.page_AddDiscoteca)
                self.verticalLayout.setObjectName("verticalLayout")
                self.label_9 = QtWidgets.QLabel(self.page_AddDiscoteca)
                self.label_9.setAlignment(QtCore.Qt.AlignCenter)
                self.label_9.setWordWrap(False)
                self.label_9.setObjectName("label_9")
                self.verticalLayout.addWidget(self.label_9)
                spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem3)
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout()
                self.verticalLayout_5.setSpacing(30)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.label_nombreDiscoteca = QtWidgets.QLabel(self.page_AddDiscoteca)
                self.label_nombreDiscoteca.setAlignment(QtCore.Qt.AlignCenter)
                self.label_nombreDiscoteca.setObjectName("label_nombreDiscoteca")
                self.verticalLayout_5.addWidget(self.label_nombreDiscoteca)
                self.label_zonaDiscoteca = QtWidgets.QLabel(self.page_AddDiscoteca)
                self.label_zonaDiscoteca.setAlignment(QtCore.Qt.AlignCenter)
                self.label_zonaDiscoteca.setObjectName("label_zonaDiscoteca")
                self.verticalLayout_5.addWidget(self.label_zonaDiscoteca)
                self.label_calleDiscoteca = QtWidgets.QLabel(self.page_AddDiscoteca)
                self.label_calleDiscoteca.setAlignment(QtCore.Qt.AlignCenter)
                self.label_calleDiscoteca.setObjectName("label_calleDiscoteca")
                self.verticalLayout_5.addWidget(self.label_calleDiscoteca)
                self.label_numeroDiscoteca = QtWidgets.QLabel(self.page_AddDiscoteca)
                self.label_numeroDiscoteca.setAlignment(QtCore.Qt.AlignCenter)
                self.label_numeroDiscoteca.setObjectName("label_numeroDiscoteca")
                self.verticalLayout_5.addWidget(self.label_numeroDiscoteca)
                self.horizontalLayout_2.addLayout(self.verticalLayout_5)
                self.verticalLayout_6 = QtWidgets.QVBoxLayout()
                self.verticalLayout_6.setSpacing(60)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.lineEdit_nombreDiscoteca = QtWidgets.QLineEdit(self.page_AddDiscoteca)
                self.lineEdit_nombreDiscoteca.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_nombreDiscoteca.setText("")
                self.lineEdit_nombreDiscoteca.setObjectName("lineEdit_nombreDiscoteca")
                self.verticalLayout_6.addWidget(self.lineEdit_nombreDiscoteca)
                self.lineEdit_zonaDiscoteca = QtWidgets.QLineEdit(self.page_AddDiscoteca)
                self.lineEdit_zonaDiscoteca.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_zonaDiscoteca.setObjectName("lineEdit_zonaDiscoteca")
                self.verticalLayout_6.addWidget(self.lineEdit_zonaDiscoteca)
                self.lineEdit_calleDiscoteca = QtWidgets.QLineEdit(self.page_AddDiscoteca)
                self.lineEdit_calleDiscoteca.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_calleDiscoteca.setText("")
                self.lineEdit_calleDiscoteca.setObjectName("lineEdit_calleDiscoteca")
                self.verticalLayout_6.addWidget(self.lineEdit_calleDiscoteca)
                self.lineEdit_numeroDiscoteca = QtWidgets.QLineEdit(self.page_AddDiscoteca)
                self.lineEdit_numeroDiscoteca.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_numeroDiscoteca.setObjectName("lineEdit_numeroDiscoteca")
                self.verticalLayout_6.addWidget(self.lineEdit_numeroDiscoteca)
                self.horizontalLayout_2.addLayout(self.verticalLayout_6)
                spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_2.addItem(spacerItem4)
                self.verticalLayout.addLayout(self.horizontalLayout_2)
                spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem5)
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_5.addItem(spacerItem6)
                self.pushButton_aceptarDiscoteca = QtWidgets.QPushButton(self.page_AddDiscoteca)
                self.pushButton_aceptarDiscoteca.setMaximumSize(QtCore.QSize(180, 16777215))
                self.pushButton_aceptarDiscoteca.setObjectName("pushButton_aceptarDiscoteca")
                self.pushButton_aceptarDiscoteca.clicked.connect(self.annadirDiscoteca)
                self.horizontalLayout_5.addWidget(self.pushButton_aceptarDiscoteca)
                spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_5.addItem(spacerItem7)
                self.verticalLayout.addLayout(self.horizontalLayout_5)
                self.verticalLayout.setStretch(0, 1)
                self.verticalLayout.setStretch(2, 8)
                self.stackedWidget.addWidget(self.page_AddDiscoteca)
                
                """PAGINA DE FIESTAS"""
                self.page_AddFiesta = QtWidgets.QWidget()
                self.page_AddFiesta.setObjectName("page_AddFiesta")
                self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_AddFiesta)
                self.verticalLayout_9.setObjectName("verticalLayout_9")
                self.label_2 = QtWidgets.QLabel(self.page_AddFiesta)
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setObjectName("label_2")
                self.verticalLayout_9.addWidget(self.label_2)
                spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_9.addItem(spacerItem8)
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout()
                self.verticalLayout_7.setSpacing(30)
                self.verticalLayout_7.setObjectName("verticalLayout_7")
                self.label_nombreFiesta = QtWidgets.QLabel(self.page_AddFiesta)
                self.label_nombreFiesta.setAlignment(QtCore.Qt.AlignCenter)
                self.label_nombreFiesta.setObjectName("label_nombreFiesta")
                self.verticalLayout_7.addWidget(self.label_nombreFiesta)
                self.label_zonaFiesta = QtWidgets.QLabel(self.page_AddFiesta)
                self.label_zonaFiesta.setAlignment(QtCore.Qt.AlignCenter)
                self.label_zonaFiesta.setObjectName("label_zonaFiesta")
                self.verticalLayout_7.addWidget(self.label_zonaFiesta)
                self.label_calleFiesta = QtWidgets.QLabel(self.page_AddFiesta)
                self.label_calleFiesta.setAlignment(QtCore.Qt.AlignCenter)
                self.label_calleFiesta.setObjectName("label_calleFiesta")
                self.verticalLayout_7.addWidget(self.label_calleFiesta)
                self.label_numeroFiesta = QtWidgets.QLabel(self.page_AddFiesta)
                self.label_numeroFiesta.setAlignment(QtCore.Qt.AlignCenter)
                self.label_numeroFiesta.setObjectName("label_numeroFiesta")
                self.verticalLayout_7.addWidget(self.label_numeroFiesta)
                self.horizontalLayout_6.addLayout(self.verticalLayout_7)
                self.verticalLayout_8 = QtWidgets.QVBoxLayout()
                self.verticalLayout_8.setSpacing(60)
                self.verticalLayout_8.setObjectName("verticalLayout_8")
                self.lineEdit_nombreFiesta = QtWidgets.QLineEdit(self.page_AddFiesta)
                self.lineEdit_nombreFiesta.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_nombreFiesta.setObjectName("lineEdit_nombreFiesta")
                self.verticalLayout_8.addWidget(self.lineEdit_nombreFiesta)
                self.lineEdit_zonaFiesta = QtWidgets.QLineEdit(self.page_AddFiesta)
                self.lineEdit_zonaFiesta.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_zonaFiesta.setText("")
                self.lineEdit_zonaFiesta.setObjectName("lineEdit_zonaFiesta")
                self.verticalLayout_8.addWidget(self.lineEdit_zonaFiesta)
                self.lineEdit_calleFiesta = QtWidgets.QLineEdit(self.page_AddFiesta)
                self.lineEdit_calleFiesta.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_calleFiesta.setObjectName("lineEdit_calleFiesta")
                self.verticalLayout_8.addWidget(self.lineEdit_calleFiesta)
                self.lineEdit_numeroFiesta = QtWidgets.QLineEdit(self.page_AddFiesta)
                self.lineEdit_numeroFiesta.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_numeroFiesta.setObjectName("lineEdit_numeroFiesta")
                self.verticalLayout_8.addWidget(self.lineEdit_numeroFiesta)
                self.horizontalLayout_6.addLayout(self.verticalLayout_8)
                spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_6.addItem(spacerItem9)
                self.verticalLayout_9.addLayout(self.horizontalLayout_6)
                spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout_9.addItem(spacerItem10)
                self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_7.addItem(spacerItem11)
                self.pushButton_aceptarFiesta = QtWidgets.QPushButton(self.page_AddFiesta)
                self.pushButton_aceptarFiesta.setObjectName("pushButton_aceptarFiesta")
                self.horizontalLayout_7.addWidget(self.pushButton_aceptarFiesta)
                #pulsar boton aceptar
                self.pushButton_aceptarFiesta.clicked.connect(self.annadirFiesta)
                spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_7.addItem(spacerItem12)
                self.verticalLayout_9.addLayout(self.horizontalLayout_7)
                self.verticalLayout_9.setStretch(0, 1)
                self.verticalLayout_9.setStretch(2, 8)
                self.stackedWidget.addWidget(self.page_AddFiesta)
                self.page_AddResenna = QtWidgets.QWidget()
                self.page_AddResenna.setStyleSheet("QFrame{\n"
"    background-color: #000000ff;\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 87 12pt \"Arial Black\";    \n"
"    background-color:#000000ff;\n"
"    color: rgb(87, 227, 137);\n"
"    border: 0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border:0px;\n"
"    color: rbg(255,255,255);\n"
"    border-bottom: 2px solid rgb(0,0,0);\n"
"    font: 75 12pt \"ABeeZee\";\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(0, 0,0);\n"
"    border-radius: 15px;\n"
"    color: rgb(255,255,255);\n"
"    font : 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(87, 227, 137);\n"
"    border-radius: 15px;\n"
"    color: rgb(0,0,0);\n"
"    font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QRadioButton{\n"
"    background-color: rgb(87, 227, 137);\n"
"    font: 87 12pt \"Arial Black\";    \n"
"}")
                """PÁGINA DE AGREGAR RESEÑA"""
                self.page_AddResenna.setObjectName("page_AddResenna")
                self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page_AddResenna)
                self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_8.setSpacing(0)
                self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                self.frame_2 = QtWidgets.QFrame(self.page_AddResenna)
                self.frame_2.setStyleSheet("")
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_2)
                self.verticalLayout_10.setObjectName("verticalLayout_10")
                self.label = QtWidgets.QLabel(self.frame_2)
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.verticalLayout_10.addWidget(self.label)
                self.lineEdit_UsuarioResea = QtWidgets.QLineEdit(self.frame_2)
                self.lineEdit_UsuarioResea.setObjectName("lineEdit_UsuarioResea")
                self.verticalLayout_10.addWidget(self.lineEdit_UsuarioResea)
                self.label_4 = QtWidgets.QLabel(self.frame_2)
                self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.label_4.setAlignment(QtCore.Qt.AlignCenter)
                self.label_4.setObjectName("label_4")
                self.verticalLayout_10.addWidget(self.label_4)
                self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.verticalLayout_10.addWidget(self.lineEdit_2)
                self.textEdit = QtWidgets.QTextEdit(self.frame_2)
                self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
                self.textEdit.setObjectName("textEdit")
                self.verticalLayout_10.addWidget(self.textEdit)
                self.radioButton_1estrella = QtWidgets.QRadioButton(self.frame_2)
                self.radioButton_1estrella.setObjectName("radioButton_1estrella")
                self.verticalLayout_10.addWidget(self.radioButton_1estrella)
                self.radioButton_2estrellas = QtWidgets.QRadioButton(self.frame_2)
                self.radioButton_2estrellas.setObjectName("radioButton_2estrellas")
                self.verticalLayout_10.addWidget(self.radioButton_2estrellas)
                self.radioButton_3estrellas = QtWidgets.QRadioButton(self.frame_2)
                self.radioButton_3estrellas.setObjectName("radioButton_3estrellas")
                self.verticalLayout_10.addWidget(self.radioButton_3estrellas)
                self.radioButton_4estrellas = QtWidgets.QRadioButton(self.frame_2)
                self.radioButton_4estrellas.setObjectName("radioButton_4estrellas")
                self.verticalLayout_10.addWidget(self.radioButton_4estrellas)
                self.radioButton_5estrellas = QtWidgets.QRadioButton(self.frame_2)
                self.radioButton_5estrellas.setObjectName("radioButton_5estrellas")
                self.verticalLayout_10.addWidget(self.radioButton_5estrellas)
                self.pushButton_AddResenna = QtWidgets.QPushButton(self.frame_2)
                self.pushButton_AddResenna.setObjectName("pushButton_AddResenna")
                self.verticalLayout_10.addWidget(self.pushButton_AddResenna)
                self.pushButton_AddResenna.clicked.connect(self.annadirResenna)
                self.horizontalLayout_8.addWidget(self.frame_2)
                self.frame_3 = QtWidgets.QFrame(self.page_AddResenna)
                self.frame_3.setStyleSheet("")
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_3)
                self.verticalLayout_11.setObjectName("verticalLayout_11")
                self.label_5 = QtWidgets.QLabel(self.frame_3)
                self.label_5.setAlignment(QtCore.Qt.AlignCenter)
                self.label_5.setObjectName("label_5")
                self.verticalLayout_11.addWidget(self.label_5)
                self.textBrowser = QtWidgets.QTextBrowser(self.frame_3)
                self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.textBrowser.setObjectName("textBrowser")
                self.verticalLayout_11.addWidget(self.textBrowser)
                self.horizontalLayout_8.addWidget(self.frame_3)
                self.horizontalLayout_8.setStretch(0, 3)
                self.horizontalLayout_8.setStretch(1, 6)
                self.stackedWidget.addWidget(self.page_AddResenna)
                self.verticalLayout_4.addWidget(self.stackedWidget)
                self.horizontalLayout.addWidget(self.frame_paginas)
                self.verticalLayout_2.addWidget(self.frame_contenido)
                self.verticalLayout_2.setStretch(0, 1)
                self.verticalLayout_2.setStretch(1, 8)
                self.verticalLayout_12.addWidget(self.frame)
                MainWindow.setCentralWidget(self.centralwidget)         
                self.retranslateUi(MainWindow)
                self.stackedWidget.setCurrentIndex(3)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                #cambia el color del texto a blanco lineEdit_UsuarioResea
                self.lineEdit_UsuarioResea.setStyleSheet("color: rgb(255, 255, 255);")
                self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);")

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.pushButton_Mapa.setText(_translate("MainWindow", "MAPA"))
                self.pushButton_Filtrado.setText(_translate("MainWindow", "FILTRADO"))
                self.pushButton_Discoteca.setText(_translate("MainWindow", "AÑADIR DISCOTECA"))
                self.pushButton_Fiesta.setText(_translate("MainWindow", "AÑADIR FIESTA"))
                self.pushButton_Resenna.setText(_translate("MainWindow", "AÑADIR RESEÑA"))
                self.label_6.setText(_translate("MainWindow", "FILTRADO"))
                self.comboBox.setItemText(0, _translate("MainWindow", "ZONA"))
                self.comboBox.setItemText(1, _translate("MainWindow", "NOMBRE"))
                self.comboBox.setItemText(2, _translate("MainWindow", "CALLE"))
                self.comboBox.setItemText(3, _translate("MainWindow", "VALORACIÓN"))
                self.lineEdit_BusquedaFiltrado.setText(_translate("MainWindow", "BÚSQUEDA"))
                self.pushButton_BuscarFiltrado.setText(_translate("MainWindow", "BUSCAR"))
                self.label_9.setText(_translate("MainWindow", "AÑADIR DISCOTECA"))
                self.label_nombreDiscoteca.setText(_translate("MainWindow", "NOMBRE"))
                self.label_zonaDiscoteca.setText(_translate("MainWindow", "ZONA"))
                self.label_calleDiscoteca.setText(_translate("MainWindow", "CALLE"))
                self.label_numeroDiscoteca.setText(_translate("MainWindow", "NÚMERO"))
                self.pushButton_aceptarDiscoteca.setText(_translate("MainWindow", "ACEPTAR"))
                self.label_2.setText(_translate("MainWindow", "AÑADIR FIESTA"))
                self.label_nombreFiesta.setText(_translate("MainWindow", "NOMBRE"))
                self.label_zonaFiesta.setText(_translate("MainWindow", "ZONA"))
                self.label_calleFiesta.setText(_translate("MainWindow", "CALLE"))
                self.label_numeroFiesta.setText(_translate("MainWindow", "NÚMERO"))
                self.pushButton_aceptarFiesta.setText(_translate("MainWindow", "ACEPTAR"))
                self.label.setText(_translate("MainWindow", "ESCRIBIR RESEÑA"))
                
                self.label_4.setText(_translate("MainWindow", "DISCOTECA"))
                self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Escriba aquí su reseña</span></p></body></html>"))
                self.radioButton_1estrella.setText(_translate("MainWindow", "1 ESTRELLA"))
                self.radioButton_2estrellas.setText(_translate("MainWindow", "2 ESTRELLAS"))
                self.radioButton_3estrellas.setText(_translate("MainWindow", "3 ESTRELLAS"))
                self.radioButton_4estrellas.setText(_translate("MainWindow", "4 ESTRELLAS"))
                self.radioButton_5estrellas.setText(_translate("MainWindow", "5 ESTRELLAS"))
                self.pushButton_AddResenna.setText(_translate("MainWindow", "AÑADIR"))
                self.label_5.setText(_translate("MainWindow", "OTRAS RESEÑAS"))







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    