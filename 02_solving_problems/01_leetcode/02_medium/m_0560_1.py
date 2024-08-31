class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = prefix_sum = 0
        sums = {0:1}

        for num in nums:
            prefix_sum += num
            result += sums.get(prefix_sum - k, 0)
            sums[prefix_sum] = sums.get(prefix_sum, 0) + 1
     
        return result

#OK, 98%, 56%
