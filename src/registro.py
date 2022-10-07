from re import L
from tkinter import *
from tkinter import messagebox

from baseDatosPrueba import comprobarUsuario

import pyglet

pyglet.font.add_file('fuentes/productSans.ttf')  # ABeeZee

raiz = Tk()
raiz.geometry("600x300")
raiz.config(bg='lightblue')
raiz.title("REGISTRO")

frame = Frame(raiz, bg="lightblue")
frame.pack()

eventlyLbl = Label(frame, text="EVENTLY", font=(
    "ABeeZee", 14), pady=10, bg="lightblue")
eventlyLbl.pack()

frame1 = Frame(raiz, bg="lightblue")
frame1.pack()

usuarioLbl = Label(frame1, text="Usuario:",
                   font=("ABeeZee", 12), bg="lightblue")
usuarioLbl.grid(column=0, row=0, padx=5, pady=5)

nombreLbl = Label(frame1, text="Nombre:", font=("ABeeZee", 12), bg="lightblue")
nombreLbl.grid(column=0, row=1, padx=5, pady=5)

apellidosLbl = Label(frame1, text="Apellido:",
                     font=("ABeeZee", 12), bg="lightblue")
apellidosLbl.grid(column=0, row=2, padx=5, pady=5)

contrasenaLbl = Label(frame1, text="Contraseña:",
                      font=("ABeeZee", 12), bg="lightblue")
contrasenaLbl.grid(column=2, row=0, padx=5, pady=5)

emailLbl = Label(frame1, text="E-mail:", font=("ABeeZee", 12), bg="lightblue")
emailLbl.grid(column=2, row=1, padx=5, pady=5)

edadLbl = Label(frame1, text="Edad:", font=("ABeeZee", 12), bg="lightblue")
edadLbl.grid(column=2, row=2, padx=5, pady=5)

usuario = StringVar()
usuarioEntry = Entry(frame1, text=usuario, font=("ABeeZee", 12))
usuarioEntry.grid(column=1, row=0, padx=5, pady=5)

nombre = StringVar()
nombreEntry = Entry(frame1, text=nombre, font=("ABeeZee", 12))
nombreEntry.grid(column=1, row=1, padx=5, pady=5)

apellidos = StringVar()
apellidosEntry = Entry(frame1, text=apellidos, font=("ABeeZee", 12))
apellidosEntry.grid(column=1, row=2, padx=5, pady=5)

contrasena = StringVar()
contrasenaEntry = Entry(frame1, text=contrasena, font=("ABeeZee", 12))
contrasenaEntry.grid(column=3, row=0, padx=5, pady=5)
contrasenaEntry.config(show="*")

email = StringVar()
emailEntry = Entry(frame1, text=email, font=("ABeeZee", 12))
emailEntry.grid(column=3, row=1, padx=5, pady=5)

edad = IntVar()
edadEntry = Entry(frame1, text=edad, font=("ABeeZee", 12))
edadEntry.grid(column=3, row=2, padx=5, pady=5)

frame2 = Frame(raiz, pady=20, bg="lightblue")
frame2.pack()


botonAceptar = Button(frame2, text="Aceptar",
                      command=lambda: botonAceptarClick(), font=("ABeeZee", 12))
botonAceptar.config(bg='coral')
botonAceptar.pack()
#botonAtrás=Button(frame2, text="Atrás",command=lambda:botonAceptarClick(), font=("ABeeZee", 12))
# botonAceptar.pack()

# Método para comprobar que los datos escritos son correctos: el usuario no existe, el email no está vinculado a otro usuario y todos los campos están llenos

# Método para insertar un usuario nuevo en la base de datos


# Acciones del boton Aceptar


def botonAceptarClick():
    if comprobarUsuario(usuario.get(), nombre.get(), apellidos.get(), edad.get(), email.get(), contrasena.get(), 'data'):
        messagebox.showinfo("Registro", "Usuario registrado correctamente")
        raiz.destroy()
        #import inicio
    else:
        messagebox.showerror("Error",
                             "Los datos introducidos no son correctos, por favor inténtelo de nuevo.")


raiz.mainloop()
