import numpy as np

# Datos de entrada (60 características)
input_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

# Inicializamos pesos para cada neurona en la capa oculta
weights_neuron_1 = np.random.rand(60)  # Pesos para la primera neurona
weights_neuron_2 = np.random.rand(60)  # Pesos para la segunda neurona

# Inicializamos sesgos para cada neurona en la capa oculta
bias_neuron_1 = np.random.rand(1)  # Sesgo para la primera neurona
bias_neuron_2 = np.random.rand(1)  # Sesgo para la segunda neurona

# Suma ponderada para la primera neurona en la capa oculta
z1 = np.dot(input_data, weights_neuron_1) + bias_neuron_1

# Suma ponderada para la segunda neurona en la capa oculta
z2 = np.dot(input_data, weights_neuron_2) + bias_neuron_2

# Función ReLU aplicada
output_neuron_1 = np.maximum(0, z1)
output_neuron_2 = np.maximum(0, z2)

# Ahora la capa de salida
# Inicializamos pesos y sesgo para cada neurona de la capa de salida (4 neuronas)
weights_output_neurons = np.random.rand(4, 2)  # 4 neuronas, cada una con 2 pesos
bias_output_neurons = np.random.rand(4)  # Un sesgo por cada neurona en la capa de salida

# Aseguramos que las salidas de las neuronas en la capa oculta estén en forma correcta
outputs_hidden_layer = np.array([output_neuron_1, output_neuron_2]).flatten()

# Suma ponderada en cada neurona de la capa de salida
z_output = np.dot(weights_output_neurons, outputs_hidden_layer) + bias_output_neurons

# Aplicamos la función softmax para obtener probabilidades de cada acción
output_final = np.exp(z_output) / np.sum(np.exp(z_output))

print("Probabilidades de acciones:", output_final)

# Seleccionar la acción con la mayor probabilidad
acciones = ["arriba", "abajo", "izquierda", "derecha"]
accion_seleccionada = acciones[np.argmax(output_final)]

print("Acción seleccionada:", accion_seleccionada)
