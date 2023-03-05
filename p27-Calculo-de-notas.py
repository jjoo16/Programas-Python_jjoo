# Calcular el promedio de 5 calificaciones introducidas

import os

os.system('cls')
print('Calcular el promedio de 5 calificaciones introducidas\n')
print('Dame 5 calificaciones separados por Enter?')

n1, n2, n3, n4, n5 = int(input()), int(input()), int(input()), int(input()), int(input())
suma = n1 + n2 + n3 +n4 +n5
prom = (n1 + n2 + n3 +n4 +n5)/5
print(f'El promedio de tus calificaciones es {prom}, por lo tanto:\n')
if prom < 6: 
    print('Estas Reprobado')
elif prom > 6.1 and prom < 7:
    print('Pasas de Panzaso')
elif prom > 7.1 and prom < 8:
    print('Muy bien, puedes mejorar')
elif prom > 8.1 and prom < 9:
    print('Excelente sigue así ')
elif prom > 9.1 and prom < 10.1:
    print('Perfecto tu esfuerzo valió la pena ')

print('Gracias por participar')