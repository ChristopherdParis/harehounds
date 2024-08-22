import tkinter as tk
from views.vistaPrincipal import VistaPrincipal
from controllers.mainController import MainController

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Juego cazaodr")
        self.root.geometry("600x600")
        self.root.minsize(600, 600)
        #self.root.configure(bg="#bbccaa")

        self.vistaPrincipal = VistaPrincipal(self.root)
        self.controllerPrincipal = MainController(self.vistaPrincipal)

    def run(self):
        self.root.mainloop()
