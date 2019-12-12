import random
def mutacion(poblacion, factor_probabilidad_mutacion, tamano_poblacion):
    
    rand  = random.random()
    if rand <= factor_probabilidad_mutacion:
        descendiente = random.randint(1, tamano_poblacion)
        gen1 = random.randint(1, 4)
        gen2 = gen1
        while gen2 == gen1:
            gen2 = random.randint(1, 4)
        
        temp = poblacion[descendiente][gen1
        poblacion[descendiente][gen1] = poblacion[descendiente][gen2]
        poblacion[descendiente][gen2] = temp
    
    return poblacion
    