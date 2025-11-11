while True:
    n, t = map(int, input().split())
    if n == 0 and t == 0:
        break

    tiempos = list(map(int, input().split()))
    tiempos.sort()

    tiempo_actual = 0
    resueltos = 0
    penalizacion = 0

    for x in tiempos:
        if tiempo_actual + x <= t:
            tiempo_actual += x
            resueltos += 1
            penalizacion += tiempo_actual
        else:
            break

    print(resueltos, penalizacion)
