# Calcula la paga de untrabajador considerando 40 horas jornada  las horas extras Se pagan al doble

import os

os.system('cls')

print('Calcula la paga de untrabajador considerando 40 horas jornada y las horas extras Se pagan al doble\n')
nombre = input('Dame tu nombre ?')
horas = int(input('Horas trabajadas ?'))
paga = float(input('paga por hora ? '))

if horas > 40:
    extra = horas - 40
    total = (40 * paga ) + (extra * paga)
total = horas * paga

print(f'\n {nombre} trabajo {horas} horas con una paga de {paga} pesos, total del pago {total} pesos')
print(f'Con un total de horas extras de {extra}')

