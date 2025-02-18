a = input().lower()
b = input().lower()
dict_a = {}
dict_b = {}
ignore_str = " .,!?:;-" 

for c in a:
    dict_a[c] = dict_a.get(c, 0) + 1
for c in b:
    dict_b[c] = dict_b.get(c, 0) + 1

for c in ignore_str:
    dict_a.pop(c, 0)
    dict_b.pop(c, 0)

if dict_a == dict_b:
    print("YES")
else:
    print("NO")