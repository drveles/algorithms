class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = temp_res = 0
        temp_num = 0

        for num in nums: 
            if num:
                temp_res += 1
                temp_num = 1
            elif temp_num and not num:
                result = temp_res if temp_res > result else result
                temp_res = 0

        return temp_res if temp_res > result else result


#OK, 92%, 90%
