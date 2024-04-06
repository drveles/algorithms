class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        wind = set()

        for i, c in enumerate(s):
            if c not in wind:
                wind.add(c)
            else:
                len_wind = len(wind)
                if res < len_wind:
                    res = len_wind
                wind.clear()
                wind.add(c) 
                for ch in range(i - 1, -1, -1):
                    if s[ch] == c:
                        break
                    wind.add(s[ch]) 
        len_wind = len(wind)
        if res < len_wind:
            res = len_wind
        
        return res
    
# firs solution, not so good