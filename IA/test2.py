import numpy as np
'''
# Datos de posiciones de movimientos posibles
personas = np.array([
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    ],
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    ],
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    ],
])

# Nodos de destino correspondientes a las posiciones anteriores (Ejemplo)
clases = np.array([
    14,  # Nodo 14 para el primer conjunto de entradas
    4,   # Nodo 4 para el segundo conjunto
    9,   # Nodo 9 para el tercer conjunto
])

# Función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Derivada de la función ReLU
def relu_derivada(x):
    return np.where(x > 0, 1, 0)

# Función de activación Softmax para la capa de salida
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Substraer el máximo para evitar problemas numéricos
    return exp_x / exp_x.sum(axis=0)

# Predicción usando ReLU para capa oculta y softmax para capa de salida
def prediccion(pesos_entrada, pesos_salida, x, b_entrada, b_salida):
    capa_oculta = relu(np.dot(pesos_entrada, x) + b_entrada)
    salida = softmax(np.dot(pesos_salida, capa_oculta) + b_salida)
    return capa_oculta, salida

# Inicialización de pesos y bias
pesos_entrada = np.random.uniform(-1, 1, size=(30, 60))  # Pesos para capa oculta (30 neuronas, 60 entradas)
b_entrada = np.random.uniform(-1, 1, size=30)  # Bias para capa oculta (30 neuronas)

pesos_salida = np.random.uniform(-1, 1, size=(15, 30))  # Pesos para capa de salida (15 neuronas de salida, 30 entradas de capa oculta)
b_salida = np.random.uniform(-1, 1, size=15)  # Bias para capa de salida (15 neuronas)

tasa_de_aprendizaje = 0.01
epocas = 500

# Entrenamiento del perceptrón multicapa con ReLU y Softmax
for epoca in range(epocas):
    error_total = 0
    for i in range(len(personas)):
        # Forward pass
        capa_oculta, salida = prediccion(pesos_entrada, pesos_salida, personas[i], b_entrada, b_salida)
        
        # Calcular el error de la salida
        error_salida = np.zeros_like(salida)
        error_salida[clases[i] - 1] = 1 - salida[clases[i] - 1]  # Restamos 1 para ajustar al índice del array

        # Calcular el error total (suma de cuadrados)
        error_total += np.sum((error_salida) ** 2)

        # Backward pass para actualizar los pesos de la capa de salida
        delta_salida = error_salida
        pesos_salida += tasa_de_aprendizaje * np.outer(delta_salida, capa_oculta)
        b_salida += tasa_de_aprendizaje * delta_salida

        # Backward pass para actualizar los pesos de la capa oculta
        delta_oculta = relu_derivada(capa_oculta) * np.dot(pesos_salida.T, delta_salida)
        pesos_entrada += tasa_de_aprendizaje * np.outer(delta_oculta, personas[i])
        b_entrada += tasa_de_aprendizaje * delta_oculta

    if (epoca + 1) % 100 == 0 or epoca == epocas - 1:
        print(f"Época {epoca+1}/{epocas}, Error Total: {error_total}")

# Predicción con ReLU y Softmax para un nuevo conjunto de posiciones
entrada_nueva = np.array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
])

# Realizar la predicción
_, probabilidades = prediccion(pesos_entrada, pesos_salida, entrada_nueva, b_entrada, b_salida)

# Obtener el nodo con mayor probabilidad (el nodo al que moverse)
nodo_prediccion = np.argmax(probabilidades) + 1  # Sumar 1 para que el rango sea de 1 a 15

print("\nProbabilidades para cada nodo:", probabilidades)
print("El nodo recomendado para moverse es:", nodo_prediccion)

# Mostrar la probabilidad asociada al nodo recomendado
print(f"La probabilidad de moverse al nodo {nodo_prediccion} es: {probabilidades[nodo_prediccion - 1]:.4f}")
'''

import numpy as np

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
        0, 0, 0, 0, 0,
        3, 0, 2, 1, 0,
        0, 4, 0, 0, 0
    ],
])

# Clases objetivo
clases = np.array([ 4, 3, 4])

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
entrada = personas[0]
resultado = activacion(pesos, entrada, b)
print("\nEl resultado es:", round(resultado))
