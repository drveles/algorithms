class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        has_zeroes = False

        for _, num in enumerate(nums):
            if num or has_zeroes:
                prefix *= num
            else:
                has_zeroes = True

        return [(0 if num else prefix) if has_zeroes else prefix // num for num in nums]
