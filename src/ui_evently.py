# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'evently.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################



from re import T
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QInputDialog, QFileDialog, QVBoxLayout, QFrame, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QSize, Qt, QRect, QCoreApplication, QMetaObject
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
import pyglet
import webview
from datetime import date
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import ui_carta

from baseDatosPrueba import datosUsuario, valoracionesUsuario, fiestasUsuario, nombreUsuario, apellidoUsuario, emailUsuario, edadUsuario, filtrarDiscotecas, getItemBaseDatos, getTodosLosDatos, insertarDiscoteca, insertarFiesta, insertarValoracion, variableUsuarioSimp,color, color2


pyglet.font.add_file('fuentes/productSans.ttf')  # ABeeZee



class Ui_MainWindow(object):
    
    filtrado=True
    # BOTON DE AÑADIR DISCOTECA
    def annadirDiscoteca(self):
        insertarDiscoteca(self.lineEdit_nombreDiscoteca.text(), self.lineEdit_calleDiscoteca.text(
        ), self.lineEdit_numeroDiscoteca.text(), self.lineEdit_zonaDiscoteca.text(), 'data')

    # BOTON DE AÑADIR FIESTA
    def annadirFiesta(self):
        self.usuario = datosUsuario('usuario')+'·º·'
        insertarFiesta(self.lineEdit_nombreFiesta.text(), self.lineEdit_calleFiesta.text(
        ), self.lineEdit_numeroFiesta.text(), self.lineEdit_zonaFiesta.text(), self.usuario, 'data')

    # BOTON DE AÑADIR RESEÑA
    contador_valoracion = 0
    def annadirResenna(self):
        # comprueba que radioButton_ esta seleccionado
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
            
        if self.contador_valoracion == 0:    
            resenna = self.textEdit.toPlainText().replace(',', ',@[[')
            usuarioParaSaltoLinea = datosUsuario('usuario')+'·º·'
            fecha_actual = date.today().strftime("%d/%m/%Y")                 
            insertarValoracion(fecha_actual,usuarioParaSaltoLinea, self.comboBoxDisco.currentText(
            ), valoracion, resenna, 'data')
            self.contador_valoracion += 1
        else:
            print("ya has valorado esta discoteca hoy")
            
        #metodo crea botones al filtrar
    def crearBotonesDiscotecasFiltradas(self,numeroFiltro):
        out = filtrarDiscotecas(
                numeroFiltro, self.lineEdit_BusquedaFiltrado.text())
        if(self.filtrado==False):
            for i in self.scrollAreaWidgetContents.children():
                if isinstance(i, QPushButton):
                    i.deleteLater()
            
            self.filtrado=True

        if(self.filtrado):
            for i in range(len(out)):
                self.discotecas_filtradas = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                self.discotecas_filtradas.setObjectName("discotecas_filtradas")
                self.discotecas_filtradas.setText(out[i])
                self.discotecas_filtradas.setFixedHeight(80)
                self.verticalLayout_14.addWidget(self.discotecas_filtradas)
                self.filtrado=False

    # BOTON DE BUSQUEDA

    def busquedaFilter(self):
        print("busqueda filter")
        if self.comboBox.currentText() == "ZONA":
            self.crearBotonesDiscotecasFiltradas(1)

        elif self.comboBox.currentText() == "NOMBRE":
            self.crearBotonesDiscotecasFiltradas(2)
            
        elif self.comboBox.currentText() == "CALLE":
            self.crearBotonesDiscotecasFiltradas(3)
            
        
        elif self.comboBox.currentText() == "VALORACIÓN":
            self.crearBotonesDiscotecasFiltradas(4)
            
            

    def buttonMapa(self):
        self.stackedWidget.setCurrentWidget(self.page_mapa)
        # import mapViewer
        webview.create_window('Evently - Mapa de discotecas', '../mapa.html')
        webview.start()
        print("he seleccionado el boton MAPA")

    def buttonFiltrado(self):
        self.stackedWidget.setCurrentWidget(self.page_filtrado)
        print("he seleccionado el boton FILTRADO")

    def buttonDiscotecas(self):
        self.stackedWidget.setCurrentWidget(self.page_AddDiscoteca)
        print("he selecionado el boton DISCOTECAS")

    def buttonFiesta(self):
        self.stackedWidget.setCurrentWidget(self.page_AddFiesta)
        print("he seleccionado el boton FIESTA")

    def buttonResenna(self):
        self.stackedWidget.setCurrentWidget(self.page_AddResenna)
        out = str(getTodosLosDatos('valoraciones', 'data'))

        out = out.replace('[{', '').replace(']', '').replace(
            '}', '').replace(', ', '').replace('{', '').replace('nombre_discoteca', 'Discoteca').replace('nota', '  Estrellas').replace('texto', '  Comentario').replace(',@[[', ',').replace('·º·', '\n\n').replace('"', '').replace('', '')
        print(out)
        self.textBrowser.setText(out)

        print("he seleccionado el boton RESEÑA")

    def abrir_ventana_carta(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ui_carta.Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def buttonPerfil(self):
        self.stackedWidget.setCurrentWidget(self.page_MiPerfil)
        self.usuario = datosUsuario('usuario')
        self.textBrowser_usuario.setText(self.usuario)
        self.nombre = nombreUsuario('nombre')
        self.textBrowser_nombre.setText(self.nombre)
        self.apellido = apellidoUsuario('apellido')
        self.textBrowser_apellido.setText(self.apellido)
        self.email = emailUsuario('email')
        self.textBrowser_email.setText(self.email)
        self.edad = edadUsuario('edad')
        self.textBrowser_edad.setText(str(self.edad))
        print("he seleccionado el boton MI PERFIL")
        
    def buttonMisResennas(self):
        self.usr = datosUsuario('usuario')
        print(self.usr)
        self.mis_resennas = str(valoracionesUsuario(self.usr))
        self.textBrowser_MiPerfil.setText(self.mis_resennas)
        
    def buttonMisFiestas(self):
        self.usr = datosUsuario('usuario')
        self.mis_fiestas = str(fiestasUsuario(self.usr))
        self.textBrowser_MiPerfil.setText(self.mis_fiestas)



    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 533)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(36, 31, 49);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 42))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
                                            "	background-color:"+color+";\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton{\n"
                                            "	background-color: #000000ff;\n"
                                            "	border-radius: 20px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton: hover{\n"
                                            "	background-color: rgb(61, 61, 61);\n"
                                            "	border-radius: 20px\n"
                                            "}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_Menu = QPushButton(self.frame_superior)
        self.pushButton_Menu.setObjectName(u"pushButton_Menu")
        self.pushButton_Menu.setMinimumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u"../im\u00e1genes/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Menu.setIcon(icon)
        self.pushButton_Menu.setIconSize(QSize(195, 38))
        self.pushButton_Menu.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.pushButton_Menu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_Minimizar = QPushButton(self.frame_superior)
        self.pushButton_Minimizar.setObjectName(u"pushButton_Minimizar")
        self.pushButton_Minimizar.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u"../im\u00e1genes/dentro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Minimizar.setIcon(icon1)
        self.pushButton_Minimizar.setIconSize(QSize(38, 38))
        self.pushButton_Minimizar.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.pushButton_Minimizar)

        self.pushButton_Aumentar = QPushButton(self.frame_superior)
        self.pushButton_Aumentar.setObjectName(u"pushButton_Aumentar")
        self.pushButton_Aumentar.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"../im\u00e1genes/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Aumentar.setIcon(icon2)
        self.pushButton_Aumentar.setIconSize(QSize(38, 38))
        self.pushButton_Aumentar.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.pushButton_Aumentar)

        self.pushButton_Cerrar = QPushButton(self.frame_superior)
        self.pushButton_Cerrar.setObjectName(u"pushButton_Cerrar")
        self.pushButton_Cerrar.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u"../im\u00e1genes/1828774.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Cerrar.setIcon(icon3)
        self.pushButton_Cerrar.setIconSize(QSize(38, 38))
        self.pushButton_Cerrar.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.pushButton_Cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_control = QFrame(self.frame_contenido)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(200, 0))
        self.frame_control.setMaximumSize(QSize(0, 16777215))
        self.frame_control.setStyleSheet(u"QFrame{\n"
                                            "	background-color:"+color+";\n"
                                            "}\n"
                                            "\n"
                                            " QPushButton{\n"
                                            "	background-color: rgb(0, 0, 0);\n"
                                            "	border-top-left-radius: 20px;\n"
                                            "	border-bottom-left-radius: 20px;\n"
                                            "	color: rgb(255,255,255);\n"
                                            "	font: 77 12pt \"Arial Black\";\n"
                                            "}\n"
                                            "\n"
                                            " QPushButton:hover{\n"
                                            "	background-color: white;\n"
                                            "	border-top-left-radius: 20px;\n"
                                            "	border-bottom-left-radius: 20px;\n"
                                            "	color: rgb(0,0,0);\n"
                                            "	font: 77 12pt \"Arial Black\";\n"
                                            "}")
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.frame_control.setObjectName("frame_control")
        self.verticalLayout_3 = QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_Mapa = QPushButton(self.frame_control)
        self.pushButton_Mapa.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Mapa.clicked.connect(self.buttonMapa)
        self.pushButton_Mapa.setObjectName(u"pushButton_Mapa")
        self.pushButton_Mapa.setEnabled(True)

        self.verticalLayout_3.addWidget(self.pushButton_Mapa)

        self.pushButton_Filtrado = QPushButton(self.frame_control)
        self.pushButton_Filtrado.setObjectName("pushButton_Filtrado")
        self.pushButton_Filtrado.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Filtrado.clicked.connect(self.buttonFiltrado)
        self.pushButton_Filtrado.setEnabled(True)

        self.verticalLayout_3.addWidget(self.pushButton_Filtrado)

        self.pushButton_Discoteca = QPushButton(self.frame_control)
        self.pushButton_Discoteca.setObjectName(u"pushButton_Discoteca")
        self.pushButton_Discoteca.clicked.connect(self.buttonDiscotecas)
        self.pushButton_Discoteca.setEnabled(True)
        self.pushButton_Discoteca.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.pushButton_Discoteca)

        self.pushButton_Fiesta = QPushButton(self.frame_control)
        self.pushButton_Fiesta.setObjectName(u"pushButton_Fiesta")
        self.pushButton_Fiesta.clicked.connect(self.buttonFiesta)
        self.pushButton_Fiesta.setEnabled(True)
        self.pushButton_Fiesta.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.pushButton_Fiesta)

        self.pushButton_Resenna = QPushButton(self.frame_control)
        self.pushButton_Resenna.setObjectName(u"pushButton_Resenna")
        self.pushButton_Resenna.clicked.connect(self.buttonResenna)
        self.pushButton_Resenna.setEnabled(True)
        self.pushButton_Resenna.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.pushButton_Resenna)

        self.pushButton_MiPerfil = QPushButton(self.frame_control)
        self.pushButton_MiPerfil.setObjectName(u"pushButton_MiPerfil")
        self.pushButton_MiPerfil.clicked.connect(self.buttonPerfil)
        self.pushButton_MiPerfil.setEnabled(True)
        self.pushButton_MiPerfil.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.pushButton_MiPerfil)

        self.pushButton_Carta = QPushButton(self.frame_control, clicked = lambda: self.abrir_ventana_carta())
        self.pushButton_Carta.setObjectName(u"pushButton_Carta")
        #self.pushButton_Carta.clicked.connect(self.buttonCarta)
        self.pushButton_Carta.setText('CARTA')
        self.pushButton_Carta.setEnabled(True)
        self.pushButton_Carta.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.pushButton_Carta)


        self.horizontalLayout.addWidget(self.frame_control)

        self.frame_paginas = QFrame(self.frame_contenido)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setStyleSheet(u"QFrame{\n"
                                            "	background-color:"+color+";\n"
                                            "}\n"
                                            "\n"
                                            "QLabel{\n"
                                            "	font: 87 12pt \"Arial Black\";	\n"
                                            "	background-color:#000000ff;\n"
                                            "	color:"+color+";\n"
                                            "	border: 0px solid #14C8DC;\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit{\n"
                                            "	border:0px;\n"
                                            "	color: rbg(255,255,255);\n"
                                            "	border-bottom: 2px solid rgb(0,0,0);\n"
                                            "	font: 75 12pt \"Times New Roman\";\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton{\n"
                                            "	background-color: rgb(0, 0,0);\n"
                                            "	border-radius: 15px;\n"
                                            "	color: rgb(255,255,255);\n"
                                            "	font : 77 10pt \"Arial Black\";\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "	background-color:"+color+";\n"
                                            "	border-radius: 15px;\n"
                                            "	color: rgb(0,0,0);\n"
                                            "	font: 77 10pt \"Arial Black\";\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "")
        self.frame_paginas.setFrameShape(QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Raised)
        self.frame_paginas.setObjectName("frame_paginas")
        self.verticalLayout_4 = QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget = QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        
        """PÁGINA DEL MAPA"""
        self.page_mapa = QWidget()
        self.page_mapa.setObjectName(u"page_mapa")
        self.stackedWidget.addWidget(self.page_mapa)
        
        """PÁGINA DEL FILTRADO"""
        self.page_filtrado = QtWidgets.QWidget()
        self.page_filtrado.setObjectName("page_filtrado")
        self.verticalLayout_13 = QVBoxLayout(self.page_filtrado)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QLabel(self.page_filtrado)
        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_6)

        self.comboBox = QComboBox(self.page_filtrado)
        self.comboBox.setStyleSheet("color:"+color+";\n"
                                     "background-color: #000000ff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.verticalLayout_13.addWidget(self.comboBox)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_BusquedaFiltrado = QLineEdit(self.page_filtrado)
        self.lineEdit_BusquedaFiltrado.setObjectName(u"lineEdit_BusquedaFiltrado")
        self.lineEdit_BusquedaFiltrado.setStyleSheet(u"color:"+color+";")

        self.horizontalLayout_9.addWidget(self.lineEdit_BusquedaFiltrado)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.pushButton_BuscarFiltrado = QPushButton(self.page_filtrado)
        self.pushButton_BuscarFiltrado.setObjectName("pushButton_BuscarFiltrado")
        self.pushButton_BuscarFiltrado.clicked.connect(self.busquedaFilter)

        self.horizontalLayout_9.addWidget(self.pushButton_BuscarFiltrado)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        
        #añade para poder añadir un boton por cada discoteca, y poder desplazarte con un scroll bar por los botones
        self.scrollArea = QtWidgets.QScrollArea(self.page_filtrado)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_13.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_filtrado)
        
        
        """PÁGINA DE DISCOTECAS"""
        self.page_AddDiscoteca = QWidget()
        self.page_AddDiscoteca.setObjectName(u"page_AddDiscoteca")
        self.verticalLayout = QVBoxLayout(self.page_AddDiscoteca)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.page_AddDiscoteca)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)

        self.verticalLayout.addWidget(self.label_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_nombreDiscoteca = QLabel(self.page_AddDiscoteca)
        self.label_nombreDiscoteca.setObjectName(u"label_nombreDiscoteca")
        self.label_nombreDiscoteca.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_nombreDiscoteca)

        self.label_zonaDiscoteca = QLabel(self.page_AddDiscoteca)
        self.label_zonaDiscoteca.setObjectName(u"label_zonaDiscoteca")
        self.label_zonaDiscoteca.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_zonaDiscoteca)

        self.label_calleDiscoteca = QLabel(self.page_AddDiscoteca)
        self.label_calleDiscoteca.setObjectName(u"label_calleDiscoteca")
        self.label_calleDiscoteca.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_calleDiscoteca)

        self.label_numeroDiscoteca = QLabel(self.page_AddDiscoteca)
        self.label_numeroDiscoteca.setObjectName(u"label_numeroDiscoteca")
        self.label_numeroDiscoteca.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_numeroDiscoteca)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(60)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_nombreDiscoteca = QLineEdit(self.page_AddDiscoteca)
        self.lineEdit_nombreDiscoteca.setText("")
        self.lineEdit_nombreDiscoteca.setObjectName(u"lineEdit_nombreDiscoteca")
        self.lineEdit_nombreDiscoteca.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.lineEdit_nombreDiscoteca)

        self.lineEdit_zonaDiscoteca = QLineEdit(self.page_AddDiscoteca)
        self.lineEdit_zonaDiscoteca.setObjectName(u"lineEdit_zonaDiscoteca")
        self.lineEdit_zonaDiscoteca.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.lineEdit_zonaDiscoteca)

        self.lineEdit_calleDiscoteca = QLineEdit(self.page_AddDiscoteca)
        self.lineEdit_calleDiscoteca.setObjectName(u"lineEdit_calleDiscoteca")
        self.lineEdit_calleDiscoteca.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_calleDiscoteca.setText("")

        self.verticalLayout_6.addWidget(self.lineEdit_calleDiscoteca)

        self.lineEdit_numeroDiscoteca = QLineEdit(self.page_AddDiscoteca)
        self.lineEdit_numeroDiscoteca.setObjectName(u"lineEdit_numeroDiscoteca")
        self.lineEdit_numeroDiscoteca.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.lineEdit_numeroDiscoteca)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pushButton_aceptarDiscoteca = QPushButton(self.page_AddDiscoteca)
        self.pushButton_aceptarDiscoteca.setObjectName(u"pushButton_aceptarDiscoteca")
        self.pushButton_aceptarDiscoteca.setMaximumSize(QSize(80, 16777215))
        self.pushButton_aceptarDiscoteca.clicked.connect(self.annadirDiscoteca)

        self.horizontalLayout_5.addWidget(self.pushButton_aceptarDiscoteca)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 8)
        self.stackedWidget.addWidget(self.page_AddDiscoteca)
        
        
        """PÁGINA DE FIESTAS"""
        self.page_AddFiesta = QWidget()
        self.page_AddFiesta.setObjectName(u"page_AddFiesta")
        self.verticalLayout_9 = QVBoxLayout(self.page_AddFiesta)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.page_AddFiesta)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_nombreFiesta = QLabel(self.page_AddFiesta)
        self.label_nombreFiesta.setObjectName(u"label_nombreFiesta")
        self.label_nombreFiesta.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_nombreFiesta)

        self.label_zonaFiesta = QLabel(self.page_AddFiesta)
        self.label_zonaFiesta.setObjectName(u"label_zonaFiesta")
        self.label_zonaFiesta.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_zonaFiesta)

        self.label_calleFiesta = QLabel(self.page_AddFiesta)
        self.label_calleFiesta.setObjectName(u"label_calleFiesta")
        self.label_calleFiesta.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_calleFiesta)

        self.label_numeroFiesta = QLabel(self.page_AddFiesta)
        self.label_numeroFiesta.setObjectName(u"label_numeroFiesta")
        self.label_numeroFiesta.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_numeroFiesta)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(60)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lineEdit_nombreFiesta = QLineEdit(self.page_AddFiesta)
        self.lineEdit_nombreFiesta.setObjectName(u"lineEdit_nombreFiesta")
        self.lineEdit_nombreFiesta.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.lineEdit_nombreFiesta)

        self.lineEdit_zonaFiesta = QLineEdit(self.page_AddFiesta)
        self.lineEdit_zonaFiesta.setObjectName(u"lineEdit_zonaFiesta")
        self.lineEdit_zonaFiesta.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_zonaFiesta.setText("")

        self.verticalLayout_8.addWidget(self.lineEdit_zonaFiesta)

        self.lineEdit_calleFiesta = QLineEdit(self.page_AddFiesta)
        self.lineEdit_calleFiesta.setObjectName(u"lineEdit_calleFiesta")
        self.lineEdit_calleFiesta.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.lineEdit_calleFiesta)

        self.lineEdit_numeroFiesta = QLineEdit(self.page_AddFiesta)
        self.lineEdit_numeroFiesta.setObjectName(u"lineEdit_numeroFiesta")
        self.lineEdit_numeroFiesta.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.lineEdit_numeroFiesta)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.pushButton_aceptarFiesta = QPushButton(self.page_AddFiesta)
        self.pushButton_aceptarFiesta.setObjectName(u"pushButton_aceptarFiesta")
        self.pushButton_aceptarFiesta.clicked.connect(self.annadirFiesta)

        self.horizontalLayout_7.addWidget(self.pushButton_aceptarFiesta)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(2, 8)
        self.stackedWidget.addWidget(self.page_AddFiesta)
        
        """PÁGINA DE RESEÑAS"""
        self.page_AddResenna = QWidget()
        self.page_AddResenna.setObjectName(u"page_AddResenna")
        self.page_AddResenna.setStyleSheet(u"QFrame{\n"
                                            "	background-color: #000000ff;\n"
                                            "}\n"
                                            "\n"
                                            "QLabel{\n"
                                            "	font: 87 12pt \"Arial Black\";	\n"
                                            "	background-color:#000000ff;\n"
                                            "	color:"+color+";\n"
                                            "	border: 0px solid #14C8DC;\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit{\n"
                                            "	border:0px;\n"
                                            "	color: rbg(255,255,255);\n"
                                            "	border-bottom: 2px solid rgb(0,0,0);\n"
                                            "	font: 75 12pt \"Times New Roman\";\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton{\n"
                                            "	background-color: rgb(0, 0,0);\n"
                                            "	border-radius: 15px;\n"
                                            "	color: rgb(255,255,255);\n"
                                            "	font : 77 10pt \"Arial Black\";\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover{\n"
                                            "	background-color:"+color+";\n"
                                            "	border-radius: 15px;\n"
                                            "	color: rgb(0,0,0);\n"
                                            "	font: 77 10pt \"Arial Black\";\n"
                                            "}\n"
                                            "\n"
                                            "QRadioButton{\n"
                                            "	background-color: "+color+";\n"
                                            "	font: 87 12pt \"Arial Black\";	\n"
                                            "}")
        self.horizontalLayout_8 = QHBoxLayout(self.page_AddResenna)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_AddResenna)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)

        self.lineEdit_UsuarioResea = QLineEdit(self.frame_2)
        self.lineEdit_UsuarioResea.setObjectName(u"lineEdit_UsuarioResea")

        self.verticalLayout_10.addWidget(self.lineEdit_UsuarioResea)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_4)

        #self.lineEdit_2 = QLineEdit(self.frame_2)
        #self.lineEdit_2.setObjectName(u"lineEdit_2")
        #self.verticalLayout_10.addWidget(self.lineEdit_2)
        
        # change the lineEdit2 to a comboBox
        self.comboBoxDisco = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxDisco.setObjectName("comboBoxDisco")
        self.verticalLayout_10.addWidget(self.comboBoxDisco)
        self.comboBoxDisco.setStyleSheet("color:  "+color+";\n"
                                         "background-color: #000000ff;")
        discotecas = getItemBaseDatos('discotecas', 'nombre', 'data')
        for i in discotecas:
            self.comboBoxDisco.addItem(i)


        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_10.addWidget(self.textEdit)

        self.radioButton_1estrella = QRadioButton(self.frame_2)
        self.radioButton_1estrella.setObjectName(u"radioButton_1estrella")

        self.verticalLayout_10.addWidget(self.radioButton_1estrella)

        self.radioButton_2estrellas = QRadioButton(self.frame_2)
        self.radioButton_2estrellas.setObjectName(u"radioButton_2estrellas")

        self.verticalLayout_10.addWidget(self.radioButton_2estrellas)

        self.radioButton_3estrellas = QRadioButton(self.frame_2)
        self.radioButton_3estrellas.setObjectName(u"radioButton_3estrellas")

        self.verticalLayout_10.addWidget(self.radioButton_3estrellas)

        self.radioButton_4estrellas = QRadioButton(self.frame_2)
        self.radioButton_4estrellas.setObjectName(u"radioButton_4estrellas")

        self.verticalLayout_10.addWidget(self.radioButton_4estrellas)

        self.radioButton_5estrellas = QRadioButton(self.frame_2)
        self.radioButton_5estrellas.setObjectName(u"radioButton_5estrellas")

        self.verticalLayout_10.addWidget(self.radioButton_5estrellas)

        self.pushButton_AddResenna = QPushButton(self.frame_2)
        self.pushButton_AddResenna.setObjectName(u"pushButton_AddResenna")
        self.pushButton_AddResenna.clicked.connect(self.annadirResenna)

        self.verticalLayout_10.addWidget(self.pushButton_AddResenna)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_AddResenna)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_5)

        self.textBrowser = QTextBrowser(self.frame_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.textBrowser)


        self.horizontalLayout_8.addWidget(self.frame_3)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 6)
        self.stackedWidget.addWidget(self.page_AddResenna)
        
        """PÁGINA MI PERFIL"""
        self.page_MiPerfil = QWidget()
        self.page_MiPerfil.setObjectName(u"page_MiPerfil")
        self.label_7 = QLabel(self.page_MiPerfil)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QtCore.QRect(6, 10, 591, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.page_MiPerfil)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 40, 111, 141))
        self.verticalLayout_14 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_usuario = QLabel(self.verticalLayoutWidget)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.label_usuario)

        self.label_nombre = QLabel(self.verticalLayoutWidget)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.label_nombre)

        self.label_apellido = QLabel(self.verticalLayoutWidget)
        self.label_apellido.setObjectName(u"label_apellido")
        self.label_apellido.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.label_apellido)

        self.textBrowser_usuario = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_usuario.setObjectName(u"textBrowser_usuario")
        self.textBrowser_usuario.setGeometry(QtCore.QRect(130, 50, 151, 31))
        self.textBrowser_usuario.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.textBrowser_nombre = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_nombre.setObjectName(u"textBrowser_nombre")
        self.textBrowser_nombre.setGeometry(QRect(130, 100, 151, 31))
        self.textBrowser_nombre.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.textBrowser_apellido = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_apellido.setObjectName(u"textBrowser_apellido")
        self.textBrowser_apellido.setGeometry(QRect(130, 150, 151, 31))
        self.textBrowser_apellido.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.verticalLayoutWidget_2 = QWidget(self.page_MiPerfil)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(290, 40, 91, 141))
        self.verticalLayout_15 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_email = QLabel(self.verticalLayoutWidget_2)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.label_email)

        self.label_edad = QLabel(self.verticalLayoutWidget_2)
        self.label_edad.setObjectName(u"label_edad")
        self.label_edad.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.label_edad)

        self.textBrowser_email = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_email.setObjectName(u"textBrowser_email")
        self.textBrowser_email.setGeometry(QRect(390, 60, 201, 31))
        self.textBrowser_email.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.textBrowser_edad = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_edad.setObjectName(u"textBrowser_edad")
        self.textBrowser_edad.setGeometry(QRect(390, 130, 201, 31))
        self.textBrowser_edad.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.textBrowser_MiPerfil = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_MiPerfil.setObjectName(u"textBrowser_MiPerfil")
        self.textBrowser_MiPerfil.setGeometry(QRect(10, 230, 581, 221))
        self.textBrowser_MiPerfil.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.pushButton_MisResennas = QPushButton(self.page_MiPerfil)
        self.pushButton_MisResennas.setObjectName(u"pushButton_MisResennas")
        self.pushButton_MisResennas.clicked.connect(self.buttonMisResennas)
        self.pushButton_MisResennas.setGeometry(QRect(190, 200, 111, 23))
        self.pushButton_MisFiestas = QPushButton(self.page_MiPerfil)
        self.pushButton_MisFiestas.setObjectName(u"pushButton_MisFiestas")
        self.pushButton_MisFiestas.clicked.connect(self.buttonMisFiestas)
        self.pushButton_MisFiestas.setGeometry(QRect(310, 200, 101, 23))
        self.stackedWidget.addWidget(self.page_MiPerfil)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_paginas)


        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout_12.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Menu.setText("")
        self.pushButton_Minimizar.setText("")
        self.pushButton_Aumentar.setText("")
        self.pushButton_Cerrar.setText("")
        self.pushButton_Mapa.setText(QCoreApplication.translate("MainWindow", u"MAPA", None))
        self.pushButton_Filtrado.setText(QCoreApplication.translate("MainWindow", u"FILTRADO", None))
        self.pushButton_Discoteca.setText(QCoreApplication.translate("MainWindow", u"A\u00d1ADIR DISCOTECA", None))
        self.pushButton_Fiesta.setText(QCoreApplication.translate("MainWindow", u"A\u00d1ADIR FIESTA", None))
        self.pushButton_Resenna.setText(QCoreApplication.translate("MainWindow", u"A\u00d1ADIR RESE\u00d1A", None))
        self.pushButton_MiPerfil.setText(QCoreApplication.translate("MainWindow", u"MI PERFIL", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"FILTRADO", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ZONA", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CALLE", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"VALORACI\u00d3N", None))

        self.lineEdit_BusquedaFiltrado.setText(QCoreApplication.translate("MainWindow", u"B\u00daSQUEDA", None))
        self.pushButton_BuscarFiltrado.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"A\u00d1ADIR DISCOTECA", None))
        self.label_nombreDiscoteca.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_zonaDiscoteca.setText(QCoreApplication.translate("MainWindow", u"ZONA", None))
        self.label_calleDiscoteca.setText(QCoreApplication.translate("MainWindow", u"CALLE", None))
        self.label_numeroDiscoteca.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.lineEdit_nombreDiscoteca.setText("")
        self.lineEdit_calleDiscoteca.setText("")
        self.pushButton_aceptarDiscoteca.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"A\u00d1ADIR FIESTA", None))
        self.label_nombreFiesta.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.label_zonaFiesta.setText(QCoreApplication.translate("MainWindow", u"ZONA", None))
        self.label_calleFiesta.setText(QCoreApplication.translate("MainWindow", u"CALLE", None))
        self.label_numeroFiesta.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.lineEdit_zonaFiesta.setText("")
        self.pushButton_aceptarFiesta.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ESCRIBIR RESE\u00d1A", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"USUARIO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DISCOTECA", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:11pt; font-style:italic;\">Escriba aqu\u00ed su rese\u00f1a</span></p></body></html>", None))
        self.radioButton_1estrella.setText(QCoreApplication.translate("MainWindow", u"1 ESTRELLA", None))
        self.radioButton_2estrellas.setText(QCoreApplication.translate("MainWindow", u"2 ESTRELLAS", None))
        self.radioButton_3estrellas.setText(QCoreApplication.translate("MainWindow", u"3 ESTRELLAS", None))
        self.radioButton_4estrellas.setText(QCoreApplication.translate("MainWindow", u"4 ESTRELLAS", None))
        self.radioButton_5estrellas.setText(QCoreApplication.translate("MainWindow", u"5 ESTRELLAS", None))
        self.pushButton_AddResenna.setText(QCoreApplication.translate("MainWindow", u"A\u00d1ADIR", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"OTRAS RESE\u00d1AS", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MI PERFIL", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"USUARIO:", None))
        self.label_nombre.setText(QCoreApplication.translate("MainWindow", u"NOMBRE:", None))
        self.label_apellido.setText(QCoreApplication.translate("MainWindow", u"APELLIDO:", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"EMAIL:", None))
        self.label_edad.setText(QCoreApplication.translate("MainWindow", u"EDAD:", None))
        self.pushButton_MisResennas.setText(QCoreApplication.translate("MainWindow", u"Mis rese\u00f1as", None))
        self.pushButton_MisFiestas.setText(QCoreApplication.translate("MainWindow", u"Mis fiestas", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())