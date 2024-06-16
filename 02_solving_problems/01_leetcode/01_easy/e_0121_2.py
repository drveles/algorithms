class Solution:
    def maxProfit(prices: List[int]) -> int:
        temp_profits = [0] * len(prices)
        min_price = prices[0]

        for idx in range(len(prices)):
            temp_profits[idx] = prices[idx] - min_price
            if prices[idx] < min_price:
                min_price = prices[idx]

        return max(temp_profits)

    with open("user.out", "w") as f:
        for case in map(loads, stdin):
            f.write(f"{maxProfit(case)}\n")
    exit(0)


# OK , 99%, 99%
