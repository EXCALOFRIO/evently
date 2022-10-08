# Form implementation generated from reading ui file '.\login.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from tkinter import messagebox
from PyQt6 import QtCore, QtGui, QtWidgets
from baseDatosPrueba import comprobarInicioSesion


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(426, 475)
        Login.setWindowOpacity(1.0)
        Login.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.i_password = QtWidgets.QLineEdit(self.centralwidget)
        self.i_password.setGeometry(QtCore.QRect(50, 250, 331, 41))
        self.i_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 153, 0);\n"
"font: 15pt \"Yu Gothic UI\";")
        self.i_password.setText("")
        self.i_password.setObjectName("i_password")
        self.l_signup = QtWidgets.QLabel(self.centralwidget)
        self.l_signup.setGeometry(QtCore.QRect(110, 400, 211, 21))
        self.l_signup.setStyleSheet("color: rgb(255, 153, 0);\n"
"font: 13pt \"Yu Gothic UI\";")
        self.l_signup.setObjectName("l_signup")
        self.b_login = QtWidgets.QPushButton(self.centralwidget)
        self.b_login.setGeometry(QtCore.QRect(50, 330, 331, 41))
        self.b_login.setStyleSheet("background-color: rgb(255, 153, 0);\n"
"font: 16pt \"Yu Gothic UI\";")
        self.b_login.setObjectName("b_login")
        self.l_password = QtWidgets.QLabel(self.centralwidget)
        self.l_password.setGeometry(QtCore.QRect(50, 200, 91, 31))
        self.l_password.setStyleSheet("font: 15pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.l_password.setObjectName("l_password")
        self.l_username = QtWidgets.QLabel(self.centralwidget)
        self.l_username.setGeometry(QtCore.QRect(50, 100, 91, 31))
        self.l_username.setStyleSheet("font: 15pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.l_username.setObjectName("l_username")
        self.i_username = QtWidgets.QLineEdit(self.centralwidget)
        self.i_username.setGeometry(QtCore.QRect(50, 150, 331, 41))
        self.i_username.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 153, 0);\n"
"font: 15pt \"Yu Gothic UI\";")
        self.i_username.setObjectName("i_username")
        self.l_topic = QtWidgets.QLabel(self.centralwidget)
        self.l_topic.setGeometry(QtCore.QRect(170, 20, 91, 51))
        self.l_topic.setStyleSheet("font: 26pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.l_topic.setObjectName("l_topic")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.l_signup.setText(_translate("Login", "No Account? Sign Up here"))
        self.b_login.setText(_translate("Login", "Login"))
        self.l_password.setText(_translate("Login", "Password:"))
        self.l_username.setText(_translate("Login", "Username:"))
        self.l_topic.setText(_translate("Login", "Login"))

        
        
        def botonRegistroClick():
                
                import registro


# metodo comprueba que el usuario y la contraseña son correctos


# Acciones del botón Aceptar
        def botonAceptarClick():
                if comprobarInicioSesion(self.i_username.text(),self.i_password.text() ,'data'):
                        Login.close()
                        import principal
                else:
                        messagebox.showerror(
                        "Error", "El usuario o la contraseña son incorrectos")

        #cuadno se presiona el boton de login se llama a la funcionAceptarClick
        self.b_login.clicked.connect(botonAceptarClick)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
