from re import L
from tkinter import *
from tkinter import messagebox

from firebase_admin import db


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

apellidosLbl=Label(frame1, text="Apellido:", font=("Arial", 12))
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


botonAceptar=Button(frame2, text="Aceptar",command=lambda:botonAceptarClick(), font=("Arial", 12))
botonAceptar.pack()
#botonAtrás=Button(frame2, text="Atrás",command=lambda:botonAceptarClick(), font=("Arial", 12))
#botonAceptar.pack()

#Método para comprobar que los datos escritos son correctos: el usuario no existe, el email no está vinculado a otro usuario y todos los campos están llenos            
def comprobarUsuario(usuario,nombre,apellido,edad,email,contraseña):
    usuarios = db.reference('data/usuarios')
    #comprueba que no estan en uso ni el usuario y el email introducidos por el usuario estan en la base de datos y tambien q los campos no esten vacios
    for i in usuarios.get():
        if usuarios.get()[i]['usuario'] == usuario:
            print('El usuario ya existe')
            return False
        elif usuarios.get()[i]['email'] == email:
            print('El email ya existe')
            return False
        elif usuario == '' or nombre == '' or apellido == '' or edad == '' or email == '' or contraseña == '':
            print('No puede haber campos vacios')
            return False
    insertarUsuario(usuario,nombre,apellido,edad,email,contraseña)
    return True

#Método para insertar un usuario nuevo en la base de datos
def insertarUsuario(usuario, nombre, apellido, edad, email, contraseña):
    usuarios = {
        'usuario': usuario,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'email': email,
        'contraseña': contraseña
    }

    db.reference('data').child('usuarios').push(usuarios)

#Acciones del boton Aceptar
def botonAceptarClick():
    if comprobarUsuario(usuario.get(), nombre.get(), apellidos.get(), edad.get(), email.get(), contrasena.get()):
        messagebox.showinfo("Registro", "Usuario registrado correctamente")
        raiz.destroy()
        #import inicio
    else:
        messagebox.showerror("Error", 
                             "Los datos introducidos no son correctos, por favor inténtelo de nuevo.")

raiz.mainloop()