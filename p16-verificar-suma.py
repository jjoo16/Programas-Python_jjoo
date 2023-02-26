# Verificar si la suma de dos numeros es igual a un tercero

import os

os.system('cls')

print('Verifica si la suma de 2 números es igual a un tercero\n')
print('Dame tres números separados por Enter: \n')

n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3:
    print('Son iguales')
else:
    print('Son diferentes')

print('Proceso Terminado Gracias')
