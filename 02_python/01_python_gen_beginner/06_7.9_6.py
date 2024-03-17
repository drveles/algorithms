from math import factorial

num = int(input())
sum_factorials = 0

for i in range(1, num + 1):
    sum_factorials += factorial(int(i))
print(sum_factorials)

#OK