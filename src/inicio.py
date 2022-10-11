from tkinter import *
from tkinter import messagebox
from turtle import bgcolor

from baseDatosPrueba import comprobarInicioSesion

import pyglet

pyglet.font.add_file('fuentes/productSans.ttf')  # ABeeZee

inicio = Tk()
inicio.title("EVENTLY")
inicio.geometry("300x350")
inicio.config(bg='#57E389')
inicio.resizable(0, 0)

frame1 = Frame(inicio, width=300, height=500, bg='#57E389')
frame1.pack()

inicioSesion = Label(frame1, text="Inicio de Sesión",
                     font=("ABeeZee", 20), bg='#57E389')
inicioSesion.grid(row=0, padx=10, pady=10)

usuarioLabel = Label(frame1, text="Usuario:",
                     font=("ABeeZee", 12), bg='#57E389')
usuarioLabel.grid(row=1, pady=5)

contrasenaLabel = Label(frame1, text="Contraseña:",
                        font=("ABeeZee", 12), bg='#57E389')
contrasenaLabel.grid(row=3, pady=5)

nombreUsuario = StringVar()
usuarioEntry = Entry(frame1, textvariable=nombreUsuario, font=("ABeeZee", 12))
usuarioEntry.grid(row=2)

contrasenaUsuario = StringVar()
contrasenaEntry = Entry(
    frame1, textvariable=contrasenaUsuario, font=("ABeeZee", 12))
contrasenaEntry.grid(row=4)
contrasenaEntry.config(show="*")

frame2 = Frame(inicio, bg='#57E389')
frame2.pack()

botonAceptar = Button(frame2, text="Aceptar",
                      command=lambda: botonAceptarClick(), font=("ABeeZee", 10))
botonAceptar.config(bg='coral')
botonAceptar.grid(column=0, row=0, padx=5, pady=10)


botonRegistro = Button(frame2, text="Registro",
                       command=lambda: botonRegistroClick(), font=("ABeeZee", 10))
botonRegistro.config(bg='#4295f5')
botonRegistro.grid(column=1, row=0, padx=5, pady=10)


# Acciones del botón Registro
def botonRegistroClick():
    inicio.destroy()
    import registro


# metodo comprueba que el usuario y la contraseña son correctos


# Acciones del botón Aceptar
def botonAceptarClick():
    if comprobarInicioSesion(usuarioEntry.get(), contrasenaEntry.get(),'data'):
        inicio.destroy()
        import principal
    else:
        messagebox.showerror(
            "Error", "El usuario o la contraseña son incorrectos")


inicio.mainloop()
