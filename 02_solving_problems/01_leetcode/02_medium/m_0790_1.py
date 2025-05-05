class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5] + [0] * n
        module = 1000000007

        for idx in range(3, n):
            dp[idx] = (dp[idx - 1] * 2 + dp[idx - 3]) % module

        return dp[n-1]
