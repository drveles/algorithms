class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        else:
            return True

        return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]


#OK, 80%, 70%
