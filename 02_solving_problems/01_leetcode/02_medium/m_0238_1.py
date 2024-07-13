class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cntr = 0
        multed_nums = reduce((lambda x, y: (x if x else 1) * (y if y else 1)), nums)

        for num in nums:
            if num == 0:
                zero_cntr += 1

        for idx in range(len(nums)):
            if zero_cntr == 1:
                if nums[idx] == 0:
                    nums[idx] = multed_nums
                else:
                    nums[idx] = 0
            elif zero_cntr == 0:
                nums[idx] = int(multed_nums / nums[idx]) if nums[idx] else multed_nums
            else:
                nums[idx] = 0

        return nums


# OK, 47%, 97%
