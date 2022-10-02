import tkinter as tk


class Resennas():
    def __init__(self):

        self.main_window = tk.Tk()

        self.main_window.title("EVENTLY")
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.columnconfigure(1, weight=3)
        self.main_window.rowconfigure(0, weight=100)
        self.main_window.rowconfigure(1, weight=1)

        self.leftframe = tk.Label(
            self.main_window, text='Valoraciones', bg="#FFA500")
        self.leftframe.grid(row=0, column=0, sticky='nsew')

        self.rightframe = tk.Label(
            self.main_window, text='Reseñas', bg="#1E90FF")
        self.rightframe.grid(row=0, column=1, sticky='nsew')

        self.txtbox = tk.Text(self.main_window)
        self.txtbox.grid(row=1, column=0, sticky='nsew', columnspan=2)

        self.main_window.mainloop()


resenna = Resennas()
