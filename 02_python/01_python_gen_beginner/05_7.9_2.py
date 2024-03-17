n = int(input())
for i in range(1, n + 1):
    for j in range(1, (n - (n - i))):
        print(j, end="")
    print(i, end="")
    for k in range(((n - (n - i))), 1, -1):
        print(k - 1, end="")
    if i != n:
        print()
