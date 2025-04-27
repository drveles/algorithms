class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        res = 0

        for idx in range(1, len(nums) - 1):
            if nums[idx - 1] + nums[idx + 1] == nums[idx] / 2:
                res += 1
        
        return res
