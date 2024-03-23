n = int(input())
fib_tuple = (1, 1, 1)

for i in range(3, n):
    fib_tuple += (sum(fib_tuple[i - 3:i + 1]),)

print(*fib_tuple[:n])
