class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_number = 0
        
        for i in nums:
            bit_number ^= i
        
        return bit_number

# OK 
# time 57%, mem 73% beated
# using bit operations to use less memory