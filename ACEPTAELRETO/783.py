tiempo = []
solucion ={}

nProblemas, tiempoEstimado = map(int, (input().split()))


while nProblemas != 0 and tiempoEstimado != 0:
    print(nProblemas, tiempoEstimado)
    for i in range(nProblemas):
        tiempo = list(map(int, input().split()))
    tiempo.sort()

    for i in tiempo:
        tiempoAcumulado = 0
        problemasResueltos = 0
        penalizacion = 0

        if tiempoAcumulado + i <= tiempoEstimado:
            tiempoAcumulado += i
            problemasResueltos += 1
            penalizacion += tiempoAcumulado
        else:
            break
    solucion[nProblemas] = penalizacion
    print(solucion)
    nProblemas, tiempoEstimado = map(int, (input().split()))

print(solucion.items())