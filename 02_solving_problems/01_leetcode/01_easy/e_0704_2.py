from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid_el = left + (right - left) // 2

            if nums[mid_el] > target:
                right = mid_el
            elif nums[mid_el] < target:
                left = mid_el + 1
            else:
                return mid_el

        if nums[left] == target:
            return left
        return -1


# OK 90% time, 83% mem
