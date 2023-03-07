# Calcula los números de la conjetura collatz 

import os

while (True):
    os.system('cls')
    num = int( input(' Dame un número positivo ?' ))


    while num != 1 :
        print(num, end=' ')
        if num % 2 == 0:
            num = num //2
        else:
            num = num * 3 +1
    print(num)

    res = input('\n Deseas continuar (S/N)?')
    if res.upper()=='N':
        break

print('\n Proceso terminado...')





