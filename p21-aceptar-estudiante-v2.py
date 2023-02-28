# Aceptar un estudiante en base a su edad y sus calificaciones

import os

os.system('cls')
print('Aceptar un estudiante en base a su edad y sus calificaciones')

nombre = input('Dame tu nombre?')
edad = int(input('Dame tu edad?'))

if edad >= 18:
    print('No aceptamos menores de edad')
else:
    print('Dame dos calificaciones separadas por Enter')
    c1, c2 = int(input()), int(input())
    if c1>=8 and c2>=8 :
        print('No se aceptamos calificaciones menores de 8')
    else:
        print(f'{nombre} Bienvenido a la universidad, tu edad es {edad}, tus calificaciones son {c1} y {c2} lo permiten')

print('Proceso terminado')

