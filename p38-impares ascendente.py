#  imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n), 
# además deberá imprimirse la suma de esos números impares.  El proceso debe poder repetirse hasta que el 
# usuario lo decida. 

import os

while (True):
    os.system('cls')
    n = int(input('Hasta el núm?   '))

    c = 1
    while c<= n:
        print(f'{c} ')
        c += 2
    
    res = input('\n Deseas continuar (S/N)?')
    if res.upper()=='N':
        break

print('\n Gracias por participar')