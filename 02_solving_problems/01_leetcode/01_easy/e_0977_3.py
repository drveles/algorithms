import sys
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = right = 0
        result = []

        while right < len(nums) and nums[right] < 0:
            right += 1
        left = right - 1

        while -1 < left or right < len(nums):
            left_num = sys.maxsize if -1 >= left else abs(nums[left])
            right_num = sys.maxsize if right >= len(nums) else nums[right]
            if left_num <= right_num:
                result.append(left_num**2)
                left -= 1
            else:
                result.append(right_num**2)
                right += 1

        return result


if __name__ == "__main__":
    print(Solution().sortedSquares([-3, 0, 1, 2]))
