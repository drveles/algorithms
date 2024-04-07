class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_id = 0
        

        if not nums[0] < nums[-1]:
            left, right = 0, len(nums) - 1
            if right == 1:
                return min(nums)
            if right == 0: 
                return nums[0]

            while left < right:
                mid = left + (right - left) // 2 
                if nums[mid] < nums[0]:
                    right = min_id = mid
                else:
                    left = mid + 1
        
            min_id = left if nums[left] < nums[right] else right

        return nums[min_id]

#ok 62%, 22%