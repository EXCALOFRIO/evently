from tkinter import *
    
raiz=Tk()
raiz.title("EVENTLY")
raiz.config(width=500, height=500)
    
frame1=Frame(raiz, width=300, height=500)#,bg="lightblue")
frame1.pack()

inicioSesion=Label(frame1, text="Inicio de Sesión", font=("Arial", 16))
inicioSesion.grid(row=0, padx=10, pady=10)

usuarioLabel=Label(frame1, text="Usuario:")
usuarioLabel.grid(row=1, pady=5)

contrasenaLabel=Label(frame1, text="Contraseña:")
contrasenaLabel.grid(row=3, pady=5)

nombreUsuario=StringVar()
usuarioEntry=Entry(frame1, textvariable=nombreUsuario)
usuarioEntry.grid(row=2)

contrasenaUsuario=StringVar()
contrasenaEntry=Entry(frame1, textvariable=contrasenaUsuario)
contrasenaEntry.grid(row=4)
contrasenaEntry.config(show="*")

frame2=Frame(raiz)
frame2.pack()

botonAceptar=Button(frame2, text="Aceptar")
botonAceptar.grid(column=0, row=0, padx=5, pady=10)

botonRegistro=Button(frame2, text="Registro")
botonRegistro.grid(column=1, row=0, padx=5, pady=10)


raiz.mainloop()
