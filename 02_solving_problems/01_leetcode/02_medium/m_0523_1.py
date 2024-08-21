class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        curr_remainder = 0

        for idx in range(len(nums)):
            curr_remainder += nums[idx]
            curr_remainder %= k

            if curr_remainder not in remainder_map:
                remainder_map[curr_remainder] = idx
            elif idx - remainder_map[curr_remainder] >= 2:
                return True

        return False


# OK 25%, 31%
