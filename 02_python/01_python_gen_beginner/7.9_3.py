min_num = int(input())
max_num = int(input())
max_num_with_sum = 0
max_sum_dividers = 0

for i in range(min_num, max_num + 1):
    sum_dividers = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum_dividers += j
    if sum_dividers >= max_sum_dividers:
        max_sum_dividers = sum_dividers
        max_num_with_sum = i
print(max_num_with_sum, max_sum_dividers)

# OK