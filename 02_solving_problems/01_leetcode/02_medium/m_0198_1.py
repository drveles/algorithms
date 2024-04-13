class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)

        if len_nums < 3:
            return max(nums)

        dp = [nums[0], max(nums[0],nums[1])]

        for i in range(2, len_nums):
            dp.append(max(nums[i] + dp[i - 2], dp[i - 1], nums[i]))

        return dp[-1]

#OK 95%, 89%