# Calcular la paga total de un trabajador

print( "Calcular la paga total de un trabajador:\n")
nombre = input ("Dame tu nombre : ")
horas = int(input("horas trabajadoras: "))
paga = float(input("paga por hora: "))

tasa = 0.3

pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print("\nResumen de pagos : \n")
print(f"El trabajador {nombre} trabajo {horas} horas con una paga de {paga}, impuesto de {tasa}% ")
print(f"paga bruta : {pagabruta}")
print(f'Impuesto {impuesto}')
print(f"paga neta : {paganeta}")
