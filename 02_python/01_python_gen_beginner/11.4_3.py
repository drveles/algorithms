n = int(input())
seq = []
seq_res = []

for _ in range(n):
    temp_value= int(input())
    seq.append(temp_value)
    seq_res.append((temp_value ** 2 + 2 * temp_value + 1))

print(*seq, sep='\n')
print()
print(*seq_res, sep='\n', end='')