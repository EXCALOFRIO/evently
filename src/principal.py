from tkinter import *

# add a custom fonto to tkinter from a file that is in the same directory as the python file
import tkinter as tk

import pyglet

from baseDatosPrueba import datosUsuario

pyglet.font.add_file('fuentes/productSans.ttf')  # ABeeZee


# add froma a .ttf
inicio = Tk()
inicio.title("INICIO")
inicio.geometry("600x350")
inicio.resizable(0, 0)

frame1 = Frame(inicio, width=300, height=500)
frame1.pack()

#añade un texto encima de los botonoes con el nombre de usuario de la sesion que lo obtien de usuarioActual
def textoUsuario():
    texto = Label(inicio, text='Bienvenido: ' + datosUsuario('usuario') )
    texto.place(x=10, y=10)

textoUsuario()


# añade 3 botones de colore salmón, verde y azul para añadir discotecas añadir fiestas y valoraciones
boton1 = Button(frame1, text="Añadir Discoteca",
                command=lambda: botonDicotecaClick(), font=("ABeeZee", 10))
boton1.grid(column=0, row=0, padx=20, pady=30)

boton2 = Button(frame1, text="Añadir Fiestas",
                command=lambda: botonFiestaClick(), font=("ABeeZee", 10))
boton2.grid(column=1, row=0, padx=20, pady=30)

boton3 = Button(frame1, text="Añadir Valoraciones",
                command=lambda: botonValoracionClick(), font=("ABeeZee", 10))
boton3.grid(column=2, row=0, padx=20, pady=30)

boton4 = Button(frame1, text="Volver atrás",
                command=lambda: botonVolverAtras(), font=("ABeeZee", 10))
boton4.grid(column=1, row=1, padx=20, pady=30)


# Acciones del botón Discoteca
def botonDicotecaClick():
    inicio.destroy()
    import añadirDiscoteca

# Acciones del botón Fiesta


def botonFiestaClick():
    inicio.destroy()
    import añadirFiesta

# Acciones del botón Valoracion


def botonValoracionClick():
    inicio.destroy()
    import reseñas


def botonVolverAtras():
    inicio.destroy()
    import registro


inicio.mainloop()
