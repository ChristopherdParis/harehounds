import numpy as np

# Función para representar el estado del juego como un vector de entrada detallado
def get_detailed_game_state_vector(liebre_pos, sabuesos_pos):
    """
    Convierte el estado del juego a un vector de tamaño 15 que indica el tipo de pieza en cada nodo.
    
    Args:
    liebre_pos (int): La posición de la liebre (1-15).
    sabuesos_pos (list): Una lista de tres enteros que representan las posiciones de los sabuesos (1-15).
    
    Returns:
    numpy.ndarray: Un vector de tamaño 15 representando el estado detallado del juego.
    """
    # Inicializamos un vector de tamaño 15 con ceros (0 representa un nodo vacío)
    state_vector = np.zeros(15)
    
    # Marcamos la posición de la liebre con un 1
    state_vector[liebre_pos - 1] = 1  # Restamos 1 para ajustar el índice (0 basado en Python)
    
    # Marcamos las posiciones de los sabuesos con diferentes valores (2, 3, 4)
    for i, pos in enumerate(sabuesos_pos):
        state_vector[pos - 1] = i + 2  # Sabuesos marcados como 2, 3, 4 respectivamente
    
    return state_vector

# Ejemplo del estado actual del juego basado en la imagen
liebre_pos = 9
sabuesos_pos = [2, 6, 12]

# Obtener el vector de estado del juego detallado
detailed_game_state_vector = get_detailed_game_state_vector(liebre_pos, sabuesos_pos)
entrada_data = detailed_game_state_vector.astype(int)

# Convertir el array a una cadena con comas
resultado = ', '.join(map(str, entrada_data))

print(f"[{resultado}]")
print("Vector de estado del juego detallado:", detailed_game_state_vector)
