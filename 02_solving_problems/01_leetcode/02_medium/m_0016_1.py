class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        if target < result:
            return result
        if target > sum(nums[-3:]):
            return sum(nums[-3:])

        for idx in range(len(nums) - 2):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                temp = nums[idx] + nums[left] + nums[right]
                if temp == target:
                    return temp
                result = result if abs(target - result) < abs(target - temp) else temp
                if temp < target:
                    left += 1
                else: 
                    right -= 1

        return result 
