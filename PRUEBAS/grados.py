import numpy as np

# Datos de entrada (conversión Celsius a Fahrenheit)
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Normalizar los datos de entrada
celsius_normalized = (celsius - np.min(celsius)) / (np.max(celsius) - np.min(celsius))

# Función de activación: combinación lineal
def activacion(pesos, x, b):
    z = pesos * x  # Aquí, x es un escalar y pesos es un peso escalar
    return z + b

# Inicializar peso y sesgo
pesos = np.random.uniform(-1, 1)  # Un peso (ya que la entrada es escalar)
b = np.random.uniform(-1, 1)      # Un término de sesgo
tasa_de_aprendizaje = 0.001       # Tasa de aprendizaje reducida
epocas = 10000                    # Número de épocas para entrenamiento

for epoca in range(epocas):
    error_total = 0
    for i in range(len(celsius_normalized)):
        prediccion = activacion(pesos, celsius_normalized[i], b)
        error = fahrenheit[i] - prediccion
        error_total += error**2
        pesos += tasa_de_aprendizaje * celsius_normalized[i] * error
        b += tasa_de_aprendizaje * error
    if epoca % 100 == 0:  # Imprimir cada 100 épocas
        print(f"Época {epoca}, Peso: {pesos}, Sesgo: {b}, Error total: {error_total}")

# Predicción final para 0 grados Celsius (normalizado)
zero_normalized = (8 - np.min(celsius)) / (np.max(celsius) - np.min(celsius))
hola = activacion(pesos, zero_normalized, b)
print("\nEl resultado es:", hola)
