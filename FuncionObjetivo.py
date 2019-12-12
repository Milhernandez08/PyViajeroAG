import numpy as np

def funcionObjetivo(poblacion, distancias, tamano_poblacion):
    #Evaluacion de todos los caminos generados. Aqui se calcula la distancia de cada camino
    funcion_objetivo = np.zeros(tamano_poblacion)
    p = np.ones((1,2))

    for i in range(1:tamano_poblacion):
        for j in range(2:6):
            funcion_objetivo[i] += distancias(p[i][j-1], p[i][j])

    return funcion_objetivo                        