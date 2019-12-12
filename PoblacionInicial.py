import numpy as np


from random import randrange

# Creación de la población inicial solo se creara el
# camino entre las ciudades BCDE, por que el inicio
# y el final es la misma cuidad A 

# Las ciudades se representaran por números
# A = 1, B = 2, C = 3, D = 4, E = 5

def poblacionInicial(tamano_poblacion):                 

    poblacion = np.zeros((tamano_poblacion, 4))         # Creación del arreglo población inicializando todos sus elementos en 0 

    for fila in range(tamano_poblacion):                # Recorro las filas (individuos de la población)
        for columna in range(4):                        # Recorro las columnas (ciudades)
            parar = False
            while parar != True:                        # Repetir hasta que se encuentre una ciudad que no esté en el camino que se está creando
                a = randrange(4) + 2                    # Genero las ciudades aleatoriamente (numero aleatorio entre 2 y 5)
                if not a in poblacion[fila]:            # Verificar si la cuidad no está en el camino (No se pueden repetir las ciudades en un mismo camino)
                    poblacion[fila][columna] = a        # Si no está en el camino introducir la cuidad
                    parar = True                        # Para salir del ciclo while y generar la otra cuidad  

    return poblacion