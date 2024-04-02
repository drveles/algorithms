class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start_id = 0
        end_id = len(nums) - 1
        while start_id < end_id:
            
            if nums[start_id] == 0: 
                nums.append(nums.pop(start_id))
                end_id -= 1
            else: 
                start_id += 1

#45%, 31%