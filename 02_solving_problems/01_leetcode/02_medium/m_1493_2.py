class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr = prev = result = 0

        for num in nums:
            if num:
                curr += 1
            else:
                result = max(result, curr + prev)
                prev = curr
                curr = 0

        result = max(result, curr + prev)

        return result - 1 if result == len(nums) else result


# OK, 98%, 63%
