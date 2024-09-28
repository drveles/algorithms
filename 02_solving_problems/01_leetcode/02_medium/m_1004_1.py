class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0

        while right < len(nums):
            if not nums[right]:
                k -= 1
            if k < 0:
                if not nums[left]:
                    k += 1
                left += 1
            right += 1
        
        return right - left 
