def tt():
    pass

@tt
def a():
    pass

t = tt

print(t.__name__)
print(tt.__name__)