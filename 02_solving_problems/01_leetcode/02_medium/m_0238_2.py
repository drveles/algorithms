class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        result = [1] * len(nums)

        for idx in range(1, len(nums)):
            result[idx] = result[idx-1] * nums[idx-1]

        right = nums[-1]
        for idx in range(len(nums)-2, -1, -1):
            result[idx] *= right 
            right *= nums[idx]
        
        return result

#OK, 87%, 73%