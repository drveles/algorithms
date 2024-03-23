seq = []

for i in "abcdefghijklmnopqrstuvwxyz":
    seq.append(i * (ord(i) - 96))

print(seq)