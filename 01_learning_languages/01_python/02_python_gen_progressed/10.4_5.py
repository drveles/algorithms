my_dict = {}

for _ in range(int(input())):
    a_tuple = tuple(input().split())
    my_dict.update(((a_tuple[0], a_tuple[1:]),))

for _ in range(int(input())):
    inp_str = input()
    for el in my_dict:
        if inp_str in my_dict[el]:
            print(el)