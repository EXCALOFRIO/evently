from re import L
from tkinter import *
from tkinter import messagebox

from firebase_admin import db

from baseDatosPrueba import insertarDiscoteca


raiz = Tk()
raiz.geometry("600x300")
raiz.title("AÑADIENDO VALORACIÓN")

frame = Frame(raiz, bg="lightblue")
frame.pack()

eventlyLbl = Label(frame, text="EVENTLY", font=("Arial", 14), pady=10)
eventlyLbl.pack()

frame1 = Frame(raiz)
frame1.pack()

# Crea un selector de elementos


def crearSelector(frame, texto, lista):
    label = Label(frame, text=texto, font=("Arial", 12))
    label.grid(column=0, row=0, padx=5, pady=5)
    selector = StringVar()
    selector.set(lista[0])
    selector = OptionMenu(frame, selector, *lista)
    # modifica tamaño del OptionMenu para que se vea bien
    selector.config(width=15, font=('Helvetica', 12))
    selector.grid(column=1, row=0, padx=5, pady=5)
    # modificca tamaño selector para que se vea bien
    selector["menu"].config(font=('Helvetica', 12))

    return selector

# crea un metodo para devolver todos los nombres de las discotecas y con el resultao llamar a la funcin crearSelector


def getDiscotecas():
    discotecas = db.reference('data/discotecas')
    listaDiscotecas = []
    for i in discotecas.get():
        # crea una lista de discotecas que se llama litaDiscotecas
        listaDiscotecas.append(discotecas.get()[i]['nombre'])
    return(listaDiscotecas)


# llamada a la función
crearSelector(frame1, "Discoteca:", getDiscotecas())

zonaLbl = Label(frame1, text="Zona:", font=("Arial", 12))
zonaLbl.grid(column=0, row=1, padx=5, pady=5)

calleLbl = Label(frame1, text="Calle:", font=("Arial", 12))
calleLbl.grid(column=0, row=2, padx=5, pady=5)

numeroLbl = Label(frame1, text="Numero:", font=("Arial", 12))
numeroLbl.grid(column=0, row=3, padx=5, pady=5)


zona = StringVar()
zonaEntry = Entry(frame1, text=zona, font=("Arial", 12))
zonaEntry.grid(column=1, row=1, padx=5, pady=5)

calle = StringVar()
calleEntry = Entry(frame1, text=calle, font=("Arial", 12))
calleEntry.grid(column=1, row=2, padx=5, pady=5)

numero = IntVar()
numeroEntry = Entry(frame1, text=numero, font=("Arial", 12))
numeroEntry.grid(column=1, row=3, padx=5, pady=5)

frame2 = Frame(raiz, pady=20)
frame2.pack()


botonAceptar = Button(frame2, text="Aceptar",
                      command=lambda: botonAceptarClick(), font=("Arial", 12))
botonAceptar.pack()


def comprobarDatos(nombre, zona, calle, numero):
    if nombre != "" and zona != "" and calle != "" and numero != "":
        insertarDiscoteca(nombre, zona, calle, numero)
        return True
    else:
        return False


# Acciones del boton Aceptar

def botonAceptarClick():
    if comprobarDatos(nombre.get(), zona.get(), calle.get(), numero.get()):
        messagebox.showinfo("Datos", "Discoteca registrada correctamente")
        raiz.destroy()
        #import inicio
    else:
        messagebox.showerror("Error",
                             "Los datos introducidos no son correctos, por favor inténtelo de nuevo.")


raiz.mainloop()
