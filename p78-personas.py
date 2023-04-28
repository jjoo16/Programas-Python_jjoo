
A = {'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
B = {'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}

print(A.union(B), '\n')
print( A & B), '\n'
print( A - B), '\n'
print( A ^ B), '\n'

print(A.issubset(B))

print(A.issuperset(B))

print('Pedro' in A)
print('Lilia' not in B)

