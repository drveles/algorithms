class Solution:
    def checker(self, nums, target, left, mid, right):
        if nums[left] <= nums[mid]:
            return nums[left] <= target < nums[mid]
        else:
            return not nums[mid] < target <= nums[right]


    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if self.checker(nums, target, left, mid, right):
                right = mid - 1
            else:
                left = mid + 1

        return -1
