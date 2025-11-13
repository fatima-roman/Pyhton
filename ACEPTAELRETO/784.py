solucion = []
temp = []

nAbreviatras = int(input())

for i in range(nAbreviatras):
    abreviaturas=input()#.split() #b.,s.,d.
    #print(abreviaturas)

    for k in (abreviaturas):
        if k != '.' and k != ' ':
            solucion.append(2*k + '. ')
    #print(solucion)
    temp.append(len(solucion)-len(abreviaturas))

for i in range(len(solucion)):
    print(solucion[i], end='')

print((solucion))
