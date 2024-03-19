n = int(input())
nums_neg = []
nums_zeros = []
nums_pos = []

for _ in range(n):
    temp = int(input())
    if temp < 0:
        nums_neg.append(temp)
    elif temp == 0:
        nums_zeros.append(temp)
    else:
        nums_pos.append(temp)

print(*(nums_neg + nums_zeros + nums_pos), sep='\n')
