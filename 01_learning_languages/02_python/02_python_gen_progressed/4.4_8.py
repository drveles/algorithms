listing = []
n, m = int(input()), int(input())
for _ in range(n):
    listing.append([input() for _ in range(m)])

for i in listing:
    print(*i)
