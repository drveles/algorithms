my_dict = {}

for _ in range(int(input())):
    a = input().split()
    my_dict.update(((a[0],a[1]), (a[1], a[0])))

print(my_dict.get(input()))
