import numpy as np


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


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

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
        salida_capa_oculta = sigmoid(entrada_capa_oculta)

        entrada_capa_salida = np.dot(pesos_salidas, salida_capa_oculta) + bias_salidas
        salida_capa_salida = sigmoid(entrada_capa_salida)

        
        output_error = mejor_movimiento - salida_capa_salida
        output_delta = output_error * sigmoid_derivative(salida_capa_salida)

        hidden_error = np.dot(pesos_salidas.T, output_delta)
        hidden_delta = hidden_error * sigmoid_derivative(salida_capa_oculta)

        pesos_salidas += tasa_aprendizaje * np.dot(output_delta, salida_capa_oculta.T)
        bias_salidas += tasa_aprendizaje * output_delta

        pesos += tasa_aprendizaje * np.dot(hidden_delta, tablero.T)
        bias += tasa_aprendizaje * hidden_delta

def predict(tablero):
    tablero = np.array(tablero).reshape(-1, 1)
    salida_capa_oculta = sigmoid(np.dot(pesos, tablero) + bias)
    salida_capa_salida = sigmoid(np.dot(pesos_salidas, salida_capa_oculta) + bias_salidas)
    return np.argmax(salida_capa_salida)

# Ejemplo de predicción
entrada = [
        0, 2, 0, 1, 0,
        0, 0, 2, 0, 0, 
        0, 2, 0, 0, 0, 
    ]
hola = predict(entrada)
print(f"La mejor jugada es en la posición: {hola +1}")
