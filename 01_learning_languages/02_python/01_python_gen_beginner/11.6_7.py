text_list = input().split()
counter = 0

for i in text_list:
    if i.lower() in ['a', "an", "the"]:
        counter += 1

print("Общее количество артиклей:", counter)
