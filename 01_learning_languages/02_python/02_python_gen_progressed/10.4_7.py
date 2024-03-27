str_inputed = input()
my_dict1 = {}

for c in str_inputed:
    my_dict1[c] = my_dict1.get(c, 0) + 1
for _ in range(int(input())):
    char, count = tuple(input().split(": "))
    for el in my_dict1: 
        if my_dict1[el] == int(count):
            my_dict1[el] = char

for c in str_inputed:
    print(my_dict1[c], sep='', end='')