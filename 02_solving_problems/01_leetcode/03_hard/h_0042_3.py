class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        left, right = 0, len(height) - 1
        result = 0
        
        while left < right:
            max_left = max(max_left, height[left])
            
            while left < right and max_left > height[right]:
                max_right = max(max_right, height[right])
                result += max_right - height[right]
                right -= 1
            
            result += max_left - height[left]
            left += 1

        return result
