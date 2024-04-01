class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = {}

        for i in nums: 
            dct[i] = dct.get(i, 0) + 1
        
        for i in dct:
            if dct[i] == 1:
                return(i)
                

# OK 
# time 22%, mem 73% beated
# may be faster if use bit manipulations