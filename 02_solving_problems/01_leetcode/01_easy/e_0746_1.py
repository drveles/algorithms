class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        preprev = cost[0]
        prev = cost[1]

        for i in range(2, len(cost)):
            temp = cost[i] + min(prev, preprev)
            preprev = prev
            prev = temp

        return min(prev, preprev)

#OK, 73%, 28%