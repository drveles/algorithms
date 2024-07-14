class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        mono_queue = deque()

        for idn in range(k):
            while mono_queue and nums[idn] > mono_queue[-1][0]:
                mono_queue.pop()
            mono_queue.append((nums[idn], idn))
        result.append(mono_queue[0][0])

        for idn in range(k, len(nums)):
            if mono_queue and mono_queue[0][1] == idn - k: 
                mono_queue.popleft()
            
            while mono_queue and nums[idn] > mono_queue[-1][0]:
                mono_queue.pop()

            mono_queue.append((nums[idn], idn))
            result.append(mono_queue[0][0])

        return result

#OK, 63%, 63%