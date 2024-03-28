_ = input()
arr = tuple(map(int, input().split()))
k = int(input())
count_dict = {}

for num in arr:
    count_dict[num] = count_dict.get(num, 0) + 1

for _ in range(k):
    l, r = map(int, input().split())
    count = 0
    for num in count_dict:
        if l <= num <= r:
            count += count_dict[num]
    print(count, sep='', end=' ')

# TL