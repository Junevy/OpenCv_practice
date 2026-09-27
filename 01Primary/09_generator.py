
g = (x * x for x in range(1, 10))

print(g)

g1 = next(g)
print(g1)

for n in g:
    print(n)
