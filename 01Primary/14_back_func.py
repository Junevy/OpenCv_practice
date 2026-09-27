# back function
def cal_sum(*nums):
    def cal():
        sum = 0
        for n in nums:
            sum += n
        return sum
    return cal

# ls = [1,2,3,4]
f = cal_sum(1,2,3,4,5)
print(f)
ret = f()
print(ret)


# ls = range(1,10)
# t = map(cal_sum, ls)
# print(int(t))

#nonlocal
def inc():
    x = 0
    def t():
        nonlocal x
        x += 1
        return x
    return t

ff = inc()

print(ff())

# practice: return a increment function

def incr():
    i = 0
    def exec():
        nonlocal i
        i +=1
        return i
    return exec

fff = incr()

print(fff())
print(fff())
print(fff())
            



