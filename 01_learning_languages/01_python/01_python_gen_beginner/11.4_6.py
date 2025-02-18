n = int(input())
seq = []

for _ in range(n):
    seq.append(input())

search = input()

for i in seq:
    if search.lower() in i.lower():
        print(i)
