class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        last = res = 0

        for idx, ch in enumerate(s):
            if ch in seen and seen[ch] >= last:
                last = seen[ch] + 1
            seen[ch] = idx
            res = max(res, idx - last + 1)

        return res
