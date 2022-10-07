import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from baseDatosPrueba import insertarValoracion
cred = credentials.Certificate("firebase/evently-key.json")

import pyglet

pyglet.font.add_file('fuentes/productSans.ttf')  # ABeeZee

class Resennas():
    def __init__(self):

        self.main_window = tk.Tk()

        self.main_window.title("EVENTLY")
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.columnconfigure(1, weight=3)
        self.main_window.rowconfigure(0, weight=100)

        # Creacion del cuadro de la izquierda que contiene las valoraciones
        self.leftframe = tk.Frame(
            self.main_window, bg="#FFA500")
        self.leftframe.grid(row=0, column=0, sticky='nsew')

        # Titulo frame izquierdo
        self.leftTitle = tk.Label(
            self.leftframe, text='Escriba una Reseña', font=('ABeeZee', 30))
        self.leftTitle.pack()

        # Usuario
        self.usuario = tk.Label(
            self.leftframe, text='Usuario:', font=('ABeeZee', 18))
        self.usuario.pack()

        self.usuarioEntry = tk.Entry(self.leftframe)
        self.usuarioEntry.pack()

        # Discoteca
        self.discoteca = tk.Label(
            self.leftframe, text='Discoteca:', font=('ABeeZee', 18))
        self.discoteca.pack()

        self.discotecaEntry = tk.Entry(self.leftframe)
        self.discotecaEntry.pack()
        # Caja de texto para escribir reseñas
        self.txtbox = tk.Text(self.leftframe, height=15,
                              width=30, font=('ABeeZee', 22))
        self.txtbox.pack(pady=10)

        # Botones de seleccion de valoración
        self.opcion = tk.IntVar()

        self.val1 = tk.Radiobutton(self.leftframe, text="1 Estrella", variable=self.opcion,
                                   value=1, command=self.seleccion)
        self.val2 = tk.Radiobutton(self.leftframe, text="2 Estrellas", variable=self.opcion,
                                   value=2, command=self.seleccion)
        self.val3 = tk.Radiobutton(self.leftframe, text="3 Estrellas", variable=self.opcion,
                                   value=3, command=self.seleccion)
        self.val4 = tk.Radiobutton(self.leftframe, text="4 Estrellas", variable=self.opcion,
                                   value=4, command=self.seleccion)
        self.val5 = tk.Radiobutton(self.leftframe, text="5 Estrellas", variable=self.opcion,
                                   value=5, command=self.seleccion)
        self.val1.pack()
        self.val2.pack()
        self.val3.pack()
        self.val4.pack()
        self.val5.pack()

        # Boton para añadir reseña
        self.boton = tk.Button(self.leftframe, text='Añadir reseña', font=(
            'ABeeZee', 16), command=self.validarResenna)
        self.boton.pack(pady=10)
        # Creacion del cuadro de la derecha que contiene las reseñas
        self.rightframe = tk.Frame(
            self.main_window, bg="#1E90FF")
        self.rightframe.grid(row=0, column=1, sticky='nsew')

        self.rightTitle = tk.Label(
            self.rightframe, text='Reseñas de otros usuarios', font=('ABeeZee', 30))
        self.rightTitle.pack()

        self.resennas = tk.Label(self.rightframe, text=str(
            self.getValoraciones()), font=('ABeeZee', 18))
        self.resennas.pack(pady=10)

        self.main_window.mainloop()

    # Metodo que checkea que opcion ha sido escogida en el radiobutton
    def seleccion(self):
        return self.opcion.get()

    # Metodo que obtiene las reseñas de la base de datos
    def getValoraciones(self):
        valoraciones = db.reference('data/valoraciones')
        text = []
        for i in valoraciones.get():
            text.append(valoraciones.get()[i])
        return text

    # Metodo que checkea que los campos no esten vacios y sube la reseña a la base de datos
    def validarResenna(self):
        if self.txtbox.get('1.0', tk.END) != '' and self.usuarioEntry.get() != '' and self.discotecaEntry.get() != '' and self.opcion.get() != None:
            message = self.txtbox.get('1.0', tk.END)
            valoracion = self.opcion.get()
            discoteca = self.discotecaEntry.get()
            user = self.usuarioEntry.get()
            insertarValoracion(user, discoteca, valoracion, message,'data')
        else:
            messagebox.showinfo(
                title='Message', message='Introduce todos los campos para añadir una reseña')


resenna = Resennas()
