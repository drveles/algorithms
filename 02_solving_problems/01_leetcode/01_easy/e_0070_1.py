class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4: return n
        
        dp = [1,2,3]
        for i in range(3,n):
            dp.append(dp[i - 1] + dp[i - 2])
        
        return dp[n - 1]

#OK 97%, 30%