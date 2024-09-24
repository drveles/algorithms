# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.

# Я хочу пройти циклом и будем хранить текущее и предыдущее количество единиц.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = curr_wind = prev_wind = 0

        for num in nums: 
            if not num: 
                result = max(result, curr_wind + prev_wind)
                prev_wind = curr_wind
                curr_wind = 0
            else: 
                curr_wind += 1
        result = max(result, curr_wind + prev_wind)

        return result - 1 if result == len(nums) else result

