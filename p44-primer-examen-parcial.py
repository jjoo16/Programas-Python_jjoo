# Se desea llevar el control de la inscripción a un evento académico
# calcular un subtotal de la venta sumando el precio del tipo de usuario más el precio de tipo de paquete, 
# y multiplicando por la cantidad solicitada. 

import os

while (True):
    os.system('cls')
    print('Se desea llevar el control de la inscripción a un evento académico, Se especifica: Tipo de usuario, paquete y cantidad \n')

    us = input('Dame tipo de usuario [A]lumno, [T]rabajador, [D]ocente? ').upper()
    pa = input('Dame tipo de paquete [C]onferencias, [E]ventos sociales, [K]it de acceso? ').upper()
    Q = int(input('Dame cantidad Solicitada? '))

    if us == 'A':
        u = 100
    
    elif us == 'T':
        u = 200
    elif us == 'D':
        u = 500

    if pa== 'C':
        p = 600
    elif pa == 'E':
        p = 800
    elif pa =='K':
        p = 900

    st = (u + p) * Q

    if st >= 5000 and us == 'A':
        des = st * .20
        tf = st - des
    else:
        des = st * 0
        tf = st


    print(f'El subtotal es {st}')
    print(f'Tu pedido fue de {Q}, de usuario {us}, paquete {pa}')
    print(f'El subtotal es {st} con un descuento de {des} y el total final es de {tf} ')

    print('\nDeseas continuar (S/N) ? ', end= ' ')
    res = input()
    if res.upper() == 'S' or res.upper() == 'N':
            bandera = False
    if res.upper()=='N':
            break
print('Gracias por participar')

 
