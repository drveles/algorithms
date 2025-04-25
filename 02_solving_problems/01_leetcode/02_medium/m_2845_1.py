class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        res = pref = 0
        dct = defaultdict(int)
        dct[0] = 1

        for num in nums:
            if num % modulo == k:
                pref += 1
            res += dct[(pref - k) % modulo]
            dct[pref % modulo] += 1

        return res
