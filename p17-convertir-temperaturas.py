# Convierte una temperatura de grados celcius a farenheit y viceversa

import os

os.system('clear')
print('Convierte una temperatura Celcius a farenheit o viceversa')
opcion = input('[C]elcius [F]arenheit ?').upper()

if opcion == 'C':
    print('\n Converitir a Celcius')
    temp = float(input('Dame grados Farenheit ?'))
    res = (temp -32)*5/9
    print(f'{temp} grados farenheit, equivale a {res} grados celcius')
else:
    print('\n Converitir a Farenheit')
    temp = float(input('Dame grados Celcius ?'))
    res = (temp*9/5)+32
    print(f'{temp} grados celcius, equivale a {res} grados farenheit')
    