# Efectua operaciones matematicas con dos valores

print("efectua operaciones matematicas con dos vlores:\n")
print("dame dos valores separados por espacio")

x, y = input().split()
y, y = [float(x), float(y)]

suma = x + y
resta = x - y
mult = x * y
div = x / y
dive = x // y
res = x % y
exp = x ** y

print("suma   :", suma)
print("resta   :", resta)


