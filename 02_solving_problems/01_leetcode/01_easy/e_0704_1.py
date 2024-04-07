from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return -1
        if len_nums == 1 and nums[0] == target:
            return 0

        left = 0
        right = len_nums

        while len_nums // 2:
            len_nums //= 2
            if nums[left + len_nums - 1] == target:
                return left + len_nums - 1
            elif nums[left + len_nums - 1] < target:
                left = left + len_nums
                len_nums = right - left + 1
            else:
                right = left + len_nums - 1
                len_nums = right - left + 1

        return -1


# OK 21% time, 83% mem
