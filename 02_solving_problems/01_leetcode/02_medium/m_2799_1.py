class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        unique_len = len(set(nums))
        result = left = 0
        window = dict()
        for right, num in enumerate(nums):
            window[num] = right
            if len(window) == unique_len:
                while left <= right:
                    result += len(nums) - right 
                    if window[nums[left]] == left:
                        del window[nums[left]]
                        left += 1
                        break
                    left += 1
        return result
