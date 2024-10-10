class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
            curr_sum = max(curr_sum, 0)

        return max_sum
