"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
# Хочу втупую очистить строку и сравнить ее с зеркальной версией
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_s = ""
        
        for c in s:
            if c.isalnum():
                clear_s += c.lower() 
        
        return clear_s == clear_s[::-1]
