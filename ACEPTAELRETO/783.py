solucion = []

while True:
    nProblemas, tiempoEstimado = map(int, input().split())
    
    if nProblemas == 0 and tiempoEstimado == 0:
        break
    
    tiempos = list(map(int, input().split()))
    tiempos.sort()  
    
    tiempoAcumulado = 0
    problemasResueltos = 0
    penalizacion = 0
    
    for tiempo in tiempos:
        if tiempoAcumulado + tiempo <= tiempoEstimado:
            tiempoAcumulado += tiempo
            problemasResueltos += 1
            penalizacion += tiempoAcumulado
        else:
            break
    
    solucion.append((problemasResueltos, penalizacion))

for result in solucion:
    print(result[0], result[1])