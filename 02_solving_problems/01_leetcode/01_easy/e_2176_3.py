from collections import defaultdict


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        res = 0
        dct = defaultdict(set)

        for i, num in enumerate(nums):
            if num in dct:
                for j in dct[num]:
                    if not i * j % k:
                        res += 1
            dct[num].add(i)

        return res
