class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for idx in range(len(nums)):
            result ^= nums[idx]
            result ^= idx

        return result
