import tkinter as tk
from controllers.mainController import MainController
class VistaPrincipal:
    def __init__(self, root):
        self.root = root
        self.controller = None
        self.canvas = tk.Canvas(root, bg="#bbccaa")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.frame_principal = tk.Frame(self.root, bd=2, relief="ridge", padx=10, pady=10)
        self.frame_principal.pack(padx=10, pady=10)

        self.turno_text = None
        self.turno_animal = None

        self.conejo_text = None
        self.perro1_text = None
        self.perro2_text = None
        self.perro3_text = None
         
        # Variable para guardar la opción seleccionada
        self.jugador_inicial = tk.StringVar()
        #self.jugador_inicial.set(1) 
    def set_controller(self, controller):

        self.controller = controller
        self.configurar_botones()
    
    def configurar_botones(self):
        
        # Crear un Frame inferior para los botones y marcador
        self.frame_botones = tk.Frame(self.frame_principal)
        self.frame_botones.grid(row=1, column=0, columnspan=3)

        # Botón "New"
        self.boton_new = tk.Button(self.frame_botones, text="New", command=self.controller.iniciar_juego)
        self.boton_new.grid(row=0, column=0)

        # Marcador
        self.label_marcador = tk.Label(self.frame_botones, text="0", relief="sunken", width=5)
        self.label_marcador.grid(row=0, column=1, padx=10)

        # Botón "Help"
        self.boton_help = tk.Button(self.frame_botones, text="Help", command=self.controller.help)
        self.boton_help.grid(row=0, column=2)



    def dibujar_nodos_y_relaciones(self, nodos, relaciones):
        for nombre, (x, y) in nodos.items():
            self.canvas.create_oval(x-30, y-30, x+30, y+30, fill="gray", outline="gray", tags=(nombre,))
            self.canvas.create_text(x, y, text=nombre, font=("Arial", 16), tags=(nombre,))

        for nodo1, nodo2 in relaciones:
            x1, y1 = nodos[nodo1]
            x2, y2 = nodos[nodo2]
            self.canvas.create_line(x1, y1, x2, y2, fill="brown", width=1)

    def dibujar_conejo(self, posicion, texto):
        x, y = posicion
        self.conejo_text = self.canvas.create_text(x, y, text=texto, font=("Arial", 12), fill="red")

    def dibujar_perro(self, posicion, texto):
        x, y = posicion
        return self.canvas.create_text(x, y, text=texto, font=("Arial", 12), fill="green")

    def mover(self, text_id, posicion):
        x, y = posicion
        print("Posicion" , posicion)
        self.canvas.coords(text_id, x, y)

    def dibujar_tablero(self):
        self.canvas.create_text(50, 20, text="Turno: ", font=("Arial", 12), fill="black")
        
        # Crear el Frame superior para las opciones de movimiento
        self.frame_opciones = tk.Frame(self.frame_principal)
        self.frame_opciones.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # Label de instrucciones
        self.label_opciones = tk.Label(self.frame_opciones, text="Who moves first:")
        self.label_opciones.grid(row=0, column=0, columnspan=3)

        # Radiobuttons para seleccionar quién se mueve primero
        self.radio_perros = tk.Radiobutton(self.frame_opciones, text="Perros", variable=self.jugador_inicial, value="perros")
        self.radio_perros.grid(row=1, column=0)

        self.radio_liebre = tk.Radiobutton(self.frame_opciones, text="Liebre", variable=self.jugador_inicial, value="liebre")
        self.radio_liebre.grid(row=1, column=2)

        # Label que actúa como separador entre los Radiobuttons
        self.label_separator = tk.Label(self.frame_opciones, text=" ")
        self.label_separator.grid(row=1, column=1)

    def mostrarTurno(self, turno):
        
        if self.turno_text is None:
            self.turno_text = self.canvas.create_text(100, 20, text=turno, font=("Arial", 12), fill="black")
        else:
            self.canvas.itemconfig(self.turno_text, text=turno)
