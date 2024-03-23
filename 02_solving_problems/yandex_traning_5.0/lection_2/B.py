days, spoiled = map(int, input().split())
price_list = list(map(int, input().split()))
max_profit = 0

for i in range(days):
    for j in range(i+1, min(i + 1 + spoiled, days)):
        if max_profit < price_list[j] - price_list[i]:
            max_profit = price_list[j] - price_list[i]
print(max_profit)

# OK                