

c1 = {1,2,3,4,5}
c2 = {2,3,4,6,7,8,9}
c3 = {9,10,11,12,13}
c4 = {3,4,5}

print(c1, c2, c3, c4, '\n')

print(c1.union(c2), '\n')
print(c2 | c3, '\n')

print(c1.intersection(c2), '\n')
print(c1 & c2)

print(c1.difference(c2), '\n')
print(c1-c2)

print(c1.symmetric_difference(c2), '\n')
print(c1 ^ c2)

print(c1.issubset(c4))
print(c1>=c4)
print(c2.issuperset(c3), '\n')
print(4 in c1)
print(4 not in c1)

