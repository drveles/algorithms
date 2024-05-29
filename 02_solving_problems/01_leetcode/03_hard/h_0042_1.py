class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1

        max_left_val = height[left]
        max_right_val = height[right]

        while left < right:
            if height[left] < height[right]:
                water += max_left_val - height[left]
                left += 1
                max_left_val = max(max_left_val, height[left])
            else: 
                water += max_right_val - height[right]
                right -= 1
                max_right_val = max(max_right_val, height[right])

        return water

# OK, 97%, 71%