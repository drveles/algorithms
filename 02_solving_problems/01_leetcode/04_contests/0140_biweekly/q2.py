class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        towers = sorted(maximumHeight)
        prev = towers[-1] + 1
        summ = 0
        
        for tower in towers[::-1]:
            temp = tower

            while temp >= prev:
                temp = prev - 1
            
            if temp < 1:
                return -1
            summ += temp
            prev = temp
        
        return summ
    
#OK