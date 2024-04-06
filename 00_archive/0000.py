x = 198
y = 201

print(bin(x))
print(bin(y))

x ^= y
print(x, bin(x))
print(y, bin(y))
y ^= x
print(x, bin(x))
print(y, bin(y))
x ^= y
print(x, bin(x))
print(y, bin(y))
