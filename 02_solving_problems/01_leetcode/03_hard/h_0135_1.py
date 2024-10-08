class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for idx in range(1, len(ratings)):
            if ratings[idx] > ratings[idx - 1] :
                candies[idx] = candies[idx - 1] + 1

        for idx in range(len(ratings) - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1] :
                candies[idx] = max(candies[idx + 1] + 1, candies[idx])

        return sum(candies)
