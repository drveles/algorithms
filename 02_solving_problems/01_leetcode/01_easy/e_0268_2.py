class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0

        for idx, num in enumerate(nums):
            result ^= num
            result ^= idx + 1
        
        return result