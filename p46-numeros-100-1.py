# Imprimir los números del 100 a 1

n = int(input('Desde donde quieres descender? '))
s = int(input('Paso? '))

for y in range(n, 0,-s):
    print(y, end=' ')
