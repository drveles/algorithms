n = int(input())
count = 1
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(str(count))
        count += 1
    print(' '.join(row))
