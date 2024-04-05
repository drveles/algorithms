class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        start = 0
        end = len(height) - 1
        
        while start < end:
            temp = min((height[start], height[end])) * (end - start)
            if temp > res:
                res = temp
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return res

#OK, 74 runtime, 94 mem