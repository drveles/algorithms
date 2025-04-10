class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        pairs = dict()

        for num in nums:
            pairs[num] = pairs.get(num, 0) + 1
        
        for val in pairs.values():
            if val % 2:
                return False
        
        return True
