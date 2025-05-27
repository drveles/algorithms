class Solution:
    def trap(self, height: List[int]) -> int:
        left = result = 0
        right = len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if height[left] > height[right]:
                right -= 1
                if height[right] < right_max:
                    result += min(left_max, right_max) - height[right]
                else:
                    right_max = height[right]
            else: 
                left += 1
                if height[left] < left_max:
                    result += min(left_max, right_max) - height[left]
                else:
                    left_max = height[left]

        return result
