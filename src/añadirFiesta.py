from re import L
from tkinter import *
from tkinter import messagebox

from firebase_admin import db

from baseDatosPrueba import insertarDiscoteca, insertarFiesta
# pip install pyglet
import pyglet

pyglet.font.add_file('fuentes/productSans.ttf')  # ABeeZee

raiz = Tk()
raiz.geometry("600x300")
raiz.title("AÑADIENDO FIESTA")

frame = Frame(raiz, bg="lightblue")
frame.pack()

eventlyLbl = Label(frame, text="EVENTLY", font=("ABeeZee", 14), pady=10)
eventlyLbl.pack()

frame1 = Frame(raiz)
frame1.pack()

nombreLbl = Label(frame1, text="Nombre:", font=("ABeeZee", 12))
nombreLbl.grid(column=0, row=0, padx=5, pady=5)

zonaLbl = Label(frame1, text="Zona:", font=("ABeeZee", 12))
zonaLbl.grid(column=0, row=1, padx=5, pady=5)

calleLbl = Label(frame1, text="Calle:", font=("ABeeZee", 12))
calleLbl.grid(column=0, row=2, padx=5, pady=5)

numeroLbl = Label(frame1, text="Numero:", font=("ABeeZee", 12))
numeroLbl.grid(column=0, row=3, padx=5, pady=5)

nombre = StringVar()
nombreEntry = Entry(frame1, text=nombre, font=("ABeeZee", 12))
nombreEntry.grid(column=1, row=0, padx=5, pady=5)

zona = StringVar()
zonaEntry = Entry(frame1, text=zona, font=("ABeeZee", 12))
zonaEntry.grid(column=1, row=1, padx=5, pady=5)

calle = StringVar()
calleEntry = Entry(frame1, text=calle, font=("ABeeZee", 12))
calleEntry.grid(column=1, row=2, padx=5, pady=5)

numero = IntVar()
numeroEntry = Entry(frame1, text=numero, font=("ABeeZee", 12))
numeroEntry.grid(column=1, row=3, padx=5, pady=5)

frame2 = Frame(raiz, pady=20)
frame2.pack()


botonAceptar = Button(frame2, text="Aceptar",
                      command=lambda: botonAceptarClick(), font=("ABeeZee", 12))
botonAceptar.pack()

boton4 = Button(frame1, text="Volver atrás",
                command=lambda: botonVolverAtras(), font=("ABeeZee", 10))
boton4.grid(column=2, row=1, padx=20, pady=5)


def comprobarDatos(nombre, zona, calle, numero):
    if nombre != "" and zona != "" and calle != "" and numero != "":
        insertarFiesta(nombre, zona, calle, numero)
        return True
    else:
        return False


# Acciones del boton Aceptar

def botonAceptarClick():
    if comprobarDatos(nombre.get(), zona.get(), calle.get(), numero.get()):
        messagebox.showinfo("Datos", "Fiesta registrada correctamente")
        raiz.destroy()
        import inicio
    else:
        messagebox.showerror("Error",
                             "Los datos introducidos no son correctos, por favor inténtelo de nuevo.")


def botonVolverAtras():
    raiz.destroy()
    import principal


raiz.mainloop()
