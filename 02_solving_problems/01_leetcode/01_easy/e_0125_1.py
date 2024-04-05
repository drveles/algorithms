class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ""
        for c in s:
            if c.isalnum():
                s_clean += c
        s_clean = s_clean.lower()
        len_s = len(s_clean)
        for i in range(len_s):
            if s_clean[i] != s_clean[len_s - 1 - i]:
                return False
        
        return True
    
#OK 62% time, 63% mem