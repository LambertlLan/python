a = ['a', [1, 2, 3]]
# b = a
b = a.copy()
a[0] = 0
print(a)
print(b)
