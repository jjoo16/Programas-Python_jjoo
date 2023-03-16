# suma y promedio de n números introducidos por el usuario

print('Suma de n números introducidos por el usuario:')
num = int(input('Cuantos numeros ? '))
s = 0
for i in range(1,num+1):
    print(f'Número{i}: ', end=' ')
    n = float(input())
    s += n

print(f'\nSuma {s} y el promedio es {s/num:.2f}')



