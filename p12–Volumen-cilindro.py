# Calcular el volumen de un cilindro dado su radio y altura

import os
import math

os.system('cls')
print('Calcular el volumen de un cilindro dado su radio y altura\n')
rad = int(input('Dame el radio? '))
alt = int(input('Dame su altura? '))

vol = math.pi*(rad**2)*alt

print(f'El Volumen del circulo es {vol}')

