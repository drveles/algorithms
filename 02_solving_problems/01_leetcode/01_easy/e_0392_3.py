class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        for sc in s:
            while left < len(t):
                if t[left] == sc:
                    break
                left += 1
            else:
                return False
            left += 1
        else: 
            return True
