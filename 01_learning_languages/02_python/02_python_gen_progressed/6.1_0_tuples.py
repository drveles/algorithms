numbers = (0, 1, 3, 14, 2, 7, 9, 8, 10)
print(numbers)

s = 'симпотичный'
print(s)

a = list(s)
a[4] = 'а'
s = ''.join(a)
print(s)
print(type(s))

s = 'симпотичный'
print(s)

writer = ('Лев Толстой', 1827)
print(writer)

a = list(writer)
a[1] = 1828
writer = tuple(a)
print(writer)
print(type(writer))