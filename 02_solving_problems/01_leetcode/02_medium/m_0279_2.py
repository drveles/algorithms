class Solution:
    def numSquares(self, n: int) -> int:    
        dp = [0] * (n + 1)

        for end in range(1, n + 1):
            temp = sys.maxsize
            start = 1

            while start * start <= end:
                temp = min(temp, dp[end - start * start] + 1)
                start += 1 
            
            dp[end] = temp

        return dp[-1]
