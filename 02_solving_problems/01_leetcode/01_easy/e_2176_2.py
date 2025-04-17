class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        # идея такая - сохранять числа и их индексы в словарь. и однопроходно проверить все пары
        res = 0
        dct = dict()

        for i, num in enumerate(nums):
            if num in dct:
                for j in dct[num]:
                    if not i * j % k:
                        res += 1
            else:
                dct[num] = {i,}
            dct[num].add(i)

        return res
