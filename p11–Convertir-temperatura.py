# Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit

import os
import math

os.system('cls')
print('Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit\n')
grados = int(input('Dame temperatura en Celcius? '))

gf = (grados* 9/5) + 32

print(f' La temperatura en Farenheit es {gf} ')
