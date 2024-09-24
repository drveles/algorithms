"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

# Нужно пройти двумя указателями по массиву, собирая ровновозрастающие открезки в строки. ВАЖНО: учесть последнее вхождение и первое.
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums):
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]

        result = [] 
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[right - 1] + 1 != nums[right]:
                if left == right - 1:
                    result.append(str(nums[left]))
                else:
                    result.append(f"{nums[left]}->{nums[right-1]}")
                left = right
            
            right += 1
        
        if left == right - 1:
            result.append(str(nums[left]))
        else:
            result.append(f"{nums[left]}->{nums[right-1]}")
        
        return result