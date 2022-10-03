from re import L
from tkinter import *
from tkinter import messagebox

from baseDatosPrueba import comprobarUsuario

raiz=Tk()
raiz.geometry("600x300")
raiz.title("REGISTRO")

frame=Frame(raiz, bg="lightblue")
frame.pack()

eventlyLbl=Label(frame, text="EVENTLY", font=("Arial", 14), pady=10)
eventlyLbl.pack()



frame1=Frame(raiz)
frame1.pack()

usuarioLbl=Label(frame1, text="Usuario:", font=("Arial", 12))
usuarioLbl.grid(column=0, row=0, padx=5, pady=5)

nombreLbl=Label(frame1, text="Nombre:", font=("Arial", 12))
nombreLbl.grid(column=0, row=1, padx=5, pady=5)

apellidosLbl=Label(frame1, text="Apellidos:", font=("Arial", 12))
apellidosLbl.grid(column=0, row=2, padx=5, pady=5)

contrasenaLbl=Label(frame1, text="Contraseña:", font=("Arial", 12))
contrasenaLbl.grid(column=2, row=0, padx=5, pady=5)

emailLbl=Label(frame1, text="E-mail:", font=("Arial", 12))
emailLbl.grid(column=2, row=1, padx=5, pady=5)

edadLbl=Label(frame1, text="Edad:", font=("Arial", 12))
edadLbl.grid(column=2, row=2, padx=5, pady=5)

usuario=StringVar()
usuarioEntry=Entry(frame1, text=usuario, font=("Arial", 12))
usuarioEntry.grid(column=1, row=0, padx=5, pady=5)

nombre=StringVar()
nombreEntry=Entry(frame1, text=nombre, font=("Arial", 12))
nombreEntry.grid(column=1, row=1, padx=5, pady=5)

apellidos=StringVar()
apellidosEntry=Entry(frame1, text=apellidos, font=("Arial", 12))
apellidosEntry.grid(column=1, row=2, padx=5, pady=5)

contrasena=StringVar()
contrasenaEntry=Entry(frame1, text=contrasena, font=("Arial", 12))
contrasenaEntry.grid(column=3, row=0, padx=5, pady=5)
contrasenaEntry.config(show="*")

email=StringVar()
emailEntry=Entry(frame1, text=email, font=("Arial", 12))
emailEntry.grid(column=3, row=1, padx=5, pady=5)

edad=IntVar()
edadEntry=Entry(frame1, text=edad, font=("Arial", 12))
edadEntry.grid(column=3, row=2, padx=5, pady=5)

frame2=Frame(raiz, pady=20)
frame2.pack()
#Estructura de la tabla usuario
#def comprobarUsuario(usuario, nombre, apellido, edad, email, contraseña)

botonAceptar=Button(frame2, text="Aceptar",command=lambda:botonAceptarClick(), font=("Arial", 12))
botonAceptar.pack()

def botonAceptarClick():
    if comprobarUsuario(usuario.get(), nombre.get(), apellidos.get(), edad.get(), email.get(), contrasena.get()):
        raiz.destroy()
        import inicio
    else:
        messagebox.showerror("Error", "El usuario o el correo ya estan en uso")


raiz.mainloop()