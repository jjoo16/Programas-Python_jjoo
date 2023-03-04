# Imprime números de 1 a 200 de 10 en 10 (contonue)

import os

os.system('cls')

print('Imprime números de 1 a 200 de 10 en 10 \n')

c = 1
while c <= 200:
    c = c + 1
    if c % 10 != 0:
        continue

    print(c, end= ' ')



