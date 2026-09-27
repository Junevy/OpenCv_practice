def nop():
    pass # do nothing

nop()

x = -10

def my_abs(x):
    if not isinstance(x, int):
        raise TypeError('the type is error')
    elif x < 0:
        return -x;
    else:
        return x;

print(my_abs(-10))