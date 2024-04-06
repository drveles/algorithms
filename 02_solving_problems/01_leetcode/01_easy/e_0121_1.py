class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 
        most_expensive = most_chiper = prices[0]

        for i in prices:
            if i < most_chiper:
                if most_expensive - most_chiper > result:
                    result = most_expensive - most_chiper
                most_expensive = most_chiper = i
            if i > most_expensive: 
                most_expensive = i

        if most_expensive - most_chiper > result:
            result = most_expensive - most_chiper

        return result

#OK 98% time, 72% mem