class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)

        for right in range(1, n + 1):
            temp = float("inf")
            left = 1
            while left * left <= right:
                temp = min(temp, dp[right - left * left] + 1)
                left += 1
            dp[right] = temp

        return dp[-1]
