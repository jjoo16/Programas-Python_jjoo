# imprimir los números pares desde 100 hasta el número que el usuario decida (n), además deberá 
# imprimirse la suma de esos números pares.  El proceso debe poder repetirse hasta que el usuario lo decida.
 

import os
print('mprimir los números pares desde 100 hasta el número que el usuario decida')

while (True):
    os.system('cls')
    print('Introduce un número mayor que 100')
    n = int(input('Números pares, hasta el núm?   '))

    c = 1
    while c<= n and c == 0:
        print(f'{c} ')
        c -= 2
    
    res = input('\n Deseas continuar (S/N)?')
    if res.upper()=='N':
        break

print('\n Gracias por participar')