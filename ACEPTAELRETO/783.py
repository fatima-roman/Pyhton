tiempo = []
solucion ={}

nProblemas, tiempoEstimado = (int, (input().split()))
nProblemas = int(nProblemas)
tiempoEstimado = int(tiempoEstimado)

while nProblemas != 0 and tiempoEstimado != 0:
    for i in range(nProblemas):
        tiempo = list(map(int, input().split()))
    
    tiempo.sort()
    for i in range(len(tiempo)):
        if len(tiempo) >= 2:
            if tiempo[i] + tiempo[1] <= tiempoEstimado:
                solucion[nProblemas] = tiempoEstimado
        else: 
            tiempo[i] <= tiempoEstimado
            solucion[nProblemas] = tiempoEstimado
    nProblemas = int(input())
    tiempoEstimado = int(input())

print(solucion.items())