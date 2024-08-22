from models.grafo import Grafo

class MainController:
    def __init__(self, view):
        self.view = view
        self.graph = Grafo()
        
        self.nodo_seleccionado = 10 # pocicion inicial conejo
        # 1 perros 2 liebre
        self.turno = 2
        self.conejo_nodo = 10
        self.perro1_nodo = 2
        self.perro2_nodo = 6
        self.perro3_nodo = 12

        self.perro1_column = 200

        self.view.dibujar_tablero()
        self.view.dibujar_nodos_y_relaciones(self.graph.nodos, self.graph.relaciones)
        self.view.dibujar_conejo(self.graph.nodos[self.conejo_nodo])
        self.perro1_text = self.view.dibujar_perro(self.graph.nodos[self.perro1_nodo], "Perro1")
        self.perro2_text = self.view.dibujar_perro(self.graph.nodos[self.perro2_nodo], "Perro2")
        self.perro3_text = self.view.dibujar_perro(self.graph.nodos[self.perro3_nodo], "Perro3")

        self.view.canvas.bind("<Button-1>", self.mostrar_mensaje)

    def mostrar_mensaje(self, event):
        item = self.view.canvas.find_closest(event.x, event.y)
        print("[+] Item: " , item)
        tags = self.view.canvas.gettags(item)
        print("[+] Tags: ", tags )

        if tags:
            nodo = int(tags[0])
            if self.graph.estan_conectados(self.nodo_seleccionado, nodo):
                mensaje = f"Los nodos {self.nodo_seleccionado} y {nodo} están conectados."
                self.nodo_seleccionado = nodo
                print("[+]", mensaje)
                
                if self.turno == 2:
                    self.turnoConejo(nodo)
                #else:
                 #   self.turnoPerro(nodo)
            else:
                mensaje = f"Los nodos {self.nodo_seleccionado} y {nodo} NO están conectados."
                print("[-]", mensaje)
            self.view.mensaje_label.config(text=mensaje)
            
    def turnoConejo(self,nodo):
        if nodo != self.perro1_nodo and nodo != self.perro2_nodo and nodo != self.perro3_nodo:
            self.mover_conejo(nodo)
            #self.cambiarTurno(2)

    def turnoPerro(self, nodo):
        if nodo != self.conejo_nodo:
            if nodo == self.perro1_nodo or nodo in self.graph.grafo[self.perro1_nodo]:
                y, x = self.graph.nodos[nodo]
                
                if self.perro1_column < y:
                    self.mover_perro(nodo)
                    self.cambiarTurno(1)
                else: 
                    self.perro1_column = y

    def mover_conejo(self, nuevo_nodo):
        self.view.mover(self.view.conejo_text, self.graph.nodos[nuevo_nodo])
        self.conejo_nodo = nuevo_nodo

    def mover_perro(self, nuevo_nodo):
        self.view.mover(self.perro1_text, self.graph.nodos[nuevo_nodo])
        self.perro1_nodo = nuevo_nodo
    def cambiarTurno(self, turno):
        if turno == 2:
            self.turno = 1
            self.view.mostrarTurno("perro")
        if turno == 1:
            self.turno = 2
            self.view.mostrarTurno("liebre")
        

