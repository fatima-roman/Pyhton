solucion = []

nAbreviatras = int(input())

for i in range(nAbreviatras):
    abreviaturas=input()#.split() #b.,s.,d.
    print(abreviaturas)

    for j in ((abreviaturas)):
        if j != '.' and j != ' ':
            solucion.append(2*j + '. ')


for k in range(len(solucion)):
    if k == len(solucion)-1:
        print(solucion[k])
    else:
        print(solucion[k], end='')