

ls = [-22, 22, -99, 0, -4, 5]
print(sorted(ls))

# delegate
print(sorted(ls, key=abs))

lsName = ['Credit', 'Zoo', 'about', 'bob']
print(sorted(lsName, key=str.lower))