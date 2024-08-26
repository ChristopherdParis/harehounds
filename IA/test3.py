'''
import random
import math

# Función de activación sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Inicialización de la red neuronal con pesos y sesgos
def initialize_network():
    hidden_weights = [[random.uniform(-1, 1) for _ in range(9)] for _ in range(18)]
    output_weights = [[random.uniform(-1, 1) for _ in range(18)] for _ in range(9)]
    hidden_bias = [random.uniform(-1, 1) for _ in range(18)]
    output_bias = [random.uniform(-1, 1) for _ in range(9)]
    return hidden_weights, output_weights, hidden_bias, output_bias

# Adelante Propagación y Retropropagación en una sola función para entrenamiento
def train_network(training_data, hidden_weights, output_weights, hidden_bias, output_bias, learning_rate, epochs):
    for epoch in range(epochs):
        for board, expected_output in training_data:
            # Adelante Propagación
            hidden_layer_output = [sigmoid(sum(board[j] * hidden_weights[i][j] for j in range(9)) + hidden_bias[i]) for i in range(18)]
            output_layer_output = [sigmoid(sum(hidden_layer_output[j] * output_weights[i][j] for j in range(18)) + output_bias[i]) for i in range(9)]

            # Calcular errores de salida y ocultos
            output_errors = [expected_output[i] - output_layer_output[i] for i in range(9)]
            hidden_errors = [sum(output_errors[j] * output_weights[j][i] for j in range(9)) * sigmoid_derivative(hidden_layer_output[i]) for i in range(18)]

            # Actualizar pesos y sesgos
            for i in range(9):
                for j in range(18):
                    output_weights[i][j] += learning_rate * output_errors[i] * sigmoid_derivative(output_layer_output[i]) * hidden_layer_output[j]
                output_bias[i] += learning_rate * output_errors[i] * sigmoid_derivative(output_layer_output[i])

            for i in range(18):
                for j in range(9):
                    hidden_weights[i][j] += learning_rate * hidden_errors[i] * board[j]
                hidden_bias[i] += learning_rate * hidden_errors[i]

# Predicción del mejor movimiento basado en el tablero actual
def predict(board, hidden_weights, output_weights, hidden_bias, output_bias):
    hidden_layer_output = [sigmoid(sum(board[j] * hidden_weights[i][j] for j in range(9)) + hidden_bias[i]) for i in range(18)]
    output_layer_output = [sigmoid(sum(hidden_layer_output[j] * output_weights[i][j] for j in range(18)) + output_bias[i]) for i in range(9)]
    return output_layer_output.index(max(output_layer_output))

# Datos de entrenamiento simplificados
training_data = [
    ([1, 0, 0, 0, 2, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]),  # Aquí se asume que el movimiento esperado es en la posición 1
    ([2, 1, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]),  # Ejemplo adicional
    # Añade más ejemplos de entrenamiento
]

# Inicialización y entrenamiento
hidden_weights, output_weights, hidden_bias, output_bias = initialize_network()
train_network(training_data, hidden_weights, output_weights, hidden_bias, output_bias, learning_rate=0.1, epochs=1000)

# Ejemplo de predicción

board_example = [
    2, 1, 0, 0, 2, 0, 0, 0, 0]
best_move = predict(board_example, hidden_weights, output_weights, hidden_bias, output_bias)
print(f"La mejor jugada es en la posición: {best_move}")

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivada de la función sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Inicialización de la red neuronal
def initialize_network():
    # Número de neuronas en cada capa
    input_neurons = 9
    hidden_neurons = 18
    output_neurons = 9
    
    # Pesos
    hidden_weights = [[random.uniform(-1, 1) for _ in range(input_neurons)] for _ in range(hidden_neurons)]
    output_weights = [[random.uniform(-1, 1) for _ in range(hidden_neurons)] for _ in range(output_neurons)]
    
    # Sesgos
    hidden_bias = [random.uniform(-1, 1) for _ in range(hidden_neurons)]
    output_bias = [random.uniform(-1, 1) for _ in range(output_neurons)]
    
    return hidden_weights, output_weights, hidden_bias, output_bias

# Adelante Propagación
def forward_propagation(board, hidden_weights, output_weights, hidden_bias, output_bias):
    # Calcular activación de capa oculta
    hidden_layer_activation = [0] * len(hidden_weights)
    for i in range(len(hidden_weights)):
        activation = hidden_bias[i]
        for j in range(len(board)):
            activation += board[j] * hidden_weights[i][j]
        hidden_layer_activation[i] = sigmoid(activation)
    
    # Calcular activación de capa de salida
    output_layer_activation = [0] * len(output_weights)
    for i in range(len(output_weights)):
        activation = output_bias[i]
        for j in range(len(hidden_layer_activation)):
            activation += hidden_layer_activation[j] * output_weights[i][j]
        output_layer_activation[i] = sigmoid(activation)
    
    return hidden_layer_activation, output_layer_activation

# Retropropagación
def backpropagation(board, hidden_layer_activation, output_layer_activation, expected_output, hidden_weights, output_weights, hidden_bias, output_bias, learning_rate):
    # Cálculo del error de la capa de salida
    output_errors = [0] * len(output_layer_activation)
    for i in range(len(output_layer_activation)):
        output_errors[i] = expected_output[i] - output_layer_activation[i]
    
    # Ajustar pesos y sesgos para la capa de salida
    output_deltas = [0] * len(output_errors)
    for i in range(len(output_errors)):
        output_deltas[i] = output_errors[i] * sigmoid_derivative(output_layer_activation[i])
    
    for i in range(len(output_weights)):
        for j in range(len(output_weights[i])):
            output_weights[i][j] += learning_rate * output_deltas[i] * hidden_layer_activation[j]
        output_bias[i] += learning_rate * output_deltas[i]
    
    # Cálculo del error de la capa oculta
    hidden_errors = [0] * len(hidden_layer_activation)
    for i in range(len(hidden_weights)):
        error = 0
        for j in range(len(output_weights)):
            error += output_deltas[j] * output_weights[j][i]
        hidden_errors[i] = error
    
    # Ajustar pesos y sesgos para la capa oculta
    hidden_deltas = [0] * len(hidden_errors)
    for i in range(len(hidden_errors)):
        hidden_deltas[i] = hidden_errors[i] * sigmoid_derivative(hidden_layer_activation[i])
    
    for i in range(len(hidden_weights)):
        for j in range(len(hidden_weights[i])):
            hidden_weights[i][j] += learning_rate * hidden_deltas[i] * board[j]
        hidden_bias[i] += learning_rate * hidden_deltas[i]

# Función de entrenamiento
def train_network(training_data, hidden_weights, output_weights, hidden_bias, output_bias, learning_rate, epochs):
    for epoch in range(epochs):
        for board, expected_output in training_data:
            # Adelante Propagación
            hidden_layer_activation, output_layer_activation = forward_propagation(board, hidden_weights, output_weights, hidden_bias, output_bias)
            
            # Retropropagación
            backpropagation(board, hidden_layer_activation, output_layer_activation, expected_output, hidden_weights, output_weights, hidden_bias, output_bias, learning_rate)

# Predecir el mejor movimiento
def predict(board, hidden_weights, output_weights, hidden_bias, output_bias):
    _, output_layer_activation = forward_propagation(board, hidden_weights, output_weights, hidden_bias, output_bias)
    # Seleccionar el índice de la neurona de salida con el valor más alto
    best_move = output_layer_activation.index(max(output_layer_activation))
    return best_move

# Datos de entrenamiento (ejemplo)
# Necesitarías proporcionar tus propios datos de entrenamiento aquí
# Cada entrada es un par (tablero, movimiento esperado)
training_data = [
    ([1, 0, 0, 0, 2, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]),  # Aquí se asume que el movimiento esperado es en la posición 1
    ([2, 1, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]),  # Ejemplo adicional
    # Añade más ejemplos de entrenamiento
]

# Inicialización de la red
hidden_weights, output_weights, hidden_bias, output_bias = initialize_network()

# Entrenar la red neuronal
train_network(training_data, hidden_weights, output_weights, hidden_bias, output_bias, learning_rate=0.1, epochs=1000)

# Ejemplo de predicción
board_example = [
    2, 1, 0, 0, 2, 0, 0, 0, 0]  # Estado actual del tablero
best_move = predict(board_example, hidden_weights, output_weights, hidden_bias, output_bias)
print(f"La mejor jugada es en la posición: {best_move}")
'''
import numpy as np

# Función de activación sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Inicialización de la red neuronal con numpy
def initialize_network():
    hidden_weights = np.random.uniform(-1, 1, (18, 9))
    output_weights = np.random.uniform(-1, 1, (9, 18))
    hidden_bias = np.random.uniform(-1, 1, (18, 1))
    output_bias = np.random.uniform(-1, 1, (9, 1))
    return hidden_weights, output_weights, hidden_bias, output_bias

# Adelante Propagación y Retropropagación combinadas para entrenamiento
def train_network(training_data, hidden_weights, output_weights, hidden_bias, output_bias, learning_rate, epochs):
    for epoch in range(epochs):
        for board, expected_output in training_data:
            board = np.array(board).reshape(-1, 1)
            expected_output = np.array(expected_output).reshape(-1, 1)

            # Adelante Propagación
            hidden_layer_input = np.dot(hidden_weights, board) + hidden_bias
            hidden_layer_output = sigmoid(hidden_layer_input)

            output_layer_input = np.dot(output_weights, hidden_layer_output) + output_bias
            output_layer_output = sigmoid(output_layer_input)

            # Calcular errores de salida y ocultos
            output_errors = expected_output - output_layer_output
            hidden_errors = np.dot(output_weights.T, output_errors) * sigmoid_derivative(hidden_layer_output)

            # Actualizar pesos y sesgos
            output_weights += learning_rate * np.dot(output_errors * sigmoid_derivative(output_layer_output), hidden_layer_output.T)
            output_bias += learning_rate * output_errors * sigmoid_derivative(output_layer_output)

            hidden_weights += learning_rate * np.dot(hidden_errors * sigmoid_derivative(hidden_layer_output), board.T)
            hidden_bias += learning_rate * hidden_errors * sigmoid_derivative(hidden_layer_output)

# Predicción del mejor movimiento basado en el tablero actual
def predict(board, hidden_weights, output_weights, hidden_bias, output_bias):
    board = np.array(board).reshape(-1, 1)

    hidden_layer_output = sigmoid(np.dot(hidden_weights, board) + hidden_bias)
    output_layer_output = sigmoid(np.dot(output_weights, hidden_layer_output) + output_bias)

    return np.argmax(output_layer_output)

# Datos de entrenamiento simplificados
training_data = [
    ([1, 0, 0, 0, 2, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0]),  # Aquí se asume que el movimiento esperado es en la posición 1
    ([2, 1, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]),  # Ejemplo adicional
    # Añade más ejemplos de entrenamiento
]
# Inicialización y entrenamiento
hidden_weights, output_weights, hidden_bias, output_bias = initialize_network()
train_network(training_data, hidden_weights, output_weights, hidden_bias, output_bias, learning_rate=0.1, epochs=1000)

# Ejemplo de predicción
board_example = [
    2, 1, 0, 0, 2, 0, 0, 0, 0]
best_move = predict(board_example, hidden_weights, output_weights, hidden_bias, output_bias)
print(f"La mejor jugada es en la posición: {best_move}")
