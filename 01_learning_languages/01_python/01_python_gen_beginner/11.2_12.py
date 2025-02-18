n = int(input())
seq = []

for _ in range(n):
    seq.append(int(input()))
del seq[1::2]

print(seq)