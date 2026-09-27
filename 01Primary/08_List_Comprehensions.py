ls = [x * x for x in range(10)]
print(ls)

ls1 = [x * x for x in range(10) if x % 2 == 0]
print(ls1)

ls2 = [x + y for x in 'abc' for y in 'xyz']
print(ls2)

import os
dir = [d for d in os.listdir('.')]
print(dir)

dic = {'junevy': 27, 'young': 23, 'expect': 18}

for k,v in dic.items():
    print(k, '=', v)

ls3 = [k + '=' + str(v) for k,v in dic.items()]
print(ls3)