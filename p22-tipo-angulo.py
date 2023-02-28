# Muestra el tipo de angulo

import os

os.system('cls')
print('Muestra el tipo de angulo:\n')
angulo = int(input('Dame el angulo'))

if angulo>= 0 and angulo <360:
    print(f'El angulo es:')
    if angulo < 90:
        print('El angulo es agudo')
    elif angulo == 90:
        print('El angulo es recto')  
    elif angulo > 90 and angulo <180:
        print('El angulo es obtuso ')
    elif angulo == 180:
        print('El angulo es Llano')
    elif angulo > 180 and angulo < 360:
        print('El angulo es Concavo')
else:
    print('El angulo esta fuera de rango')

print('Proceso terminado')



