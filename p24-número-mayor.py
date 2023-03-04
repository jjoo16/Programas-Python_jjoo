# Dados tres números enteros, verificar cual es el mayor

import os

os.system('cls')
print('Dados tres números enteros, verificar cual es el mayor')
print('Dame 3 números separados por Enter? \n')
n1, n2, n3 = int(input()), int(input()), int(input())
if n1 > n2 and n1 > n3:
    print(f' El número mayor es {n1}')
elif n2 > n1 and n2 >n3:
    print(f'El número mayor es {n2}')
elif n3 > n1 and n3 > n2:
    print(f'El número mayor es {n3}')
elif n1 == n2 and n1 > n3:
    print(f'El número mayor es {n1}')
elif n2 == n3 and n2 > n1:
    print(f'El número mayor es {n2}')
elif n1 == n3 and n1 > n2:
    print(f'El número mayor es {n1}')

print('Proceso terminado...')
