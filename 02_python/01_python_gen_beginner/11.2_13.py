n = int(input())
seq = []
string = ""


for _ in range(n):
    seq.append(input())
k = int(input())
for i in seq:
    string += i[k-1:k]

print(string)