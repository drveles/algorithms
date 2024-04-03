class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}

        for i in nums:
            nums_count[i] = nums_count.get(i, 0) + 1
        answer = sorted(nums_count, key=lambda x: nums_count[x], reverse=True)

        return answer[:k]

# OK
# 42% runtime, 73% memory
