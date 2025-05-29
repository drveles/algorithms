class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        seen = {0: -1}

        for idx, num in enumerate(nums):
            prefix = (prefix + num) % k

            if prefix not in seen:
                seen[prefix] = idx
            elif idx - seen[prefix] >= 2:
                return True

        return False
