n = int(input())
seq = []
seq_result = []

for _ in range(n):
    seq.append(int(input()))
for i in range(1, n):
    seq_result.append(seq [i] + seq[i - 1])

print(seq_result)