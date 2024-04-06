class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        wind = set()
        left = 0

        for right in range(len(s)):
            if s[right] not in wind:
                wind.add(s[right])
            else:
                len_wind = len(wind)
                if len_wind > res:
                    res = len_wind
                while s[left] != s[right]:
                    wind.discard(s[left])
                    left += 1  
                left += 1          
        len_wind = len(wind)
        if len_wind > res:
            res = len_wind

        return res

#OK, 76% time, 60% memory