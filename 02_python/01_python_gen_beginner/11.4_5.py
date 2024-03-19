n = int(input())
seq = []

for _ in range(n):
    temp_string = input()
    if temp_string not in seq:
        seq.append(temp_string)

print(*seq, sep='\n')