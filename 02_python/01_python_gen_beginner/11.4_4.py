n = int(input())
seq = []
seq_res = []

for _ in range(n):
    temp_value = int(input())
    seq.append(temp_value)

for i in range(len(seq)):
    if seq[i] == min(seq) or seq[i] == max(seq):
        continue    
    seq_res.append(seq[i])


print(*seq_res, sep='\n', end='')