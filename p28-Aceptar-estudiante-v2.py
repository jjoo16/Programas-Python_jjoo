# Dado el nombre del estudiante, sexo, edad y 3 calificaciones decidir si se acepta 

import os

os.system('cls')
print('Dado el nombre del estudiante, sexo, edad y 3 calificaciones decidir si se acepta\n')
nombre = input('Dame tu nombre? \n')
sexo = input('Cual es tu sexo H / M ? \n').upper()
edad = int(input('Cual es tu edad? \n'))

print('Dame 3 calificaciones separados por Enter?')

n1, n2, n3 = int(input()), int(input()), int(input())
prom = (n1 + n2 + n3)/3


print(f'El promedio de tus calificaciones es {prom}, tu sexo {sexo}, edad {edad}, por lo tanto:\n')


if prom < 8: 
    print('Estas Rechazado')
elif sexo == 'H':
    print('Estas fuera, solo es para mujeres')
elif edad < 21:
    print('Estas rechazado por se menor')
else:
    print('Felicidades has sido aceptado')

print('Gracias por participar')