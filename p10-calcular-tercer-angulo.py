# Calcular el tercer angulo de un triangulo dados 2 angulos previemanete

import os
import math

os.system('cls')
print('Calcular el tercer angulo de un triangulo dados 2 angulos previemanete\n')
a1 = int(input('Dame 1er angulo? '))
a2 = int(input('Dame 2do angulo? '))

a3 = 180 - (a1 + a2)

print(f'\nEl tercer angulo es {a3}')
