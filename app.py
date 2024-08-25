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

        # Crear la vista primero
        self.vistaPrincipal = VistaPrincipal(self.root)  # Inicializar la vista sin controlador
        self.controllerPrincipal = MainController(self.vistaPrincipal)

        # Crear el controlador después de la vista

        # Asignar el controlador a la vista
        self.vistaPrincipal.set_controller(self.controllerPrincipal)


    def run(self):
        self.root.mainloop()
