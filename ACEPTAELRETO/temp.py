solucion = []

nAbreviatras = int(input())

for i in range(nAbreviatras):
    abreviaturas=input()#.split() #b.,s.,d.
    #print(abreviaturas)

    for k in (abreviaturas):
        if k != '.' and k != ' ':
            print(2*k + '. ', end='')
    print()