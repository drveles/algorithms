class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        destack = deque()
        result = []

        for idx, num in enumerate(nums):
            while destack and num > nums[destack[-1]]:
                destack.pop()
            if destack and destack[0] <= idx - k:
                destack.popleft()
            destack.append(idx)
            if idx >= k - 1:
                result.append(nums[destack[0]])

        return result
