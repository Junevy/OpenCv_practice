
m = -20
print(abs(m)) # 20

mm = 100

print(max(m, mm)) #100
print(min(m, mm)) #-20

print(bool()) # false
print(bool('2')) # true
print(bool(0)) # false
print(bool(100)) # true

# print(hex('a')) # error

a = 20
print(hex(20))

# def function
def my_abs(x):
    if x < 0:
        return -x
    return x

x = -1

print(my_abs(x))
