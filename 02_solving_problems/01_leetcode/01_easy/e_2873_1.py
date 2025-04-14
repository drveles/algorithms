class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        result = max_complex = max_prev = 0

        for num in nums:
            result = max(result, max_complex * num)
            max_complex = max(max_complex, max_prev - num)
            max_prev = max(max_prev, num)
        
        return result
