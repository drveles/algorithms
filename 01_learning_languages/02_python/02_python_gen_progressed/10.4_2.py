a = input()
b = input()
dict_a = {}
dict_b = {}

for c in a:
    dict_a[c] = dict_a.get(c, 0) + 1
for c in b:
    dict_b[c] = dict_b.get(c, 0) + 1

if dict_a == dict_b:
    print("YES")
else:
    print("NO")