# Imprimir la suma de los números pares o impares, según el ususario
import os

os.system('cls')
print('[P]ares de 1 a n y suma\n[I]mpares de 1 a n y su suma\n')
op = input('Dame tu opción? ').upper()
n = int(input('Hasta donde? '))
s = 0

if op == 'P':
    print(f'\nNúmeros pares de 1 a {n} y su suma')
    for i in range(2,n+1,2):
        print(i, end=' ')
        s += i
    print(f'\nSuma de pares', s)

elif op == 'I':
     print(f'\nNúmeros impares de 1 a {n} y su suma')
     for i in range(1,n+1,2):
        print(i, end=' ')
        s += i
     print(f'\nSuma de impares', s)

              
print('\n\n Proceso terminado')

