def is_odd(x):
    return x % 2 == 0

ls = range(1,10)

ret = filter(is_odd, ls)
print(list(ret))

ls2 = ['A', '', 'B', None, 'C', '  ']

def is_str(x):
    return x and x.strip()


ret2 = filter(is_str, ls2)
print(list(ret2))
