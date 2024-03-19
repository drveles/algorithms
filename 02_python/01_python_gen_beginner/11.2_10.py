n = int(input())
seq = []

for i in range (1, n + 1):
    if n % i == 0:
        seq.append(i)

print(seq)