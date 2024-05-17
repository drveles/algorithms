class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] == nums[left+1]:
                right -= 1 
                nums.append(nums.pop(left+1))
            else: 
                left += 1
        
        return left + 1 

#OK 5%, 23%