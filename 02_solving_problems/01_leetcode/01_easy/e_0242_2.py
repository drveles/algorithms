class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = [0] * 26
        t_arr = [0] * 26
        
        for ch in s:
            s_arr[ord(ch) - 97] += 1
        for ch in t:
            t_arr[ord(ch) - 97] += 1

        return s_arr == t_arr

#OK, 23%, 78%