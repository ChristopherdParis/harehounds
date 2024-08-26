from models.grafo import Grafo
import numpy as np

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
            tablero = self.generar_posiciones_entrada()
            movimiento = self.cerebro_conejo(tablero)
            self.validarturno(movimiento)
            # Lógica para mover liebre primero
        else:
            print("El juego inicia con la Liebre.")
            # Lógica para mover liebre primero
        self.view.mostrarTurno(seleccion)

    
    def generar_posiciones_entrada(self):
        tablero = [0] * 15
        
        tablero[self.conejo_nodo] = 1
        tablero[self.perro1_nodo] = 2
        tablero[self.perro2_nodo] = 2
        tablero[self.perro3_nodo] = 2
        print(tablero)
        return tablero

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
                    print(f"Los nodos {self.nodo_seleccionado_conejo} y {nodo} estan conectados.")
                    self.nodo_seleccionado_conejo = nodo
                    self.turnoConejo(nodo)
                else:
                    print(f"Los nodos conejo {self.nodo_seleccionado_conejo} y {nodo} no estn conectados.")
            elif self.turno == "perros":
                print("somos perros y toca a los perros")
                self.logicaperros(nodo)

    def validarturno(self,nodo):
        if self.graph.estan_conectados(self.nodo_seleccionado_conejo, nodo):
            print(f"Los nodos {self.nodo_seleccionado_conejo} y {nodo} estan conectados.")
            self.nodo_seleccionado_conejo = nodo
            self.turnoConejo(nodo)
        else:
            print(f"Los nodos {self.nodo_seleccionado_conejo} y {nodo} no estan conectados.")
            print("[+] movimiento no validao")
            print("[+] vuelta llamada")
            tabla = self.generar_posiciones_entrada()
            movimiento = self.cerebro_conejo(tabla)
            self.validarturno(movimiento)


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
            tabla = self.generar_posiciones_entrada()
            movimiento = self.cerebro_conejo(tabla)
            self.validarturno(movimiento)
        if turno == 1:
            self.turno = "perros"
            self.view.mostrarTurno("perros")

    def mover_conejo(self, nuevo_nodo):
        self.view.mover(self.view.conejo_text, self.graph.nodos[nuevo_nodo])
        self.conejo_nodo = nuevo_nodo

    # red neuronal conejo
    def sigmoid(self,x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self,x):
        return x * (1 - x)
    
    def cerebro_conejo(self, entrada):
        print("llamada a la ia")
        #return 9
        posiciones_tablero = [
            (
                # posicion tablero
                [
                    0, 2, 0, 0, 0,
                    2, 0, 0, 0, 1, 
                    0, 2, 0, 0, 0, 
                ],
                # salida esperada
                [
                    0, 0, 0, 0, 0,
                    0, 0, 0, 1, 0, 
                    0, 0, 0, 0, 0, 
                ]
            ),
            (
                [
                    0, 0, 0, 0, 0,
                    2, 0, 2, 1, 0, 
                    0, 2, 0, 0, 0, 
                ],
                [
                    0, 0, 0, 1, 0,
                    0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 
                ]
            ),
            (
                [
                    0, 2, 0, 1, 0,
                    0, 0, 2, 0, 0, 
                    0, 2, 0, 0, 0, 
                ],
                [
                    0, 0, 1, 0, 0,
                    0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 
                ]
            ),
            (
                [
                    0, 2, 0, 1, 0,
                    0, 0, 2, 0, 0, 
                    0, 0, 2, 0, 0, 
                ],
                [
                    0, 0, 0, 1, 0,
                    0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 
                ]
            ),
            (
                [
                    0, 0, 2, 1, 0,
                    0, 0, 2, 0, 0, 
                    0, 0, 2, 0, 0, 
                ],
                [
                    0, 0, 0, 0, 0,
                    0, 0, 0, 1, 0, 
                    0, 0, 0, 0, 0, 
                ]
            ),
            (
                [
                    0, 0, 2, 0, 0,
                    0, 0, 2, 1, 0, 
                    0, 0, 0, 2, 0, 
                ],
                [
                    0, 0, 0, 1, 0,
                    0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 
                ]
            ),
            (
                [
                    0, 0, 2, 1, 0,
                    0, 0, 2, 2, 0, 
                    0, 0, 0, 0, 0, 
                ],
                [
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 1, 
                    0, 0, 0, 0, 0, 
                ]
            ),
        ]

        entradas = 15
        neuronas = entradas * 2
        salidas = entradas

        pesos = np.random.uniform(-1, 1, (neuronas, entradas))
        bias = np.random.uniform(-1, 1, (neuronas, 1))

        pesos_salidas = np.random.uniform(-1, 1, (salidas, neuronas))
        bias_salidas = np.random.uniform(-1, 1, (salidas, 1))


        # Parámetros de entrenamiento
        tasa_aprendizaje = 0.1
        epocas = 1000

        # Entrenamiento de la red neuronal
        for epoch in range(epocas):
            for tablero, mejor_movimiento in posiciones_tablero:
                tablero = np.array(tablero).reshape(-1, 1)
                mejor_movimiento = np.array(mejor_movimiento).reshape(-1, 1)
                entrada_capa_oculta = np.dot(pesos, tablero) + bias
                salida_capa_oculta = self.sigmoid(entrada_capa_oculta)

                entrada_capa_salida = np.dot(pesos_salidas, salida_capa_oculta) + bias_salidas
                salida_capa_salida = self.sigmoid(entrada_capa_salida)

                
                output_error = mejor_movimiento - salida_capa_salida
                output_delta = output_error * self.sigmoid_derivative(salida_capa_salida)

                hidden_error = np.dot(pesos_salidas.T, output_delta)
                hidden_delta = hidden_error * self.sigmoid_derivative(salida_capa_oculta)

                pesos_salidas += tasa_aprendizaje * np.dot(output_delta, salida_capa_oculta.T)
                bias_salidas += tasa_aprendizaje * output_delta

                pesos += tasa_aprendizaje * np.dot(hidden_delta, tablero.T)
                bias += tasa_aprendizaje * hidden_delta

        def predict(tablero):
            tablero = np.array(tablero).reshape(-1, 1)
            salida_capa_oculta = self.sigmoid(np.dot(pesos, tablero) + bias)
            salida_capa_salida = self.sigmoid(np.dot(pesos_salidas, salida_capa_oculta) + bias_salidas)
            return np.argmax(salida_capa_salida)

        # Ejemplo de predicción
        '''
        entrada = [
                0, 2, 0, 1, 0,
                0, 0, 2, 0, 0, 
                0, 2, 0, 0, 0, 
            ]
        '''

        hola = predict(entrada)
        print(f"La mejor jugada es en la posición: {hola +1}")
        return hola + 1 

            