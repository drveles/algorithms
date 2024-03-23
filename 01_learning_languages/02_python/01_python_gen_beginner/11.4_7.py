n = int(input())
seq = []
seq_search = []
flag = True

for _ in range(n):
    seq.append(input())

n = int(input())

for _ in range(n):
    seq_search.append(input())

for i in seq:
    print_flag = True
    for j in seq_search:
        if j.lower() not in i.lower():
            print_flag = False
            break
    if print_flag:
        print(i)

# great solution
# s = [input() for _ in range(int(input()))]
# d = [input() for _ in range(int(input()))]
# for i in s:
#     for j in d:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)