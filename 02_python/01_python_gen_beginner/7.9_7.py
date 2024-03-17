min_num = int(input())
max_num = int(input())
if min_num < 2:
    min_num = 2

for i in range(min_num, max_num + 1):
    div_counter = 0
    for j in range(1, max_num + 1):
        if i % j == 0:
            div_counter += 1
    if div_counter == 2:
        print(i)

# OK