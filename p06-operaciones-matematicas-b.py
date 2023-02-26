# Efectua operaciones matematicas con dos valores

print("efectua operaciones matematicas con dos valores:\n")
print("dame dos valores separados por espacio:")

x, y = input().split()
x, y = [float(x), float(y)]

suma = x + y
resta = x - y
mult = x * y
div = x / y
dive = x // y
res = x % y
exp = x ** y

print(F"suma: {suma}\n resta: {resta}\n multiplicación: {mult}\n")
print(f'división: {div}\n div entera: {dive}\n Residuo: {res}')
print(f'Exponenciación: {exp}\n')



