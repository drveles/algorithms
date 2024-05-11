class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s) 
        res = ''
        
        def getPalindrome(left, right) -> str:
            while left >= 0 and right < len_s and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]

        for id_s in range(len_s):
            palindrom_odd = getPalindrome(id_s, id_s)
            palindrom_even = getPalindrome(id_s, id_s + 1)
            res = max([res, palindrom_odd, palindrom_even], key=len)

        return res


#OK, 90%, 97%