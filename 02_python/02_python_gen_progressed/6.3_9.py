n = int(input())
students = tuple([tuple(input().split()) for _ in range(n)])

for i in students:
    print(*i)
print()
for i in students:
    if i[-1] in "45":
        print(*i)       
