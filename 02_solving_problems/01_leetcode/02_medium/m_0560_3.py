class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = res = 0
        pref_ctr = defaultdict(int)
        pref_ctr[0] = 1

        for num in nums:
            pref += num
            res += pref_ctr[pref - k]
            pref_ctr[pref] += 1

        return res
