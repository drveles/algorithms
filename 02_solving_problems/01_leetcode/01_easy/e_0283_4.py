class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0

        while right < len(nums):
            if not (left == right and nums[left]):
                while not nums[right] and right < len(nums) - 1:
                    right += 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
