from tkinter import *
from tkinter import messagebox

from baseDatosPrueba import comprobarInicioSesion


raiz = Tk()
raiz.title("EVENTLY")
raiz.geometry("300x350")
raiz.resizable(0, 0)

frame1 = Frame(raiz, width=300, height=500)
frame1.pack()

inicioSesion = Label(frame1, text="Inicio de Sesión", font=("Arial", 20))
inicioSesion.grid(row=0, padx=10, pady=10)

usuarioLabel = Label(frame1, text="Usuario:", font=("Arial", 12))
usuarioLabel.grid(row=1, pady=5)

contrasenaLabel = Label(frame1, text="Contraseña:", font=("Arial", 12))
contrasenaLabel.grid(row=3, pady=5)

nombreUsuario = StringVar()
usuarioEntry = Entry(frame1, textvariable=nombreUsuario, font=("Arial", 12))
usuarioEntry.grid(row=2)

contrasenaUsuario = StringVar()
contrasenaEntry = Entry(
    frame1, textvariable=contrasenaUsuario, font=("Arial", 12))
contrasenaEntry.grid(row=4)
contrasenaEntry.config(show="*")

frame2 = Frame(raiz)
frame2.pack()

botonAceptar = Button(frame2, text="Aceptar",
                      command=lambda: botonAceptarClick(), font=("Arial", 10))
botonAceptar.grid(column=0, row=0, padx=5, pady=10)


botonRegistro = Button(frame2, text="Registro",
                       command=lambda: botonRegistroClick(), font=("Arial", 10))
botonRegistro.grid(column=1, row=0, padx=5, pady=10)


# Acciones del botón Registro
def botonRegistroClick():
    raiz.destroy()
    import registro


# Acciones del botón Aceptar
def botonAceptarClick():
    if comprobarInicioSesion(usuarioEntry.get(), contrasenaEntry.get()):
        raiz.destroy()
        import principal
    else:
        messagebox.showerror(
            "Error", "El usuario o la contraseña son incorrectos")


raiz.mainloop()
