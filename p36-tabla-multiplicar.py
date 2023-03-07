# Calcula los números de la conjetura collatz 

import os

while (True):
    os.system('cls')
    t = int( input(' Que tabla quieres? '))
    n = int(input('\n Hasta donde la quieres? '))
    c = 1

    while c <= n :
        print(f'{t} * {c} = {t*c} ')
        c +=1

    res = input('\n Deseas continuar (S/N)?')
    if res.upper()=='N':
        break

print('\n Proceso terminado...')