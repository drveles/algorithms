class Solution:
    @staticmethod
    def to_str(start, end):
        return str(end) if start == end else f'{start}->{end}'

    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = list()
        if not len(nums):
            return result
        prev = start = nums[0]

        for num in nums:
            if prev == start == num:
                continue
            if num - 1 != prev:
                result.append(self.to_str(start, prev)) 
                start = num
            prev = num
        result.append(self.to_str(start, num))

        return result
