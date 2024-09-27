class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        max_right = 0
        left, right = 0, len(height) - 1
        result = 0
        
        while left < right:
            while stack and height[left] > stack[-1]:
                stack.pop()
            stack.append(height[left])
            
            while left < right and stack[0] > height[right]:
                max_right = max(max_right, height[right])
                result += max_right - height[right]
                right -= 1
            
            result += stack[0] - height[left]
            left += 1

        return result
