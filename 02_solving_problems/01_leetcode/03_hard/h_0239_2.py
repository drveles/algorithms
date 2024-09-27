class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        stack = deque()

        for idx, num in enumerate(nums):
            while stack and num > stack[-1][0]:
                stack.pop() 
            stack.append((num,idx,))

            if stack[0][1] == idx - k :
                stack.popleft()

            if idx >= k - 1: 
                result.append(stack[0][0])
        
        return result 
