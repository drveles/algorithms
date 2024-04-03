class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        for c in s[::-1].strip():
            if c == ' ':
                break
            result +=1 

        return result
    
# time 98% , mem 27%