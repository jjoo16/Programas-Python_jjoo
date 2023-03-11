# Calcula las funciones trigonometricas básicas de un angulo en radianes

import math
import os

os.system('cls')
print("calcula las funciones trigonometricas de un angulo en radianes")
angulo = int( input("dame un angulo en radianes:\n"))

seno = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
grados = math.degrees(angulo)

salida = ('resumen de funciones trigonometricas\n')
f'El seno es: {seno}\n'
f'El coseno es : {cos}\n'
f'La tangente es: {tan}\n'
f'El angulo es : {angulo} en radianes equivale a: {grados}'


print(salida)
