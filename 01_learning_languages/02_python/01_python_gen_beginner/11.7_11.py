nums_squared = [int(i) ** 2 for i in input().split() if int(i) % 2 == 0]

print(*[i for i in nums_squared if str(i)[-1] != '4'])