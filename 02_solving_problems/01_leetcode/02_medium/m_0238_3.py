class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        mult = 1
        ctr_zero = 0

        for num in nums:
            if num == 0:
                ctr_zero += 1
            else:
                mult *= num

        if ctr_zero > 1:
            return answer
        
        for idx, num in enumerate(nums):
            if ctr_zero > 0 and num == 0:
                print(mult)
                answer[idx] = mult
            elif not ctr_zero:
                answer[idx] = mult // nums[idx]
        
        return answer