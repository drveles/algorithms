class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while right - 1 >= 0 and nums[right - 1] <= nums[right]:
            right -= 1

        if right == 0:
            return 0

        while left + 1 < len(nums) and nums[left] <= nums[left + 1]:
            left += 1

        min_val = min(nums[left : right + 1])
        max_val = max(nums[left : right + 1])

        while left > 0 and nums[left - 1] > min_val:
            left -= 1

        while right < len(nums) - 1 and nums[right + 1] < max_val:
            right += 1

        return 0 if right == left else right - left + 1


# OK, 79%, 24%
