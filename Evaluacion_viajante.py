import numpy as np
import random

char = np.array(['A','B','C','D','E'], dtype=str)
distancias = np.zeros(10)
camino = np.array([3,1,4,2])
caminos = np.ones((1,4))
for i in range(10):
    #camino, distancia = main
    distancias[i] = random.randrange(10)    
    caminos[i:] = camino

minimo = np.amin(distancias)
pos = np.where(distancias == np.amin(distancias))
pos = int(pos[0])
b = int(caminos[0][1])
c = int(caminos[0][2])
d = int(caminos[0][3])
#print(a,b,c,d)
print(char[0],char[pos],char[b],char[c],char[d],char[0])