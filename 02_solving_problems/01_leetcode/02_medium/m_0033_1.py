class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_id = -1
        if not nums[0] < nums[-1]:
            left, right = 0, len(nums) - 1
            if right == 1:
                return left if nums[left] < nums[right] else right                
            if right == 0: 
                return 0

            while left < right:
                mid = left + (right - left) // 2 
                if nums[mid] < nums[0]:
                    right = min_id = mid
                else:
                    left = mid + 1
        
        min_id = left if nums[left] < nums[right] else right
        return min_id

    def bin_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid_el = left + (right - left) // 2

            if nums[mid_el] > target:
                right = mid_el
            elif nums[mid_el] < target:
                left = mid_el + 1
            else:
                return mid_el

        if nums[left] == target:
            return left
        return -1

    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return -1 
        if len_nums == 1 and nums[0] == target:
            return 0
        elif len_nums == 1 and nums[0] != target: 
            return -1 
        if nums[0] < nums[-1]:
            return self.bin_search(nums, target)
        min_id = self.findMin(nums)
        right_res = self.bin_search(nums[min_id:], target)
        right_res = len(nums[:min_id]) + right_res if right_res > -1 else -1

        return max(self.bin_search(nums[:min_id], target), right_res)

#OK 39% time, 54% mem