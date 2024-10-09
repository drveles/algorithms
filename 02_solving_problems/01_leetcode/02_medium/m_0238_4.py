class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        premult = postmult = 1

        for idx, num in enumerate(nums):
            answer[idx] = premult
            premult *= num
        
        for idx in range(len(nums)-1, -1, -1):
            answer[idx] *= postmult
            postmult *= nums[idx]

        return answer
