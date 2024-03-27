str_tuple = tuple(i.strip(".,!?:;-").lower() for i in input().split())
result_dict = {}
result_list = []

for s in str_tuple:
    result_dict[s] = result_dict.get(s, 0) + 1

min_val = min(result_dict.values())
for el in result_dict: 
    if result_dict[el] == min_val:
        result_list.append(el)

print(sorted(result_list)[0])
