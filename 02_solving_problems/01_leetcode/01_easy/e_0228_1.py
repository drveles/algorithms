class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return
        left = right = 0
        temp = nums[0]
        res = []

        while right < len(nums):
            if nums[right] == temp or nums[right] == temp + 1:
                temp = nums[right]
            else:
                if nums[left] != temp:
                    res.append(f"{nums[left]}->{temp}")
                else:
                    res.append(f"{temp}")
                left = right
                temp = nums[right]
            right += 1
        if nums[left] != temp:
            res.append(f"{nums[left]}->{temp}")
        else:
            res.append(f"{temp}")

        return res