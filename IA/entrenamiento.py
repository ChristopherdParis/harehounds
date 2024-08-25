import numpy as np

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
    # movimientos iniciales conejo
    [
        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    ],
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    ],
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    ],
])

# One-hot encoding para las acciones posibles
izq = [1, 0, 0, 0, 0, 0, 0, 0, 0];  # Izquierda
der = [0, 1, 0, 0, 0, 0, 0, 0, 0];  # Derecha
up = [0, 0, 1, 0, 0, 0, 0, 0, 0];  # Arriba
down = [0, 0, 0, 1, 0, 0, 0, 0, 0];  # Abajo
front = [0, 0, 0, 0, 1, 0, 0, 0, 0];  # Adelante
back = [0, 0, 0, 0, 0, 1, 0, 0, 0];  # Atrás
daup = [0, 0, 0, 0, 0, 0, 1, 0, 0];  # Diagonal Adelante Arriba
dadown = [0, 0, 0, 0, 0, 0, 0, 1, 0];  # Diagonal Adelante Abajo
dbup = [0, 0, 0, 0, 0, 0, 0, 0, 1];  # Diagonal Atrás Arriba

# Clases correspondientes a los movimientos
clases = np.array([
    front,
    daup,
    dadown,
    daup,  # Ejemplo 1
    front, # Ejemplo 2
    dadown # Ejemplo 3
])

# Función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Función de activación Softmax para la capa de salida
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Substraer el máximo para evitar problemas numéricos
    return exp_x / exp_x.sum(axis=0)

# Predicción usando ReLU y softmax
def prediccion_softmax(pesos, x, b):
    z = np.dot(pesos, x) + b
    return softmax(z)

# Inicialización de pesos y bias
pesos = np.random.uniform(-1, 1, size=(9, 60))  # Matriz de pesos para 9 neuronas de salida (movimientos)
b = np.random.uniform(-1, 1, size=9)  # Bias para cada neurona de salida
tasa_de_aprendizaje = 0.01
epocas = 500

# Entrenamiento del perceptrón con Softmax
for epoca in range(epocas):
    error_total = 0
    for i in range(len(personas)):
        salida = prediccion_softmax(pesos, personas[i], b)
        prediccion = salida  # Ahora es un vector de probabilidades
        error = clases[i] - prediccion
        error_total += np.sum(error**2)
        # Actualización de pesos y bias
        pesos += tasa_de_aprendizaje * np.outer(error, personas[i])
        b += tasa_de_aprendizaje * error
    print(error_total, end=" ")

# Predicción con Softmax para un nuevo conjunto de posiciones
entrada_nueva = np.array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
])

# Predicción utilizando softmax para obtener probabilidades
hola = prediccion_softmax(pesos, entrada_nueva, b)

# Obtener la acción con mayor probabilidad
indice_prediccion = np.argmax(hola)

print("\nEl resultado es:", hola)
print("La acción recomendada es:", indice_prediccion)


'''

¡Exacto! Para problemas de clasificación multicategoría, como en este caso donde se necesita predecir el movimiento óptimo (izquierda, derecha, arriba, etc.), una capa de salida con la función de activación softmax es más adecuada. La función softmax convierte los valores de salida de las neuronas en probabilidades que suman a 1, facilitando la interpretación de la predicción del modelo.

1. Modificación del Modelo para Usar Softmax en la Capa de Salida
Vamos a modificar la red neuronal para que utilice softmax en la capa de salida. Esto ayudará a interpretar las salidas como probabilidades, donde la acción con la mayor probabilidad será la acción elegida.

2. Función Softmax
La función softmax se define como:


3. Código Modificado con Softmax
Aquí está el código modificado para incluir una capa de salida con softmax:

python
Copiar código
import numpy as np

# Datos de posiciones de movimientos posibles
personas = np.array([
    # movimientos iniciales conejo
    [
        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    ],
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    ],
    [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
    ],
])

# One-hot encoding para las acciones posibles
izq = [1, 0, 0, 0, 0, 0, 0, 0, 0];  # Izquierda
der = [0, 1, 0, 0, 0, 0, 0, 0, 0];  # Derecha
up = [0, 0, 1, 0, 0, 0, 0, 0, 0];  # Arriba
down = [0, 0, 0, 1, 0, 0, 0, 0, 0];  # Abajo
front = [0, 0, 0, 0, 1, 0, 0, 0, 0];  # Adelante
back = [0, 0, 0, 0, 0, 1, 0, 0, 0];  # Atrás
daup = [0, 0, 0, 0, 0, 0, 1, 0, 0];  # Diagonal Adelante Arriba
dadown = [0, 0, 0, 0, 0, 0, 0, 1, 0];  # Diagonal Adelante Abajo
dbup = [0, 0, 0, 0, 0, 0, 0, 0, 1];  # Diagonal Atrás Arriba

# Clases correspondientes a los movimientos
clases = np.array([
    daup,  # Ejemplo 1
    front, # Ejemplo 2
    dadown # Ejemplo 3
])

# Función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Función de activación Softmax para la capa de salida
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Substraer el máximo para evitar problemas numéricos
    return exp_x / exp_x.sum(axis=0)

# Predicción usando ReLU y softmax
def prediccion_softmax(pesos, x, b):
    z = np.dot(pesos, x) + b
    return softmax(z)

# Inicialización de pesos y bias
pesos = np.random.uniform(-1, 1, size=(9, 60))  # Matriz de pesos para 9 neuronas de salida (movimientos)
b = np.random.uniform(-1, 1, size=9)  # Bias para cada neurona de salida
tasa_de_aprendizaje = 0.01
epocas = 500

# Entrenamiento del perceptrón con Softmax
for epoca in range(epocas):
    error_total = 0
    for i in range(len(personas)):
        salida = prediccion_softmax(pesos, personas[i], b)
        prediccion = salida  # Ahora es un vector de probabilidades
        error = clases[i] - prediccion
        error_total += np.sum(error**2)
        # Actualización de pesos y bias
        pesos += tasa_de_aprendizaje * np.outer(error, personas[i])
        b += tasa_de_aprendizaje * error
    print(error_total, end=" ")

# Predicción con Softmax para un nuevo conjunto de posiciones
entrada_nueva = np.array([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
])

# Predicción utilizando softmax para obtener probabilidades
hola = prediccion_softmax(pesos, entrada_nueva, b)

# Obtener la acción con mayor probabilidad
indice_prediccion = np.argmax(hola)

print("\nEl resultado es:", hola)
print("La acción recomendada es:", indice_prediccion)
4. Interpretación del Resultado
Después de ejecutar el código modificado:

Resultado hola: Este será un vector de 9 elementos donde cada elemento es una probabilidad que indica cuán probable es cada movimiento posible (izquierda, derecha, arriba, abajo, adelante, atrás, etc.).

Interpretación con argmax:

np.argmax(hola) devuelve el índice de la clase con la mayor probabilidad, que corresponde al movimiento más probable.
El índice se puede mapear a la acción correspondiente:
0 -> Izquierda
1 -> Derecha
2 -> Arriba
3 -> Abajo
4 -> Adelante
5 -> Atrás
6 -> Diagonal Adelante Arriba
7 -> Diagonal Adelante Abajo
8 -> Diagonal Atrás Arriba
Ejemplo de Salida:

Si indice_prediccion es 1, la acción recomendada es "Derecha".
Si indice_prediccion es 6, la acción recomendada es "Diagonal Adelante Arriba".
5. Conclusión
Utilizando softmax en la capa de salida, puedes interpretar fácilmente el resultado de la red neuronal en términos de probabilidades de cada movimiento posible. La acción con la mayor probabilidad es la recomendada por el modelo. Esta modificación hace que tu red neuronal sea más robusta para la tarea de clasificación multicategoría en el juego que estás modelando.
'''