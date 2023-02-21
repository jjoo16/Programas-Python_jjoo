# Divide un núemro de 3 cifras en centenas, decenas, unidades
# 971 9 centenas 7 decenas 1 unidad

import math
import os
os.system('cls')
print('Divide un numero en centenas, decenas, unidades')
num = int(input('dame un númnero de tres cifras:'))

centenas = num // 100
decenas = ( num - (centenas * 100)) // 10
unidades = num - centenas*100- decenas*10



print('centenas',centenas)
print('decenas', decenas)
print('unidades', unidades)





