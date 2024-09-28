class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, list(str(num)))) for num in nums)


# OK
