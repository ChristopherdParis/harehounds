import numpy as np
# CAPA DE ENTRADA

N = 15 
# POSCIO CONEJO
ps_conejo = 10

# POSICIONES PERROS
ps_perro_1 = 2
ps_perro_2 = 6
ps_perro_3 = 12

# ENTRADA
entrada_conejo = np.zeros(N)
entrada_conejo[ps_conejo] = 1

# Vectores de entrada
entrada_perro_1 = np.zeros(N)
entrada_perro_1[ps_perro_1] = 1

entrada_perro_2 = np.zeros(N)
entrada_perro_2[ps_perro_2] = 1

entrada_perro_3 = np.zeros(N)
entrada_perro_3[ps_perro_3] = 1

entrada_data = np.concatenate([entrada_conejo, entrada_perro_1, entrada_perro_2, entrada_perro_3])

print("Vector de entrada para la red neuronal:")
print(entrada_data)

print("Entrada conejo:")
print(entrada_conejo)
print("Entrada perro1:")
print(entrada_perro_1)
print("Entrada perro2:")
print(entrada_perro_2)
print("Entrada perro3:")
print(entrada_perro_3)

# Guardar el vector de entrada en un archivo de texto
#np.savetxt('entrada_data.txt', entrada_data, delimiter=',')