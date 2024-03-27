my_dict = {}

for _ in range(int(input())):
    a_tuple = tuple(input().lower().split())
    my_dict.update(((a_tuple[0], a_tuple[1]),))

for _ in range(int(input())):
    inp_str = input().lower()
    flag = False
    for el in my_dict:
        if my_dict[el] == inp_str:
            print(el,end=' ')
            flag = True
    if not flag:
        print("абонент не найден")
    else:
        print()