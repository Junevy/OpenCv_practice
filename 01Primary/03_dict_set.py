d = {'juenvy': 18, 'young': 15}

print(d['juenvy'])

d['young'] = 18
print(d['young'])

d['test'] = 99
print(d['test'])

t = d.get('t', -1)
print(t)

# delete
d.pop('test')
print(d)

# set
# s = {1,2,3}
# print(s)

# ret = s.add(2)
# print(ret)

# if ret is None:
#     print('None__')

# test: put the list ot the set: error
# s.add([1,2,4])
# print(s)

# ok
# se = set([12,3,33])
# print(se)

s1 = {1,2,3}
s2 = {2,3,4}

print(s1 & s2)
print(s1 | s2)

