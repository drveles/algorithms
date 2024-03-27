my_list = list()

for _ in range(int(input())):
    temp_key_and_val = list(input().split(":"))
    my_list.append(temp_key_and_val)

for id in range(len(my_list)):
    my_list[id][0] = my_list[id][0].lower()

dictionary = dict(my_list)

for _ in range(int(input())):
    print(dictionary.get((input().lower()), "Не найдено"))
