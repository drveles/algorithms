"""
0 0 1 0 2 -> 1 2 0 0 
Я хочу пройти двумя указателями и если нашел 0, то на его место ищу число следующим указателем.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:        
        left = right = 0

        while left < len(nums) and right < len(nums):
            if not nums[left]:
                if right < left:
                    right = left
                while right < len(nums) - 1 and not nums[right]:
                    right += 1
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
            left += 1

