class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp2 = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp2[i][j] = dp2[i - 1][j] + dp2[i][j - 1]

        return dp2[-1][-1]


# OK, 90%, 76%
