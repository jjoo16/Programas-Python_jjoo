# Calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados

import os
import math


os.system('cls')
print('Calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados')
n1 = int(input('Dame Lado 1? '))
n2 = int(input('Dame Lado 2? '))

hip = math.sqrt(n1**2 + n2**2)

print(f'La hipotenusa es {hip}')
