# Obtener los días de la semana dado un número entre 1 y 7.

import os

os.system('cls')
print('Obtener los días de la semana dado un número entre 1 y 7')
print('Dame un número entre el 1 y 7? \n')

n = int(input())

if n == 1:
    print(f'El día {n} de la semana es Lunes')
elif n == 2:
    print(f'El día {n} de la semana es Martes')
elif n == 3:
    print(f'El día {n} de la semana es Miercoles')
elif n == 4:
    print(f'El día {n} de la semana es Jueves')
elif n == 5:
    print(f'El día {n} de la semana es Viernes')
elif n == 6:
    print(f'El día {n} de la semana es Sabado')
elif n == 7:
    print(f'El día {n} de la semana es Domingo')
else:
    print('Es un error\n')
    
print("Gracias por tu participación")


