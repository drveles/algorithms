class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        
        for right in range(len(nums)):
            if right > left and nums[right]:
                nums[left], nums[right] = nums[right], nums[left]

            while left < len(nums) - 1 and nums[left]:
                left += 1
