from models.grafo import Grafo

class MainController:
    def __init__(self, view):
        self.view = view
        self.graph = Grafo()
        
        self.nodo_seleccionado_conejo = 10 # pocicion inicial conejo
        self.nodo_seleccionado_perros = None # pocicion inicial perros
        
        self.conejo_nodo = 10
        self.perro1_nodo = 2
        self.perro2_nodo = 6
        self.perro3_nodo = 12

        self.perro1_column = 200
        self.perro2_column = 100
        self.perro3_column = 200
        if self.view:
            # 1 perros 2 liebre
            self.turno = None

            self.view.dibujar_tablero()
            self.view.dibujar_nodos_y_relaciones(self.graph.nodos, self.graph.relaciones)

            self.view.dibujar_conejo(self.graph.nodos[self.conejo_nodo], "Liebre")
            self.perro1_text = self.view.dibujar_perro(self.graph.nodos[self.perro1_nodo], "Perro1")
            self.perro2_text = self.view.dibujar_perro(self.graph.nodos[self.perro2_nodo], "Perro2")
            self.perro3_text = self.view.dibujar_perro(self.graph.nodos[self.perro3_nodo], "Perro3")

            

    def iniciar_juego(self):
        seleccion = self.view.jugador_inicial.get()
        if seleccion == "perros":
            self.turno = seleccion
            self.view.canvas.bind("<Button-1>", self.mostrar_mensaje)
            print("El juego inicia con los Perros.")
            # Lógica para mover perros primero
        elif seleccion == "liebre":
            self.turno = seleccion
            self.view.canvas.bind("<Button-1>", self.mostrar_mensaje)
            print("El juego inicia con la Liebre.")
            # Lógica para mover liebre primero
        else:
            print("El juego inicia con la Liebre.")
            # Lógica para mover liebre primero
        self.view.mostrarTurno(seleccion)

    def help(self):
        print("[+] necesito aiuda")

    def mostrar_mensaje(self, event):
        item = self.view.canvas.find_closest(event.x, event.y)
        tags = self.view.canvas.gettags(item)
        print("[+] Turno: ", self.turno)

        if tags:
            nodo = int(tags[0])
            if self.turno == "liebre":
                if self.graph.estan_conectados(self.nodo_seleccionado_conejo, nodo):
                    print(f"Los nodos {self.nodo_seleccionado_conejo} y {nodo} están conectados.")
                    self.nodo_seleccionado_conejo = nodo
                    self.turnoConejo(nodo)
                else:
                    print(f"Los nodos conejo {self.nodo_seleccionado_conejo} y {nodo} NO están conectados.")
            elif self.turno == "perros":
                print("somos perros y toca a los perros")
                self.logicaperros(nodo)

    def turnoConejo(self,nodo):
        if nodo != self.perro1_nodo and nodo != self.perro2_nodo and nodo != self.perro3_nodo:
            self.mover_conejo(nodo)
            self.cambiarTurno(1)
        else :
            print("[+] fin del juego ganan los perrois")
    
    def logicaperros(self, nodo):
        if self.nodo_seleccionado_perros is None:
            if nodo in [self.perro1_nodo, self.perro2_nodo, self.perro3_nodo]:
                self.nodo_seleccionado_perros = nodo
                print(f"Perro {nodo} seleccionado. Ahora elige el nodo destino.")
            else:
                print(f"El nodo seleccionado {nodo} no corresponde a la posición de ningún perro.")
        else:
            perro_seleccionado = self.nodo_seleccionado_perros
            if self.graph.estan_conectados(perro_seleccionado, nodo):
                if perro_seleccionado == self.perro1_nodo:
                    self.turnoPerro1(nodo)
                elif perro_seleccionado == self.perro2_nodo:
                    self.turnoPerro2(nodo)
                elif perro_seleccionado == self.perro3_nodo:
                    self.turnoPerro3(nodo)
            else:
                print(f"Los nodos {perro_seleccionado} y {nodo} no están conectados. No se puede mover.")
    
    
    
    def turnoPerro1(self, nodo):
        self.mover_perro_si_valido(nodo, self.perro1_nodo, self.perro1_column, 1)

    def turnoPerro2(self, nodo):
        self.mover_perro_si_valido(nodo, self.perro2_nodo, self.perro2_column, 2)

    def turnoPerro3(self, nodo):
        self.mover_perro_si_valido(nodo, self.perro3_nodo, self.perro3_column, 3)

    
    def mover_perro_si_valido(self, nodo, perro_nodo, perro_columna, numero_perro):
        if nodo != self.conejo_nodo:
            if nodo == perro_nodo or nodo in self.graph.grafo[perro_nodo]:
                y, x = self.graph.nodos[nodo]

                if y >= perro_columna:
                    print(f"Moviendo el perro {numero_perro} de {perro_nodo} a {nodo}.")
                    self.actualizar_posicion_perro(nodo, numero_perro)
                    self.cambiarTurno(2)
                else:
                    print("No puedes retroceder a una columna menor que la actual")
            else:
                print(f"Movimiento inválido para el perro {numero_perro}.")
        else:
            print("No puedes ponerte en el nodo del conejo", self.conejo_nodo)

        self.nodo_seleccionado_perros = None

    def actualizar_posicion_perro(self, nuevo_nodo, numero_perro):
        if numero_perro == 1:
            self.mover_perro1(nuevo_nodo)
            self.perro1_nodo = nuevo_nodo
            self.perro1_column = self.graph.nodos[nuevo_nodo][0]
        elif numero_perro == 2:
            self.mover_perro2(nuevo_nodo)
            self.perro2_nodo = nuevo_nodo
            self.perro2_column = self.graph.nodos[nuevo_nodo][0]
        elif numero_perro == 3:
            self.mover_perro3(nuevo_nodo)
            self.perro3_nodo = nuevo_nodo
            self.perro3_column = self.graph.nodos[nuevo_nodo][0]
    
    def mover_perro1(self, nuevo_nodo):
        self.view.mover(self.perro1_text, self.graph.nodos[nuevo_nodo])
        
    
    def mover_perro2(self, nuevo_nodo):
        self.view.mover(self.perro2_text, self.graph.nodos[nuevo_nodo])
        
    
    def mover_perro3(self, nuevo_nodo):
        self.view.mover(self.perro3_text, self.graph.nodos[nuevo_nodo])
        
 

    def cambiarTurno(self, turno):
        if turno == 2:
            self.turno = "liebre"
            self.view.mostrarTurno("liebre")
        if turno == 1:
            self.turno = "perros"
            self.view.mostrarTurno("perros")

    def mover_conejo(self, nuevo_nodo):
        self.view.mover(self.view.conejo_text, self.graph.nodos[nuevo_nodo])
        self.conejo_nodo = nuevo_nodo

    
    '''
    def mostrar_mensaje(self, event):
        item = self.view.canvas.find_closest(event.x, event.y)
        tags = self.view.canvas.gettags(item)
        print("[+] Turno: " , self.turno)
        

        if tags:
            nodo = int(tags[0])
            if self.turno == "liebre":

                if self.graph.estan_conectados(self.nodo_seleccionado_conejo, nodo):
                    mensaje = f"Los nodos {self.nodo_seleccionado_conejo} y {nodo} están conectados."
                    self.nodo_seleccionado_conejo = nodo
                    self.turnoConejo(nodo)
                else:
                    mensaje = f"Los nodos conejo {self.nodo_seleccionado_conejo} y {nodo} NO están conectados."
                    #print("[-]", mensaje)
            elif self.turno == "perros":
                print("somos perros y toca a los perros")
                self.logicaperros(nodo)
            else:
                if self.graph.estan_conectados(self.nodo_seleccionado_perros, nodo):
                    mensaje = f"Los nodos perro {self.nodo_seleccionado_perros} y {nodo} están conectados."
                    
                    #print("[+]", mensaje)
                    self.turnoPerro(nodo)
                else:
                    mensaje = f"Los perro nodos {self.nodo_seleccionado_perros} y {nodo} NO están conectados."
                    print("[-]", mensaje)

    def logicaperros(self,nodo):
        # Verifica si un perro ya ha sido seleccionado
        if self.nodo_seleccionado_perros is None:
            # Paso 1: Selección del perro
            if nodo in [self.perro1_nodo, self.perro2_nodo, self.perro3_nodo]:
                self.nodo_seleccionado_perros = nodo
                print(f"Perro {nodo} seleccionado. Ahora elige el nodo destino.")
            else:
                print(f"El nodo seleccionado {nodo} no corresponde a la posición de ningún perro.")
        else:
            # Paso 2: Movimiento del perro seleccionado
            perro_seleccionado = self.nodo_seleccionado_perros
            print("resultado si el perro selecionado", self.graph.estan_conectados(perro_seleccionado, nodo))
            if self.graph.estan_conectados(perro_seleccionado, nodo):
                print(f"Moviendo el perro de {perro_seleccionado} a {nodo}.")
                if perro_seleccionado == self.perro1_nodo:
                    print(" el perro selecionado es el 1")
                    self.turnoPerro1(nodo)
                    #self.perro1_nodo = nodo
                elif perro_seleccionado == self.perro2_nodo:
                    #self.perro2_nodo = nodo
                    print(" el perro selecionado es el 2")
                    self.turnoPerro2(nodo)
                elif perro_seleccionado == self.perro3_nodo:
                    print(" el perro selecionado es el 3")
                    self.turnoPerro3(nodo)
                    #self.perro3_nodo = nodo
                
                self.nodo_seleccionado_perros = None
            else:
                print(f"Los nodos {perro_seleccionado} y {nodo} no están conectados. No se puede mover.")
    '''
        
            
    
    '''
    def turnoPerro1(self, nodo):
        print("==========duncion turnoperro=========== => ",nodo)
        print("conejo nodo => ", self.conejo_nodo)
        if nodo != self.conejo_nodo:
            if nodo == self.perro1_nodo or nodo in self.graph.grafo[self.perro1_nodo]:
                y, x = self.graph.nodos[nodo]
                
                if y >= self.perro1_column:
                    print("columna perro y es mayor ", y)
                    print("columna perro ", self.perro1_column)
                    print("estado", y >= self.perro1_column)
                    self.nodo_seleccionado_perros = nodo
                    self.mover_perro(nodo)
                    self.perro1_column = y
                    self.cambiarTurno(2)
                else: 
                    print("estado", y >= self.perro1_column)
                    print("No puedes retroceder a una columna menor que la actual")

                    #self.perro1_column = y
        else:
            print("no puedes ponerte en el nodo del conejo", self.conejo_nodo)

    def turnoPerro2(self, nodo):
        print("==========duncion turnoperro=========== => ",nodo)
        print("conejo nodo => ", self.conejo_nodo)
        if nodo != self.conejo_nodo:
            if nodo == self.perro2_nodo or nodo in self.graph.grafo[self.perro2_nodo]:
                y, x = self.graph.nodos[nodo]
                
                if y >= self.perro2_column:
                    print("columna perro y es mayor ", y)
                    print("columna perro ", self.perro2_column)
                    print("estado", y >= self.perro2_column)
                    self.nodo_seleccionado_perros = nodo
                    self.mover_perro2(nodo)
                    self.perro2_column = y
                    self.cambiarTurno(2)
                else: 
                    print("estado", y >= self.perro2_column)
                    print("No puedes retroceder a una columna menor que la actual")

                    #self.perro1_column = y
        else:
            print("no puedes ponerte en el nodo del conejo", self.conejo_nodo)

    def turnoPerro3(self, nodo):
        print("==========duncion turnoperro=========== => ",nodo)
        print("conejo nodo => ", self.conejo_nodo)
        if nodo != self.conejo_nodo:
            if nodo == self.perro3_nodo or nodo in self.graph.grafo[self.perro3_nodo]:
                y, x = self.graph.nodos[nodo]
                
                if y >= self.perro3_column:
                    print("columna perro y es mayor ", y)
                    print("columna perro ", self.perro3_column)
                    print("estado", y >= self.perro3_column)
                    self.nodo_seleccionado_perros = nodo
                    self.mover_perro3(nodo)
                    self.perro3_column = y
                    self.cambiarTurno(2)
                else: 
                    print("estado", y >= self.perro3_column)
                    print("No puedes retroceder a una columna menor que la actual")

                    #self.perro2_column = y
        else:
            print("no puedes ponerte en el nodo del conejo", self.conejo_nodo)
    '''

    