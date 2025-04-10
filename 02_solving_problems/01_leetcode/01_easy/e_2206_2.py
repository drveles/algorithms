class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        result = 0

        for num in nums:
            result ^= 1 << num

        return not result
