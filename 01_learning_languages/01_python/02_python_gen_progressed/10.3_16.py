str_tuple = tuple(i.lower() for i in input().split())
result_dict = {}

for c in str_tuple:
    counter_c = result_dict.get(c, 0)
    if counter_c == 0:
        result_dict[c] = 1
    else:
        result_dict[c] += 1
        result_dict[c + '_' + str(counter_c)] = 1

print(*result_dict.keys())