import numpy as np
import mysql.connector
from mysql.connector import Error
class Grafo:
    
    def registrarDatosEntrenamiento(self, ndHare, ndP1, ndP2, ndP3):
        print('[+] registrando datos de entrenamiento')
        N = 15
        
        # POSCIO CONEJO
        ps_conejo = ndHare

        # POSICIONES PERROS
        ps_perro_1 = ndP1
        ps_perro_2 = ndP2
        ps_perro_3 = ndP3

        # ENTRADA
        entrada_conejo = np.zeros(N)
        entrada_conejo[ps_conejo] = 1

        
        entrada_conejo[ps_perro_1] = 2

        
        entrada_conejo[ps_perro_2] = 3

        
        entrada_conejo[ps_perro_3] = 4

        #entrada_data = np.concatenate([entrada_conejo, entrada_perro_1, entrada_perro_2, entrada_perro_3])

        print("Vector de entrada para la red neuronal:")
        print(entrada_conejo)
        hola = self.ia([ 0, 2, 0, 0, 0, 3, 0, 0, 0, 1, 0, 4, 0, 0, 0])
        print("salida de la funcion ia desde grafdo: ",hola)
        return hola
        #self.registroDatabase(resultado,bestnodo)
        
    def registroDatabase(self,datos,bestnodo):
        try:
            # Conectar a la base de datos MySQL
            connection = mysql.connector.connect(
                host='localhost',  # Cambia a la dirección de tu servidor MySQL si es necesario
                database='hund',  # Reemplaza con el nombre de tu base de datos
                user='root',  # Reemplaza con tu nombre de usuario de MySQL
                password='admin'  # Reemplaza con tu contraseña de MySQL
            )

            if connection.is_connected():
                print("[+] Conexión exitosa a la base de datos MySQL")

                # Crear un cursor para ejecutar comandos SQL
                cursor = connection.cursor()

                # Crear la tabla si no existe
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS entrenamiento (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        resultado TEXT,
                        bestmove INT
                    )
                ''')

                # Insertar los datos en la tabla
                cursor.execute('INSERT INTO entrenamiento (resultado,bestmove) VALUES (%s,%s)', (datos,bestnodo))

                # Confirmar los cambios
                connection.commit()
                print("[+] Datos guardados exitosamente en la base de datos.")

        except Error as e:
            print(f"Error al conectar con MySQL: {e}")

        finally:
            # Cerrar la conexión
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("[+] Conexión a MySQL cerrada.")

    def ia(self,entrada):
        print("entrada ia ", entrada)
        
        # Datos de entrenamiento
        personas = np.array([
            [ 
                0, 2, 0, 0, 0,
                3, 0, 0, 0, 1,
                0, 4, 0, 0, 0
            ],
            [ 
                0, 2, 0, 1, 0,
                3, 0, 0, 0, 0,
                0, 4, 0, 0, 0
            ],
            [ 
                0, 2, 0, 0, 0,
                3, 0, 0, 1, 0,
                0, 4, 0, 0, 0
            ],
            [ 
                0, 0, 0, 0, 0,
                3, 0, 2, 1, 0,
                0, 4, 0, 0, 0
            ],
        ])

        # Clases objetivo
        clases = np.array([9,3, 8, 4])

        # Función de activación ReLU
        def relu(x):
            return np.maximum(0, x)

        # Función de activación modificada usando ReLU
        def activacion(pesos, x, b):
            z = np.dot(pesos, x) + b
            return relu(z)

        # Inicialización de pesos y bias
        pesos = np.random.uniform(-1, 1, size=15)
        b = np.random.uniform(-1, 1)
        tasa_de_aprendizaje = 0.01
        epocas = 200

        # Bucle de entrenamiento
        for epoca in range(epocas):
            error_total = 0
            for i in range(len(personas)):
                # Predicción usando ReLU
                prediccion = activacion(pesos, personas[i], b)
                
                # Cálculo del error
                error = clases[i] - prediccion
                error_total += error**2
                
                # Actualización de pesos y bias usando operaciones vectorizadas
                pesos += tasa_de_aprendizaje * personas[i] * error
                b += tasa_de_aprendizaje * error

            print(error_total, end=" ")

        # Prueba del modelo
        #entrada = personas[0]
        resultado = activacion(pesos, entrada, b)
        print("\nEl resultado es de la ia:", round(resultado))
        return round(resultado)
