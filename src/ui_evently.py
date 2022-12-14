from re import T
import sys
import threading
import time
import cv2
from urllib.request import urlopen
import numpy as np
import imutils
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QInputDialog, QFileDialog, QVBoxLayout, QFrame, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QSize, Qt, QRect, QCoreApplication, QMetaObject
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QImage
import pyglet
import webview
from datetime import date
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import ui_carta
from datetime import timedelta

from baseDatosPrueba import datosUsuario, getDatosElementoConcreto, getTodosLosDatos, valoracionesUsuario, fiestasUsuario, nombreUsuario, apellidoUsuario, emailUsuario, edadUsuario, filtrarDiscotecas, getItemBaseDatos, insertarMensaje, insertarDiscoteca, insertarFiesta, insertarValoracion, mostrar_carta, color, color2

from Interfaz_Imagenes import subir_foto, ver_mis_fotos

pyglet.font.add_file('fuentes/productSans.ttf')


class Ui_MainWindow(QMainWindow):
    filtrado = True
    busquedaUsuarios = True
    tablaChatCreada = False
    botonesDiscotecas = {}
    botonesChatUsuarios = {}
    botonesBusquedaUsuarios = {}
    usuarioBuscado = ''
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

        fecha_actual = date.today().strftime("%d/%m/%Y")
        resenna = self.textEdit.toPlainText()
        usuarioParaSaltoLinea = datosUsuario('usuario')+'·º·'
        insertarValoracion(fecha_actual, usuarioParaSaltoLinea, self.comboBoxDisco.currentText(
        ), valoracion, resenna, 'data')
        self.buttonResenna()

    def borrarBotonesFiltrado(self):
        for i in self.scrollAreaWidgetContents.children():
            if isinstance(i, QPushButton):
                i.deleteLater()

    def borrarBotonesChatUsuarios(self):
        # comprueba que existe tabla de chat
        if(self.tablaChatCreada):
            self.tablaChat.deleteLater()
            self.textEditChat.deleteLater()
            self.botonEnviar.deleteLater()
            self.tablaChatCreada = False
        else:
            for i in self.scrollAreaWidgetContents2.children():
                if isinstance(i, QPushButton):
                    i.deleteLater()

    def borrarBotonesBusquedaUsuarios(self):
        for i in self.scrollAreaWidgetContents3.children():
            if isinstance(i, QPushButton):
                i.deleteLater()

    def borrarTextFiltrado(self):
        self.textEditCarta.clear()
        self.textEditCarta.hide()

    def borrarTablaResennas(self):
        self.tablaResennas.deleteLater()

        # metodo crea botones al filtrar

    def crearBotonesDiscotecasFiltradas(self, numeroFiltro):
        out = filtrarDiscotecas(
            numeroFiltro, self.lineEdit_BusquedaFiltrado.text())
        if(self.filtrado == False):
            self.borrarBotonesFiltrado()
            self.filtrado = True

        if(self.filtrado):
            for i in range(len(out)):
                self.botonesDiscotecas[out[i]] = QtWidgets.QPushButton(
                    self.scrollAreaWidgetContents)
                self.botonesDiscotecas[out[i]].setObjectName(out[i])
                self.botonesDiscotecas[out[i]].setText(out[i])
                self.botonesDiscotecas[out[i]].setFixedHeight(80)
                self.verticalLayout_14.addWidget(
                    self.botonesDiscotecas[out[i]])
                self.botonesDiscotecas[out[i]].clicked.connect(
                    lambda checked, out=out, i=i: self.imprimirNombreDiscoteca(out[i]))
                self.filtrado = False

    def imprimirNombreDiscoteca(self, nombreDiscoteca):
        self.borrarBotonesFiltrado()
        self.textEditCarta = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditCarta.setObjectName("textEditCarta")
        self.textEditCarta.setReadOnly(True)
        self.textEditCarta.setFixedHeight(500)
        self.textEditCarta.setStyleSheet("color:  "+color+";\n")
        self.verticalLayout_14.addWidget(self.textEditCarta)
        self.textEditCarta.setText(mostrar_carta(
            'carta', nombreDiscoteca, 'data'))

    def crearBotonesChatUsuarios(self):
        out = filtrarDiscotecas(5, self.lineEdit_BusquedaChat.text())
        if(self.busquedaUsuarios == False):
            self.borrarBotonesChatUsuarios()
            self.busquedaUsuarios = True

        if(self.busquedaUsuarios):
            for i in range(len(out)):
                self.botonesChatUsuarios[out[i]] = QtWidgets.QPushButton(
                    self.scrollAreaWidgetContents2)
                self.botonesChatUsuarios[out[i]].setObjectName(out[i])
                self.botonesChatUsuarios[out[i]].setText(out[i])
                self.botonesChatUsuarios[out[i]].setFixedHeight(80)
                self.verticalLayout_14Chat.addWidget(
                    self.botonesChatUsuarios[out[i]])
                self.botonesChatUsuarios[out[i]].clicked.connect(
                    lambda checked, out=out, i=i: self.crearChat(out[i], ''))
                self.busquedaUsuarios = False

    def crearChat(self, nombreUsuario, textoMensaje):
        self.borrarBotonesChatUsuarios()
        self.tablaChatCreada = True
        self.tablaChat = QTableWidget()

        self.tablaChat.setObjectName("tablaChat")
        self.tablaChat.setRowCount(0)
        self.tablaChat.setColumnCount(2)
        self.tablaChat.setStyleSheet(
            "QHeaderView::section { font-size: 12pt; }")
        self.verticalLayout_14Chat.addWidget(self.tablaChat)
        # creamos el textEdit y el boton circular
        self.textEditChat = QtWidgets.QTextEdit(self.scrollAreaWidgetContents2)
        self.textEditChat.setObjectName("textEditChat")
        self.textEditChat.setFixedHeight(80)

        self.textEditChat.setStyleSheet("color:  "+color+";\n")
        # color del fondo blanco con poca opacidad
        self.textEditChat.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0.8);")
        self.textEditChat.setText(textoMensaje)
        # set focus al final del texto
        self.textEditChat.setFocus()

        self.horizontalLayout_15Chat = QtWidgets.QHBoxLayout()
        self.tablaChat.setHorizontalHeaderLabels([nombreUsuario, "YO"])
        self.tablaChat.horizontalHeader().setFont(
            QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        self.botonEnviar = QtWidgets.QPushButton(
            self.scrollAreaWidgetContents2)
        self.botonEnviar.setObjectName("botonEnviar")
        self.botonEnviar.setFixedHeight(80)
        self.textEditChat.setFixedHeight(80)
        self.botonEnviar.setStyleSheet("color:  "+color+";\n")
        self.botonEnviar.setIcon(QtGui.QIcon("imágenes/enviar.png"))
        self.botonEnviar.setIconSize(QtCore.QSize(60, 60))
        self.botonEnviar.clicked.connect(lambda checked: self.enviarMensaje(
            self.textEditChat, chat, usuario2, usuario1))
        self.horizontalLayout_15Chat.addWidget(self.textEditChat)
        self.horizontalLayout_15Chat.addWidget(self.botonEnviar)
        self.verticalLayout_14Chat.addLayout(self.horizontalLayout_15Chat)

        usuario2 = datosUsuario('usuario')

        usuario1 = nombreUsuario
        if usuario1 < usuario2:
            chat = usuario1+usuario2
        else:
            chat = usuario2+usuario1

        rutaChat = 'chats/'+chat
        chatsAnteriores = getTodosLosDatos(rutaChat, 'data')
        # comprueba si chatsAnteriores es una lista vacia, si lo es añade un mensaje de bienvenida
        if chatsAnteriores == []:
            insertarMensaje(
                usuario2, 'Hola, quieres usar Evently conmigo :)', chat, 'data')
        else:
            for chatAnterior in chatsAnteriores:
                if chatAnterior['usuario'] == usuario1:
                    fila = self.tablaChat.rowCount()
                    self.tablaChat.insertRow(fila)
                    self.tablaChat.setItem(
                        fila, 0, QTableWidgetItem(chatAnterior['mensaje']))
                    self.tablaChat.setItem(fila, 1, QTableWidgetItem(''))
                    self.tablaChat.item(fila, 0).setTextAlignment(
                        QtCore.Qt.AlignVCenter)

                else:
                    fila = self.tablaChat.rowCount()
                    self.tablaChat.insertRow(fila)
                    self.tablaChat.setItem(fila, 0, QTableWidgetItem(''))
                    self.tablaChat.setItem(
                        fila, 1, QTableWidgetItem(chatAnterior['mensaje']))
                    # cada elemento alinea el texto a la derecha y centrado
                    self.tablaChat.item(fila, 1).setTextAlignment(
                        QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # recorrer la tabla, si una celda no tiene texto el color del fondeo es color2, si tiene texto el color del fondo es color
        for i in range(self.tablaChat.rowCount()):
            for j in range(self.tablaChat.columnCount()):
                if self.tablaChat.item(i, j).text() == '':
                    self.tablaChat.item(i, j).setBackground(
                        QtGui.QColor(color2))

                else:
                    self.tablaChat.item(i, j).setBackground(
                        QtGui.QColor(color))

        self.tablaChat.horizontalHeader().setStretchLastSection(True)

        self.tablaChat.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.tablaChat.horizontalHeader().setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)
        self.tablaChat.verticalHeader().setVisible(False)

        # esperar10 seg y si acaba el tiempo se actualiza el chat, pero si se cambai el text edit se resetea el tiempo
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.crearChat(
            usuario1, self.textEditChat.toPlainText()))
        self.timer.start(5000)
        self.textEditChat.textChanged.connect(self.timer.stop)
        self.pushButton_BuscarChat.clicked.connect(self.timer.stop)
        self.pushButton_Mapa.clicked.connect(self.timer.stop)
        self.pushButton_Filtrado.clicked.connect(self.timer.stop)
        self.pushButton_Discoteca.clicked.connect(self.timer.stop)
        self.pushButton_Fiesta.clicked.connect(self.timer.stop)
        self.pushButton_Resenna.clicked.connect(self.timer.stop)
        self.pushButton_MiPerfil.clicked.connect(self.timer.stop)

        self.textEditChat.textChanged.connect(lambda: self.timer.start(5000))

    def enviarMensaje(self, mensaje, chat, usuario2, usuario1):
        rutaChat = 'chats/'+chat
        if(mensaje.toPlainText() != ''):
            insertarMensaje(usuario2, mensaje.toPlainText(), chat, 'data')
            self.crearChat(usuario1, '')
        else:
            self.crearChat(usuario1, '')

    def crearBotonesUsuarios(self):
        out = filtrarDiscotecas(5, self.lineEdit_BusquedaUsuarios.text())
        if(self.busquedaUsuarios == False):
            self. botonesBusquedaUsuarios()
            self.busquedaUsuarios = True

        if(self.busquedaUsuarios):
            for i in range(len(out)):
                self. botonesBusquedaUsuarios[out[i]] = QtWidgets.QPushButton(
                    self.scrollAreaWidgetContents2)
                self. botonesBusquedaUsuarios[out[i]].setObjectName(out[i])
                self. botonesBusquedaUsuarios[out[i]].setText(out[i])
                self. botonesBusquedaUsuarios[out[i]].setFixedHeight(80)
                self.verticalLayout_14Usuarios.addWidget(
                    self. botonesBusquedaUsuarios[out[i]])
                self. botonesBusquedaUsuarios[out[i]].clicked.connect(
                    lambda checked, out=out, i=i: self.buttonPerfil2(out[i]))
                self.busquedaUsuarios = False

    def busquedaFilter(self):
        # comprueba si existe textEditCarta y lo borra
        if hasattr(self, 'textEditCarta'):
            self.borrarTextFiltrado()

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
        webview.create_window('Evently - Mapa de discotecas', '../mapa.html')
        webview.start()

    def buttonFiltrado(self):
        self.stackedWidget.setCurrentWidget(self.page_filtrado)

    def buttonDiscotecas(self):
        self.stackedWidget.setCurrentWidget(self.page_AddDiscoteca)

    def buttonFiesta(self):
        self.stackedWidget.setCurrentWidget(self.page_AddFiesta)

    def buttonResenna(self):
        # comprueba si existe tablaResenna y la borra
        if hasattr(self, 'tablaResennas'):
            self.borrarTablaResennas()

        self.stackedWidget.setCurrentWidget(self.page_AddResenna)
        # crear una tabla con las valoraciones de todas las discotecas haciendo colmnas de fecha, usuario, disco, valoracion y resenna y mostrarla en el textEdit
        self.tablaResennas = QTableWidget()
        self.tablaResennas.setColumnCount(5)
        self.tablaResennas.setHorizontalHeaderLabels(
            ["Fecha", "Usuario", "Discoteca", "Estrellas", "Reseña"])

        # cambiar el align de Header de Fecha, Usuario, Discoteca, Estrellas
        self.tablaResennas.horizontalHeaderItem(
            0).setTextAlignment(Qt.AlignCenter)
        self.tablaResennas.horizontalHeaderItem(
            1).setTextAlignment(Qt.AlignCenter)
        self.tablaResennas.horizontalHeaderItem(
            2).setTextAlignment(Qt.AlignCenter)
        self.tablaResennas.horizontalHeaderItem(
            3).setTextAlignment(Qt.AlignCenter)
        self.tablaResennas.horizontalHeaderItem(
            4).setTextAlignment(Qt.AlignLeft)

        self.tablaResennas.setShowGrid(True)
        self.tablaResennas.setGridStyle(Qt.SolidLine)

        self.tablaResennas.setRowCount(0)
        self.tablaResennas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaResennas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaResennas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaResennas.setShowGrid(False)
        self.tablaResennas.setStyleSheet("color:  "+color+";\n")
        self.tablaResennas.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tablaResennas.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.tablaResennas.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tablaResennas.horizontalHeader().setSectionResizeMode(
            3, QHeaderView.ResizeToContents)
        self.tablaResennas.horizontalHeader().setSectionResizeMode(
            4, QHeaderView.ResizeToContents)

        self.tablaResennas.verticalHeader().setVisible(False)
        self.verticalLayout_11.addWidget(self.tablaResennas)

        fechasArray = getItemBaseDatos('valoraciones', 'fecha', 'data')
        usuariosArray = getItemBaseDatos('valoraciones', 'usuario', 'data')
        # de usuariosArray quitar de cada elemento estos caracteres:'·º·'
        for i in range(len(usuariosArray)):
            usuariosArray[i] = usuariosArray[i].replace('·º·', '')
        discotecasArray = getItemBaseDatos(
            'valoraciones', 'nombre_discoteca', 'data')
        valoracionesArray = getItemBaseDatos('valoraciones', 'nota', 'data')
        resennasArray = getItemBaseDatos('valoraciones', 'texto', 'data')

        for i in range(len(fechasArray)):
            self.tablaResennas.insertRow(i)
            self.tablaResennas.setItem(i, 0, QTableWidgetItem(fechasArray[i]))
            self.tablaResennas.setItem(
                i, 1, QTableWidgetItem(usuariosArray[i]))
            self.tablaResennas.setItem(
                i, 2, QTableWidgetItem(discotecasArray[i]))
            self.tablaResennas.setItem(
                i, 3, QTableWidgetItem(str(valoracionesArray[i])))

            self.tablaResennas.setItem(
                i, 4, QTableWidgetItem(resennasArray[i]))

        # centrar el texto de la tabla
        for i in range(self.tablaResennas.rowCount()):
            for j in range(self.tablaResennas.columnCount()-1):
                self.tablaResennas.item(i, j).setTextAlignment(Qt.AlignCenter)

    def boton_subir_foto(self):
        self.usuario = datosUsuario('usuario')
        try:
            self.file_name = QFileDialog.getOpenFileName(
                filter="Imagen (*.*)")[0]
            self.image = cv2.imread(self.file_name)
            print(self.file_name)
            subir_foto(self.file_name, self.usuario)
            self.show_popup_imagen_subida()
        except FileNotFoundError:
            pass

    def show_popup_imagen_subida(self):
        msg = QMessageBox()
        msg.setWindowTitle("EVENTLY")
        msg.setText("Imagen subida correctamente.")

        x = msg.exec_()

    def boton_mis_fotos(self):
        self.usuario = datosUsuario('usuario')
        url_fotos = ver_mis_fotos(self.usuario)
        self.textBrowser_MiPerfil.clear()
        self.hbox = QHBoxLayout(self.page_MiPerfil)
        self.hbox.setContentsMargins(10, 235, 10, 10)

        for i in range(len(url_fotos)):
            resp = urlopen(url_fotos[i])
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            image = imutils.resize(image, width=200, height=200)
            self.label = QtWidgets.QLabel()
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

            self.hbox.addWidget(self.label)

    def createGridLayout(self, x):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout
        layout.setGeometry(QtCore.QRect(130, 50, 151, 31))
        layout.setColumnStretch(1, x)
        layout.setColumnStretch(2, x)

    # SE ABRE EL CHAT

    def abrir_ventana_chat(self):
        self.stackedWidget.setCurrentWidget(self.page_chat)

    def abrir_ventana_usuarios(self):
        self.stackedWidget.setCurrentWidget(self.page_usuarios)

    def buttonPerfil(self, usuarioText):
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

    def buttonPerfil2(self, usuarioText):
        self.stackedWidget.setCurrentWidget(self.page_MiPerfil2)
        datosUsuarioEspecifico = getDatosElementoConcreto('usuarios', 'usuario', usuarioText, [
                                                          'usuario', 'nombre', 'apellido', 'email', 'edad'], 'data')
        self.usuario = datosUsuarioEspecifico[0]
        self.usuarioBuscado = self.usuario
        self.textBrowser_usuarioPerfil2.setText(usuarioText)
        self.nombre = datosUsuarioEspecifico[1]
        self.textBrowser_nombrePerfil2.setText(self.nombre)
        self.apellido = datosUsuarioEspecifico[2]
        self.textBrowser_apellidoPerfil2.setText(self.apellido)
        self.email = datosUsuarioEspecifico[3]
        self.textBrowser_emailPerfil2.setText(self.email)
        self.edad = datosUsuarioEspecifico[4]
        self.textBrowser_edadPerfil2.setText(str(self.edad))

    def buttonMisResennas(self):
        self.usr = datosUsuario('usuario')
        out = filtrarDiscotecas(7, (self.usr))
        self.mis_resennas = str(out)
        if self.textBrowser_MiPerfil.isHidden():
            self.textBrowser_MiPerfil.show()
        self.textBrowser_MiPerfil.setText(self.mis_resennas)

    def buttonMisResennasOtroPerfil(self, usuarioText):
        self.usr = self.usuarioBuscado
        out = filtrarDiscotecas(7, (self.usr))
        self.mis_resennas = str(out)
        if self.textBrowser_MiPerfilPerfil2.isHidden(
        ):
            self.textBrowser_MiPerfilPerfil2.show()
        self.textBrowser_MiPerfilPerfil2.setText(self.mis_resennas)

    def buttonMisFiestas(self):
        self.usr = datosUsuario('usuario')
        out = filtrarDiscotecas(10, (self.usr))
        self.mis_fiestas = str(out)
        if self.textBrowser_MiPerfil.isHidden():
            self.textBrowser_MiPerfil.show()
        self.textBrowser_MiPerfil.setText(self.mis_fiestas)

    def buttonMisFiestasOtroPerfil(self):
        self.usr = self.usuarioBuscado
        out = filtrarDiscotecas(10, (self.usr))
        self.mis_fiestas = str(out)
        if self.textBrowser_MiPerfilPerfil2.isHidden(
        ):
            self.textBrowser_MiPerfilPerfil2.show()
        self.textBrowser_MiPerfilPerfil2.setText(self.mis_fiestas)

    def boton_mis_fotos_OtroUsuario(self):
        self.usuario = self.usuarioBuscado
        url_fotos = ver_mis_fotos(self.usuario)
        self.textBrowser_MiPerfilPerfil2.clear()
        self.hbox = QHBoxLayout(self.page_MiPerfil2)
        self.hbox.setContentsMargins(10, 235, 10, 10)

        for i in range(len(url_fotos)):
            resp = urlopen(url_fotos[i])
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            image = imutils.resize(image, width=200, height=200)
            self.label = QtWidgets.QLabel()
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(image))

            self.hbox.addWidget(self.label)

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
        self.frame.setStyleSheet("background-color: "+color2+";")
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
                                          "    background-color:"+color+";\n"
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
# crea una funcion para cuando se pulse el boton pushButton_aceptarFiesta
# llama a esa funcion cuando se pulsar pushButton_aceptarFiesta
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
                                         "    background-color:"+color+";\n"
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
       # BOTON USUARIOS
        self.pushButton_Usuarios = QPushButton(
            self.frame_control, clicked=lambda: self.abrir_ventana_usuarios())
        self.pushButton_Usuarios.setObjectName(u"pushButton_Usuarios")
        self.pushButton_Usuarios.setText('USUARIOS')
        self.pushButton_Usuarios.setEnabled(True)
        self.pushButton_Usuarios.setMinimumSize(QSize(0, 40))
        self.verticalLayout_3.addWidget(self.pushButton_Usuarios)
        # BOTON MAPA
        self.pushButton_Mapa = QtWidgets.QPushButton(self.frame_control)
        self.pushButton_Mapa.setEnabled(True)
        self.pushButton_Mapa.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Mapa.clicked.connect(self.buttonMapa)
        self.pushButton_Mapa.setObjectName("pushButton_Mapa")
        self.verticalLayout_3.addWidget(self.pushButton_Mapa)
        # BOTON FILTRADO
        self.pushButton_Filtrado = QtWidgets.QPushButton(self.frame_control)
        self.pushButton_Filtrado.setEnabled(True)
        self.pushButton_Filtrado.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Filtrado.clicked.connect(self.buttonFiltrado)
        self.pushButton_Filtrado.setObjectName("pushButton_Filtrado")
        self.verticalLayout_3.addWidget(self.pushButton_Filtrado)
        # BOTON DICOTECA
        self.pushButton_Discoteca = QtWidgets.QPushButton(self.frame_control)
        self.pushButton_Discoteca.setEnabled(True)
        self.pushButton_Discoteca.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Discoteca.clicked.connect(self.buttonDiscotecas)
        self.pushButton_Discoteca.setObjectName("pushButton_Discoteca")
        self.verticalLayout_3.addWidget(self.pushButton_Discoteca)
        # BOTON FIESTA
        self.pushButton_Fiesta = QtWidgets.QPushButton(self.frame_control)
        self.pushButton_Fiesta.setEnabled(True)
        self.pushButton_Fiesta.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Fiesta.clicked.connect(self.buttonFiesta)
        self.pushButton_Fiesta.setObjectName("pushButton_Fiesta")
        self.verticalLayout_3.addWidget(self.pushButton_Fiesta)
        # BOTON RESEÑA
        self.pushButton_Resenna = QtWidgets.QPushButton(self.frame_control)
        self.pushButton_Resenna.setEnabled(True)
        self.pushButton_Resenna.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Resenna.clicked.connect(self.buttonResenna)
        self.pushButton_Resenna.setObjectName("pushButton_Resenna")
        self.verticalLayout_3.addWidget(self.pushButton_Resenna)
        self.horizontalLayout.addWidget(self.frame_control)
        self.frame_paginas = QtWidgets.QFrame(self.frame_contenido)
        # BOTON PERFIL
        self.pushButton_MiPerfil = QPushButton(self.frame_control)
        self.pushButton_MiPerfil.setObjectName(u"pushButton_MiPerfil")
        self.pushButton_MiPerfil.clicked.connect(self.buttonPerfil)
        self.pushButton_MiPerfil.setText('MI PERFIL')
        self.pushButton_MiPerfil.setEnabled(True)
        self.pushButton_MiPerfil.setMinimumSize(QtCore.QSize(0, 40))
        self.verticalLayout_3.addWidget(self.pushButton_MiPerfil)
        # BOTON CHAT
        self.pushButton_Chat = QPushButton(
            self.frame_control, clicked=lambda: self.abrir_ventana_chat())
        self.pushButton_Chat.setObjectName(u"pushButton_Chat")
        self.pushButton_Chat.setText('CHAT')
        self.pushButton_Chat.setEnabled(True)
        self.pushButton_Chat.setMinimumSize(QSize(0, 40))
        self.verticalLayout_3.addWidget(self.pushButton_Chat)

        # ESTE ES EL DE FILTRADO
        self.frame_paginas.setStyleSheet("QFrame{\n"
                                         "    background-color:"+color2+";\n"
                                         "}\n"
                                         "\n"
                                         "QLabel{\n"
                                         "    font: 87 12pt \"Arial Black\";    \n"
                                         "    background-color:#000000ff;\n"
                                         "    color:  "+color+";\n"
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
                                         "    background-color:"+color+";\n"
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

        """PÁGINA DEL FILTRADO"""

        self.page_filtrado = QtWidgets.QWidget()
        self.page_filtrado.setObjectName("page_filtrado")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_filtrado)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.page_filtrado)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.page_filtrado)
        self.comboBox.setStyleSheet("color:  "+color+";\n"
                                    "background-color: #000000ff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_13.addWidget(self.comboBox)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_BusquedaFiltrado = QtWidgets.QLineEdit(
            self.page_filtrado)
        self.lineEdit_BusquedaFiltrado.setStyleSheet(
            "color:  "+color+";")
        self.lineEdit_BusquedaFiltrado.setObjectName(
            "lineEdit_BusquedaFiltrado")
        self.horizontalLayout_9.addWidget(self.lineEdit_BusquedaFiltrado)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.pushButton_BuscarFiltrado = QtWidgets.QPushButton(
            self.page_filtrado)
        self.pushButton_BuscarFiltrado.setObjectName(
            "pushButton_BuscarFiltrado")
        self.pushButton_BuscarFiltrado.clicked.connect(self.busquedaFilter)
        self.horizontalLayout_9.addWidget(self.pushButton_BuscarFiltrado)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)

        # añade para poder añadir un boton por cada discoteca, y poder desplazarte con un scroll bar por los botones
        self.scrollArea = QtWidgets.QScrollArea(self.page_filtrado)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_13.addWidget(self.scrollArea)
        # añade un boton dentro del scroll area
        self.stackedWidget.addWidget(self.page_filtrado)

        """PÁGINA DE CHAT"""

        self.page_chat = QtWidgets.QWidget()
        self.page_chat.setObjectName("page_chat")
        self.verticalLayout_13Chat = QtWidgets.QVBoxLayout(self.page_chat)
        self.verticalLayout_13Chat.setObjectName("verticalLayout_13Chat")
        self.label_6Chat = QtWidgets.QLabel(self.page_chat)
        self.label_6Chat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6Chat.setObjectName("label_6Chat")
        self.verticalLayout_13Chat.addWidget(self.label_6Chat)
        self.horizontalLayout_9Chat = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9Chat.setObjectName("horizontalLayout_9Chat")

        self.lineEdit_BusquedaChat = QtWidgets.QLineEdit(
            self.page_chat)
        self.lineEdit_BusquedaChat.setStyleSheet(
            "color:  "+color+";")
        self.lineEdit_BusquedaChat.setObjectName(
            "lineEdit_BusquedaChat")
        self.horizontalLayout_9Chat.addWidget(self.lineEdit_BusquedaChat)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9Chat.addItem(spacerItem1)
        self.pushButton_BuscarChat = QtWidgets.QPushButton(
            self.page_chat)
        self.pushButton_BuscarChat.setObjectName(
            "pushButton_BuscarChat")
        self.pushButton_BuscarChat.clicked.connect(
            self.crearBotonesChatUsuarios)
        self.horizontalLayout_9Chat.addWidget(self.pushButton_BuscarChat)
        spacerItem2Chat = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9Chat.addItem(spacerItem2Chat)
        self.verticalLayout_13Chat.addLayout(self.horizontalLayout_9Chat)

        # añade para poder añadir un boton por cada discoteca, y poder desplazarte con un scroll bar por los botones
        self.scrollAreaChat = QtWidgets.QScrollArea(self.page_chat)
        self.scrollAreaChat.setWidgetResizable(True)
        self.scrollAreaChat.setObjectName("scrollAreaChat")

        self.scrollAreaWidgetContents2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents2.setGeometry(
            QtCore.QRect(0, 0, 100, 100))
        self.scrollAreaWidgetContents2.setObjectName(
            "scrollAreaWidgetContents2")
        self.verticalLayout_14Chat = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents2)
        self.verticalLayout_14Chat.setObjectName("verticalLayout_14Chat")
        self.scrollAreaChat.setWidget(self.scrollAreaWidgetContents2)
        self.verticalLayout_13Chat.addWidget(self.scrollAreaChat)
        # añade un boton dentro del scroll area
        self.stackedWidget.addWidget(self.page_chat)

        # PAGINA DE USUARIOS
        self.page_usuarios = QtWidgets.QWidget()
        self.page_usuarios.setObjectName("page_usuarios")
        self.verticalLayout_13Usuarios = QtWidgets.QVBoxLayout(
            self.page_usuarios)
        self.verticalLayout_13Usuarios.setObjectName(
            "verticalLayout_13Usuarios")
        self.label_6Usuarios = QtWidgets.QLabel(self.page_usuarios)
        self.label_6Usuarios.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6Usuarios.setObjectName("label_6Usuarios")
        self.verticalLayout_13Usuarios.addWidget(self.label_6Usuarios)
        self.horizontalLayout_9Usuarios = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9Usuarios.setObjectName(
            "horizontalLayout_9Usuarios")

        self.lineEdit_BusquedaUsuarios = QtWidgets.QLineEdit(
            self.page_usuarios)
        self.lineEdit_BusquedaUsuarios.setStyleSheet(
            "color:  "+color+";")
        self.lineEdit_BusquedaUsuarios.setObjectName(
            "lineEdit_BusquedaUsuarios")
        self.horizontalLayout_9Usuarios.addWidget(
            self.lineEdit_BusquedaUsuarios)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9Usuarios.addItem(spacerItem1)
        self.pushButton_BuscarUsuarios = QtWidgets.QPushButton(
            self.page_usuarios)
        self.pushButton_BuscarUsuarios.setObjectName(
            "pushButton_BuscarUsuarios")
        self.pushButton_BuscarUsuarios.clicked.connect(
            self.crearBotonesUsuarios)
        self.horizontalLayout_9Usuarios.addWidget(
            self.pushButton_BuscarUsuarios)
        spacerItem2Usuarios = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9Usuarios.addItem(spacerItem2Usuarios)
        self.verticalLayout_13Usuarios.addLayout(
            self.horizontalLayout_9Usuarios)

        # añade para poder añadir un boton por cada discoteca, y poder desplazarte con un scroll bar por los botones
        self.scrollAreaUsuarios = QtWidgets.QScrollArea(self.page_usuarios)
        self.scrollAreaUsuarios.setWidgetResizable(True)
        self.scrollAreaUsuarios.setObjectName("scrollAreaUsuarios")

        self.scrollAreaWidgetContents3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents3.setGeometry(
            QtCore.QRect(0, 0, 100, 100))
        self.scrollAreaWidgetContents3.setObjectName(
            "scrollAreaWidgetContents3")
        self.verticalLayout_14Usuarios = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents3)
        self.verticalLayout_14Usuarios.setObjectName(
            "verticalLayout_14Usuarios")
        self.scrollAreaUsuarios.setWidget(self.scrollAreaWidgetContents3)
        self.verticalLayout_13Usuarios.addWidget(self.scrollAreaUsuarios)
        # añade un boton dentro del scroll area
        self.stackedWidget.addWidget(self.page_usuarios)

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
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        self.lineEdit_nombreDiscoteca = QtWidgets.QLineEdit(
            self.page_AddDiscoteca)
        self.lineEdit_nombreDiscoteca.setStyleSheet(
            "color: rgb(255, 255, 255);")
        self.lineEdit_nombreDiscoteca.setText("")
        self.lineEdit_nombreDiscoteca.setObjectName("lineEdit_nombreDiscoteca")
        self.verticalLayout_6.addWidget(self.lineEdit_nombreDiscoteca)
        self.lineEdit_zonaDiscoteca = QtWidgets.QLineEdit(
            self.page_AddDiscoteca)
        self.lineEdit_zonaDiscoteca.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_zonaDiscoteca.setObjectName("lineEdit_zonaDiscoteca")
        self.verticalLayout_6.addWidget(self.lineEdit_zonaDiscoteca)
        self.lineEdit_calleDiscoteca = QtWidgets.QLineEdit(
            self.page_AddDiscoteca)
        self.lineEdit_calleDiscoteca.setStyleSheet(
            "color: rgb(255, 255, 255);")
        self.lineEdit_calleDiscoteca.setText("")
        self.lineEdit_calleDiscoteca.setObjectName("lineEdit_calleDiscoteca")
        self.verticalLayout_6.addWidget(self.lineEdit_calleDiscoteca)
        self.lineEdit_numeroDiscoteca = QtWidgets.QLineEdit(
            self.page_AddDiscoteca)
        self.lineEdit_numeroDiscoteca.setStyleSheet(
            "color: rgb(255, 255, 255);")
        self.lineEdit_numeroDiscoteca.setObjectName("lineEdit_numeroDiscoteca")
        self.verticalLayout_6.addWidget(self.lineEdit_numeroDiscoteca)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.pushButton_aceptarDiscoteca = QtWidgets.QPushButton(
            self.page_AddDiscoteca)
        self.pushButton_aceptarDiscoteca.setMaximumSize(
            QtCore.QSize(180, 16777215))
        self.pushButton_aceptarDiscoteca.setObjectName(
            "pushButton_aceptarDiscoteca")
        self.pushButton_aceptarDiscoteca.clicked.connect(self.annadirDiscoteca)
        self.horizontalLayout_5.addWidget(self.pushButton_aceptarDiscoteca)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.pushButton_aceptarFiesta = QtWidgets.QPushButton(
            self.page_AddFiesta)
        self.pushButton_aceptarFiesta.setObjectName("pushButton_aceptarFiesta")
        self.horizontalLayout_7.addWidget(self.pushButton_aceptarFiesta)
        # pulsar boton aceptar
        self.pushButton_aceptarFiesta.clicked.connect(self.annadirFiesta)
        spacerItem12 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
                                           "    color:  "+color+";\n"
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
                                           "    background-color:"+color+";\n"
                                           "    border-radius: 15px;\n"
                                           "    color: rgb(0,0,0);\n"
                                           "    font: 77 10pt \"Arial Black\";\n"
                                           "}\n"
                                           "\n"
                                           "QRadioButton{\n"
                                           "    background-color:"+color+";\n"
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
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        # change the lineEdit2 to a comboBox
        self.comboBoxDisco = QtWidgets.QComboBox(self.frame_2)
        self.comboBoxDisco.setObjectName("comboBoxDisco")
        self.verticalLayout_10.addWidget(self.comboBoxDisco)
        self.comboBoxDisco.setStyleSheet("color:  "+color+";\n"
                                         "background-color: #000000ff;")
        discotecas = getItemBaseDatos('discotecas', 'nombre', 'data')
        for i in discotecas:
            self.comboBoxDisco.addItem(i)
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)

        # AÑADIR RESEÑA
        self.textEdit.setStyleSheet("background-color:"+color2+";\n")
        self.textEdit.setStyleSheet("color:  "+color+";\n")
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
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """PÁGINA MI PERFIL """
        self.page_MiPerfil = QtWidgets.QWidget()
        self.page_MiPerfil.setObjectName("page_MiPerfil")
        self.label_7 = QLabel(self.page_MiPerfil)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QtCore.QRect(6, 10, 591, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.page_MiPerfil)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 40, 111, 141))
        self.verticalLayout_15 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_usuario = QLabel(self.verticalLayoutWidget)
        self.label_usuario.setObjectName("label_usuario")
        self.label_usuario.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.verticalLayout_15.addWidget(self.label_usuario)
        self.label_nombre = QLabel(self.verticalLayoutWidget)
        self.label_nombre.setObjectName("label_nombre")
        self.label_nombre.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.verticalLayout_15.addWidget(self.label_nombre)
        self.label_apellido = QLabel(self.verticalLayoutWidget)
        self.label_apellido.setObjectName("label_apellido")
        self.label_apellido.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.verticalLayout_15.addWidget(self.label_apellido)
        self.textBrowser_usuario = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_usuario.setObjectName("textBrowser_usuario")
        self.textBrowser_usuario.setGeometry(QtCore.QRect(130, 50, 151, 31))
        self.textBrowser_usuario.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.textBrowser_nombre = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_nombre.setObjectName("textBrowser_nombre")
        self.textBrowser_nombre.setGeometry(QRect(130, 100, 151, 31))
        self.textBrowser_nombre.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.textBrowser_apellido = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_apellido.setObjectName("textBrowser_apellido")
        self.textBrowser_apellido.setGeometry(QRect(130, 150, 151, 31))
        self.textBrowser_apellido.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.verticalLayoutWidget_2 = QWidget(self.page_MiPerfil)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(290, 40, 91, 141))
        self.verticalLayout_15 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_email = QLabel(self.verticalLayoutWidget_2)
        self.label_email.setObjectName("label_email")
        self.label_email.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.verticalLayout_15.addWidget(self.label_email)
        self.label_edad = QLabel(self.verticalLayoutWidget_2)
        self.label_edad.setObjectName("label_edad")
        self.label_edad.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.verticalLayout_15.addWidget(self.label_edad)
        self.textBrowser_email = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_email.setObjectName("textBrowser_email")
        self.textBrowser_email.setGeometry(QRect(390, 60, 150, 31))
        self.textBrowser_email.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.textBrowser_edad = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_edad.setObjectName("textBrowser_edad")
        self.textBrowser_edad.setGeometry(QRect(390, 130, 150, 31))
        self.textBrowser_edad.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.textBrowser_MiPerfil = QTextBrowser(self.page_MiPerfil)
        self.textBrowser_MiPerfil.setObjectName("textBrowser_MiPerfil")
        self.textBrowser_MiPerfil.setGeometry(QRect(10, 230, 520, 280))
        self.textBrowser_MiPerfil.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.pushButton_MisResennas = QPushButton(self.page_MiPerfil)
        self.pushButton_MisResennas.setObjectName("pushButton_MisResennas")
        self.pushButton_MisResennas.clicked.connect(self.buttonMisResennas)
        self.pushButton_MisResennas.setGeometry(QRect(250, 200, 111, 23))
        self.pushButton_MisFiestas = QPushButton(self.page_MiPerfil)
        self.pushButton_MisFiestas.setObjectName("pushButton_MisFiestas")
        self.pushButton_MisFiestas.clicked.connect(self.buttonMisFiestas)
        self.pushButton_MisFiestas.setGeometry(QRect(370, 200, 101, 23))
        self.pushButton_SubirFotos = QPushButton(self.page_MiPerfil)
        self.pushButton_SubirFotos.setObjectName("pushButton_SubirFotos")
        self.pushButton_SubirFotos.clicked.connect(self.boton_subir_foto)
        self.pushButton_SubirFotos.setGeometry(20, 200, 115, 23)
        self.pushButton_MisFotos = QPushButton(self.page_MiPerfil)
        self.pushButton_MisFotos.setObjectName("pushButton_MisFotos")
        self.pushButton_MisFotos.clicked.connect(self.boton_mis_fotos)
        self.pushButton_MisFotos.setGeometry(QRect(145, 200, 101, 23))
        self.stackedWidget.addWidget(self.page_MiPerfil)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame_paginas)
        self.verticalLayout_2.addWidget(self.frame_contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout_12.addWidget(self.frame)

        """PÁGINA MI PERFIL2 """
        self.page_MiPerfil2 = QtWidgets.QWidget()
        self.page_MiPerfil2.setObjectName("page_MiPerfil2")
        self.label_7Perfil2 = QLabel(self.page_MiPerfil2)
        self.label_7Perfil2.setObjectName("label_7Perfil2")
        self.label_7Perfil2.setGeometry(QtCore.QRect(6, 10, 591, 20))
        self.label_7Perfil2.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.page_MiPerfil2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 40, 111, 141))
        self.verticalLayout_15Perfil2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_15Perfil2.setObjectName("verticalLayout_15Perfil2")
        self.verticalLayout_15Perfil2.setContentsMargins(0, 0, 0, 0)
        self.label_usuarioPerfil2 = QLabel(self.verticalLayoutWidget)
        self.label_usuarioPerfil2.setObjectName("label_usuarioPerfil2")
        self.label_usuarioPerfil2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.verticalLayout_15Perfil2.addWidget(self.label_usuarioPerfil2)
        self.label_nombrePerfil2 = QLabel(self.verticalLayoutWidget)
        self.label_nombrePerfil2.setObjectName("label_nombrePerfil2")
        self.label_nombrePerfil2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.verticalLayout_15Perfil2.addWidget(self.label_nombrePerfil2)
        self.label_apellidoPerfil2 = QLabel(self.verticalLayoutWidget)
        self.label_apellidoPerfil2.setObjectName("label_apellidoPerfil2")
        self.label_apellidoPerfil2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.verticalLayout_15Perfil2.addWidget(self.label_apellidoPerfil2)
        self.textBrowser_usuarioPerfil2 = QTextBrowser(self.page_MiPerfil2)
        self.textBrowser_usuarioPerfil2.setObjectName(
            "textBrowser_usuarioPerfil2")
        self.textBrowser_usuarioPerfil2.setGeometry(
            QtCore.QRect(130, 50, 151, 31))
        self.textBrowser_usuarioPerfil2.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.textBrowser_nombrePerfil2 = QTextBrowser(self.page_MiPerfil2)
        self.textBrowser_nombrePerfil2.setObjectName(
            "textBrowser_nombrePerfil2")
        self.textBrowser_nombrePerfil2.setGeometry(QRect(130, 100, 151, 31))
        self.textBrowser_nombrePerfil2.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.textBrowser_apellidoPerfil2 = QTextBrowser(self.page_MiPerfil2)
        self.textBrowser_apellidoPerfil2.setObjectName(
            "textBrowser_apellidoPerfil2")
        self.textBrowser_apellidoPerfil2.setGeometry(QRect(130, 150, 151, 31))
        self.textBrowser_apellidoPerfil2.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.verticalLayoutWidget_2Perfil = QWidget(self.page_MiPerfil2)
        self.verticalLayoutWidget_2Perfil.setObjectName(
            "verticalLayoutWidget_2Perfil")
        self.verticalLayoutWidget_2Perfil.setGeometry(QRect(290, 40, 91, 141))
        self.verticalLayout_15Perfil2 = QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_15Perfil2.setObjectName("verticalLayout_15Perfil2")
        self.verticalLayout_15Perfil2.setContentsMargins(0, 0, 0, 0)
        self.label_emailPerfil2 = QLabel(self.verticalLayoutWidget_2Perfil)
        self.label_emailPerfil2.setObjectName("label_emailPerfil2")
        self.label_emailPerfil2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.verticalLayout_15Perfil2.addWidget(self.label_emailPerfil2)
        self.label_edadPerfil2 = QLabel(self.verticalLayoutWidget_2Perfil)
        self.label_edadPerfil2.setObjectName("label_edadPerfil2")
        self.label_edadPerfil2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.verticalLayout_15Perfil2.addWidget(self.label_edadPerfil2)
        self.textBrowser_emailPerfil2 = QTextBrowser(self.page_MiPerfil2)
        self.textBrowser_emailPerfil2.setObjectName("textBrowser_emailPerfil2")
        self.textBrowser_emailPerfil2.setGeometry(QRect(390, 60, 150, 31))
        self.textBrowser_emailPerfil2.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.textBrowser_edadPerfil2 = QTextBrowser(self.page_MiPerfil2)
        self.textBrowser_edadPerfil2.setObjectName("textBrowser_edadPerfil2")
        self.textBrowser_edadPerfil2.setGeometry(QRect(390, 130, 150, 31))
        self.textBrowser_edadPerfil2.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.textBrowser_MiPerfilPerfil2 = QTextBrowser(self.page_MiPerfil2)
        self.textBrowser_MiPerfilPerfil2.setObjectName(
            "textBrowser_MiPerfilPerfil2")
        self.textBrowser_MiPerfilPerfil2.setGeometry(QRect(10, 230, 520, 280))
        self.textBrowser_MiPerfilPerfil2.setStyleSheet(
            "background-color: rgb(255, 255, 255)")
        self.pushButton_MisResennasPerfil2 = QPushButton(self.page_MiPerfil2)
        self.pushButton_MisResennasPerfil2.setObjectName(
            "pushButton_MisResennasPerfil2")
        self.pushButton_MisResennasPerfil2.clicked.connect(
            self.buttonMisResennasOtroPerfil)
        self.pushButton_MisResennasPerfil2.setGeometry(
            QRect(250, 200, 111, 23))
        self.pushButton_MisFiestasPerfil2 = QPushButton(self.page_MiPerfil2)
        self.pushButton_MisFiestasPerfil2.setObjectName(
            "pushButton_MisFiestasPerfil2")
        self.pushButton_MisFiestasPerfil2.clicked.connect(
            self.buttonMisFiestasOtroPerfil)
        self.pushButton_MisFiestasPerfil2.setGeometry(QRect(370, 200, 101, 23))
        self.pushButton_MisFotosPerfil2 = QPushButton(self.page_MiPerfil2)
        self.pushButton_MisFotosPerfil2.setObjectName(
            "pushButton_MisFotosPerfil2")
        self.pushButton_MisFotosPerfil2.clicked.connect(
            self.boton_mis_fotos_OtroUsuario)
        self.pushButton_MisFotosPerfil2.setGeometry(QRect(145, 200, 101, 23))

        self.stackedWidget.addWidget(self.page_MiPerfil2)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Mapa.setText(_translate("MainWindow", "MAPA"))
        self.pushButton_Filtrado.setText(_translate("MainWindow", "FILTRADO"))
        self.pushButton_Discoteca.setText(
            _translate("MainWindow", "AÑADIR DISCOTECA"))
        self.pushButton_Fiesta.setText(
            _translate("MainWindow", "AÑADIR FIESTA"))
        self.pushButton_Resenna.setText(
            _translate("MainWindow", "AÑADIR RESEÑA"))
        self.pushButton_MiPerfil.setText(
            _translate("MainWindow", "MI PERFIL"))
        self.label_6.setText(_translate("MainWindow", "FILTRADO"))
        self.label_6Chat.setText(_translate("MainWindow", "CHAT"))
        self.label_6Usuarios.setText(_translate("MainWindow", "USUARIOS"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ZONA"))
        self.comboBox.setItemText(1, _translate("MainWindow", "NOMBRE"))
        self.comboBox.setItemText(2, _translate("MainWindow", "CALLE"))
        self.comboBox.setItemText(3, _translate("MainWindow", "VALORACIÓN"))
        self.lineEdit_BusquedaFiltrado.setText(
            _translate("MainWindow", "BÚSQUEDA"))
        self.lineEdit_BusquedaChat.setText(
            _translate("MainWindow", "BÚSQUEDA"))
        self.pushButton_BuscarFiltrado.setText(
            _translate("MainWindow", "BUSCAR"))
        self.pushButton_BuscarUsuarios.setText(
            _translate("MainWindow", "BUSCAR"))
        self.pushButton_BuscarChat.setText(_translate("MainWindow", "BUSCAR"))
        self.label_9.setText(_translate("MainWindow", "AÑADIR DISCOTECA"))
        self.label_nombreDiscoteca.setText(_translate("MainWindow", "NOMBRE"))
        self.label_zonaDiscoteca.setText(_translate("MainWindow", "ZONA"))
        self.label_calleDiscoteca.setText(_translate("MainWindow", "CALLE"))
        self.label_numeroDiscoteca.setText(_translate("MainWindow", "NÚMERO"))
        self.pushButton_aceptarDiscoteca.setText(
            _translate("MainWindow", "ACEPTAR"))
        self.label_2.setText(_translate("MainWindow", "AÑADIR FIESTA"))
        self.label_nombreFiesta.setText(_translate("MainWindow", "NOMBRE"))
        self.label_zonaFiesta.setText(_translate("MainWindow", "ZONA"))
        self.label_calleFiesta.setText(_translate("MainWindow", "CALLE"))
        self.label_numeroFiesta.setText(_translate("MainWindow", "NÚMERO"))
        self.pushButton_aceptarFiesta.setText(
            _translate("MainWindow", "ACEPTAR"))
        self.label.setText(_translate("MainWindow", "ESCRIBIR RESEÑA"))
        self.label_4.setText(_translate("MainWindow", "DISCOTECA"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Escriba aquí su reseña</span></p></body></html>"))
        self.radioButton_1estrella.setText(
            _translate("MainWindow", "1 ESTRELLA"))
        self.radioButton_2estrellas.setText(
            _translate("MainWindow", "2 ESTRELLAS"))
        self.radioButton_3estrellas.setText(
            _translate("MainWindow", "3 ESTRELLAS"))
        self.radioButton_4estrellas.setText(
            _translate("MainWindow", "4 ESTRELLAS"))
        self.radioButton_5estrellas.setText(
            _translate("MainWindow", "5 ESTRELLAS"))
        self.pushButton_AddResenna.setText(_translate("MainWindow", "AÑADIR"))
        self.label_5.setText(_translate("MainWindow", "OTRAS RESEÑAS"))
        self.label_7.setText(_translate("MainWindow", "MI PERFIL"))
        self.label_7Perfil2.setText(_translate("MainWindow", "PERFIL"))
        self.pushButton_MiPerfil.setText(_translate("MainWindow", "MI PERFIL"))
        self.label_usuario.setText(_translate("MainWindow", "USUARIO:"))
        self.label_nombre.setText(_translate("MainWindow", "NOMBRE:"))
        self.label_apellido.setText(_translate("MainWindow", "APELLIDO:"))
        self.label_email.setText(_translate("MainWindow", "EMAIL:"))
        self.label_edad.setText(_translate("MainWindow", "EDAD:"))
        self.pushButton_MisResennas.setText(
            _translate("MainWindow", "Mis rese\u00f1as"))
        self.pushButton_MisFiestas.setText(
            _translate("MainWindow", "Mis fiestas"))
        self.pushButton_SubirFotos.setText(
            _translate("MainWindow", "Subir fotos"))
        self.pushButton_MisFotos.setText(
            _translate("MainWindow", "Mis fotos"))
        self.label_usuarioPerfil2.setText(_translate("MainWindow", "USUARIO:"))
        self.label_nombrePerfil2.setText(_translate("MainWindow", "NOMBRE:"))
        self.label_apellidoPerfil2.setText(
            _translate("MainWindow", "APELLIDO:"))
        self.label_emailPerfil2.setText(_translate("MainWindow", "EMAIL:"))
        self.label_edadPerfil2.setText(_translate("MainWindow", "EDAD:"))
        self.pushButton_MisResennasPerfil2.setText(
            _translate("MainWindow", "Rese\u00f1as"))
        self.pushButton_MisFiestasPerfil2.setText(
            _translate("MainWindow", "Fiestas"))
        self.pushButton_MisFotosPerfil2.setText(
            _translate("MainWindow", "Fotos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.showMaximized()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
