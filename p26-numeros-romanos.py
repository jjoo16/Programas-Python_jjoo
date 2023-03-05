# Pide un número entre 1 y 10 y muestre su equivalente en número romano

import os

os.system('cls')
print('Pide un número entre 1 y 10 y muestre su equivalente en número romano\n')
print('Dame un número entre el 1 y 10, daré su equivalente en número Romano?')

n = int(input())

if n == 1:
    print(f'El numero {n} su equivalente en Romano es I')
elif n == 2:
    print(f'El numero {n} su equivalente en Romano es II')
elif n == 3:
    print(f'El numero {n} su equivalente en Romano es III')
elif n == 4:
    print(f'El numero {n} su equivalente en Romano es IV')
elif n == 5:
    print(f'El numero {n} su equivalente en Romano es V')
elif n == 6:
    print(f'El numero {n} su equivalente en Romano es VI')
elif n == 7:
    print(f'El numero {n} su equivalente en Romano es VII')
elif n == 8:
    print(f'El numero {n} su equivalente en Romano es VIII')
elif n == 9:
    print(f'El numero {n} su equivalente en Romano es IX')
elif n == 10:
    print(f'El numero {n} su equivalente en Romano es X')
else:
    print('Es un error')
print('Gracias por participar')
