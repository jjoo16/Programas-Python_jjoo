
a = {'50','60','70','80','90','100','200'}
b = {'60','90','100','300','400','500'}
c = {'10', '20','60','90','70','100','600','700'}

print( a | b)
print( b | c)
print( a - c)
print( b ^ c)
print( b & c)

print(a.issubset(b))
print(c.issubset(a))
print('100' in a)
print('60' in a in b in c)
print('900' not in c)

