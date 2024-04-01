class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0

        while num: 
            if num & 1: 
                num -= 1 
                result += 1
            else:
                num >>= 1
                result += 1
        
        return result

#OK
#time 75% mem 95%