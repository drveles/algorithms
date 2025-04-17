class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        # о боже, внимательне условия читай
        # ограничения лайтовые - перебираем

        result = 0

        for idx, inum in enumerate(nums):
            for jdx in range(idx+1, len(nums)):
                if inum == nums[jdx] and not idx * jdx % k:
                    result += 1

        return result
