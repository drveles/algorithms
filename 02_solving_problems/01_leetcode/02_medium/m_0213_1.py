class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        def dp(nums):
            temp = [0] * len(nums)
            temp[0] = nums[0]
            temp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                temp[i] = max(temp[i - 1], temp[i - 2] + nums[i])

            return temp[-1]

        return max(dp(nums[:-1]), dp(nums[1:]))


# OK, 65%, 73%
