def f(x):
    return x * x

# The input function has been effect every list item
ret = map(str, range(1,10))
print(list(ret))



# reduce
from functools import reduce

def fn(x, y):
    return x * 10 + y

def charToNums(s):
    return digits[s]

r = reduce(fn, range(2,10))
print(r)

digits = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6}

# re = reduce(fn, map(charToNums, '1234'))
# print(re)
# print(isinstance(re, str))

# def strToNum(s):
#     def fn(x,y):
#         return x * 10 + y
#     def charToNum(z):
#         return digits[z]
#     return reduce(fn, map(charToNum, s))

# # ret = strToNum('123')
# print(ret)
# print(isinstance(ret, int))


ret = reduce(lambda x, y : x * 10 + y, map(charToNums, '1234'))
print(ret)
print(isinstance(ret, int))


# practice
# Trans the illegal alphabeta that user input to Capital 


def nomarlize(name):
    return name.upper()

na = input('plz input your name:')


# ret = map(nomarlize, na)
# print(list(ret))

# reduce: 其实就是把传进去的委托，两两迭代对象，依次作用
# map:    将传递过去的委托 逐一作用到 可迭代对象 上

def prod(n):
    return int(n)

lsNum = [1,2,3]

ret = reduce(lambda x, y : x * y, map(prod, lsNum))
print(ret)