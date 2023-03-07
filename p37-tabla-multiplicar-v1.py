# # Imprime las tablas de 1 a n, hasta m

import os

while (True):
    os.system('cls')
    n = int(input('Las tablas desde la 1 hasta la del número? '))
    m = int(input('Desde la 1 hasta m'))

t = 1
while t <= n:
    print(f'Tabla del {t}')

    c = 1
    while c<= m:
        print(f'{t} x {c} = {c*t}')
        c += 1
    
    t += 1
    res = input('\n Deseas continuar (S/N)?')
    if res.upper()=='N':
        break

print('\n Gracias por participar')