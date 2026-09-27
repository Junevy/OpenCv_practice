def power(x, y = 2):
    return x * y

print(power(2))

def mult_param(*number):
    n = 0
    for n in number:
        n += n
    return n

print(mult_param(1,2))