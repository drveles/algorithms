def recursion_sum(num):
    sum_of_digits = 0
    while num >= 10:
        sum_of_digits += num % 10
        num //= 10
    sum_of_digits += num
    if sum_of_digits >= 10:
        sum_of_digits = recursion_sum(sum_of_digits)
    return sum_of_digits

stock_num = int(input())
print(recursion_sum(stock_num))

# OK