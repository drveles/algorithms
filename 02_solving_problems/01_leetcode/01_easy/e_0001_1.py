class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for id, el in enumerate(nums):
            if target - el in nums_dict:
                return (
                    nums_dict[target - el],
                    id,
                )
            nums_dict[el] = id


# OK
# time 70%, mem 41%
