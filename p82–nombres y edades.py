# Nombres y edades
import os; os.system('cls')
datos = {}
print('Introduce nombres y edades (nombre vacio para terminar)')
while True:
    nombre = input('Dame el nombre ? ')
    if nombre!='':
        datos[nombre]=int(input('Edad ? '))
    else: 
        break
print(f'El diccionario de datos creado: \n{len(datos)} - {datos}\n')
print('\nListado y promedio de edades:')
s=0
for n,e in datos.items():
    print(f'{n:<20} - {e:2}')
s+=e
print(f'\n\nSuma: {s} y promedio: {s/len(datos)}') 