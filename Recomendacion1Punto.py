# Este método de recombinación de un punto está 
# ligeramente modificado para este problema en 
# particular, ya que tenemos el inconveniente de 
# que las ciudades en un mismo recorrido no se 
# pueden repetir, así que si hiciéramos el método 
# como es, estuviéramos violando esta regla del 
# problema.
# Para este problema en particular se seleccionó 
# el punto de recombinación para el cual cada 
# padre va a mantener los primeros genes hasta este
#  punto y después del punto se van a ordenar las 
#  ciudades que quedan como esta en el otro padre.

import numpy as np 

from random import randrange

def recombinacion_1_punto(numero_descendientes, poblacion, factor_probabilidad_recombinacion, tamano_poblacion):
    numero_descendientes_temporar = numero_descendientes;
    padres                        = np.zeros((tamano_poblacion, 4))
    fila                          = 0

    # Ordenar el arreglo de numero de descendientes 
    # da mayor a menor y guardarlo en un arreglo personal 
    while np.max(numero_descendientes_temporar) != 0:
        valor, posicion = numero_descendientes_temporar.max(), int(np.where(numero_descendientes_temporar == numero_descendientes_temporar.max())[0])
        for cantidad in range (valor):
            fila += 1
            padres[fila] = poblacion[poblacion]
        numero_descendientes_temporar[poblacion][0] = 0
    
    while len(padres) != 0:
        padre1 = padres[0]
        a = randrange(len(padres)-1) + 2
        padre2 = padres[a]

        padres[a] = np.zeros(len(padres[a]))
        padres[0] = np.zeros(len(padres[0]))
            pass
        pass



    # return poblacion
    pass