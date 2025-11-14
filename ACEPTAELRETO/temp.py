solucion = []
temp = []
cont = 0

nAbreviatras = int(input())

for i in range(nAbreviatras):
    abreviaturas=input()#.split() #b.,s.,d.
    #print(abreviaturas)

    for k in (abreviaturas):
        cont = cont + 1
        if k != '.' and k != ' ':
            solucion.append(2*k + '. ')
    #print(solucion)
    temp.append(cont-len(abreviaturas))

for i in range(len(solucion)):
    cont = 0
    cont = cont + 1
    print(solucion[i], end='')
    if temp[cont-1] == i+1:
        print()

#print((solucion))
