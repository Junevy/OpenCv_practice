d ={'juenvy': 18, 'young': 22}

for x in d:
    print(x)

for x in d.values():
    print(x)

for x in d.items():
    print(x)

from collections.abc import Iterable

print(isinstance('xy', Iterable))

for s in 'xy':
    print(s)

print(isinstance(12, Iterable))
