# Imprimir los números de 1 a 100

n = int(input( 'Hasta donde quieres llegar? '))
s = int(input('Paso ?'))

for x in range(1, n + 1, s):
    print(x, end=' ')

