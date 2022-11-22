from tkinter import *
from tkinter import messagebox
from turtle import bgcolor

#from evently.src.ui_evently import Ui_MainWindow

from ui_evently import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QInputDialog, QFileDialog
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.uic import loadUi
import pyglet
import webview

from baseDatosPrueba import comprobarInicioSesion, color,color2, fuentePrincipal

import pyglet

pyglet.font.add_file('fuentes/productSans.ttf')  # ABeeZee

inicio = Tk()
inicio.title("EVENTLY")
inicio.geometry("300x350")

inicio.config(bg=color)
inicio.resizable(0, 0)

frame1 = Frame(inicio, width=300, height=500, bg=color)
frame1.pack()

inicioSesion = Label(frame1, text="Inicio de Sesión",
                     font=(fuentePrincipal, 20), bg=color)
inicioSesion.grid(row=0, padx=10, pady=10)

usuarioLabel = Label(frame1, text="Usuario:",
                     font=(fuentePrincipal, 12), bg=color)
usuarioLabel.grid(row=1, pady=5)

contrasenaLabel = Label(frame1, text="Contraseña:",
                        font=(fuentePrincipal, 12), bg=color)
contrasenaLabel.grid(row=3, pady=5)

nombreUsuario = StringVar()
usuarioEntry = Entry(frame1, textvariable=nombreUsuario, font=(fuentePrincipal, 12))

usuarioEntry.grid(row=2)

contrasenaUsuario = StringVar()
contrasenaEntry = Entry(
    frame1, textvariable=contrasenaUsuario, font=(fuentePrincipal, 12))
contrasenaEntry.grid(row=4)
contrasenaEntry.config(show="*")

frame2 = Frame(inicio, bg=color)
frame2.pack()

botonAceptar = Button(frame2, text="Aceptar",
                      command=lambda: botonAceptarClick(), font=(fuentePrincipal, 10))
botonAceptar.config(bg='white')
botonAceptar.grid(column=0, row=0, padx=5, pady=10)


botonRegistro = Button(frame2, text="Registro",
                       command=lambda: botonRegistroClick(), font=(fuentePrincipal, 10))
botonRegistro.config(bg='white')
botonRegistro.grid(column=1, row=0, padx=5, pady=10)


# Acciones del botón Registro
def botonRegistroClick():
    inicio.destroy()
    import registro


# Acciones del botón Aceptar
def botonAceptarClick():
    if comprobarInicioSesion(usuarioEntry.get(), contrasenaEntry.get(),'data'):
        inicio.destroy()
        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
    elif ValueError:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")
    else:
        messagebox.showerror(
            "Error", "El usuario o la contraseña son incorrectos")


inicio.mainloop()
