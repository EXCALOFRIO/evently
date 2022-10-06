from tkinter import *

inicio = Tk()
inicio.title("INICIO")
inicio.geometry("600x350")
inicio.resizable(0, 0)

frame1 = Frame(inicio, width=300, height=500)
frame1.pack()
# añade 3 botones de colore salmón, verde y azul para añadir discotecas añadir fiestas y valoraciones
boton1 = Button(frame1, text="Añadir Discoteca",
                command=lambda: botonDicotecaClick(), font=("Arial", 10))
boton1.grid(column=0, row=0, padx=20, pady=30)

boton2 = Button(frame1, text="Añadir Fiestas",
                command=lambda: botonFiestaClick(), font=("Arial", 10))
boton2.grid(column=1, row=0, padx=20, pady=30)

boton3 = Button(frame1, text="Añadir Valoraciones",
                command=lambda: botonValoracionClick(), font=("Arial", 10))
boton3.grid(column=2, row=0, padx=20, pady=30)


# Acciones del botón Discoteca
def botonDicotecaClick():
    inicio.destroy()
    import añadirDiscoteca

# Acciones del botón Fiesta


def botonFiestaClick():
    inicio.destroy()
    import añadirDiscoteca

# Acciones del botón Valoracion


def botonValoracionClick():
    inicio.destroy()
    import reseñas


inicio.mainloop()
