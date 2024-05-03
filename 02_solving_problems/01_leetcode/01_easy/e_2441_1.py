class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1111
        temp_set = set(nums)

        for n in nums:
            if n > res and -n in temp_set:
                res = n

        return -1 if res == -1111 else res
    
#OK, 85%, 26%