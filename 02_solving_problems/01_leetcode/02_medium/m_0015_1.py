class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        len_nums = len(nums)
        result = set()
        
        for start in range(len_nums - 2):
            mid = start + 1
            end = len_nums - 1
            while mid < end:
                temp_res = nums[start] + nums[mid] + nums[end]
                if temp_res > 0:
                    end -= 1
                elif temp_res < 0:
                    mid += 1
                else:
                    result.add((nums[start] , nums[mid],  nums[end]))
                    mid += 1
                    end -= 1

        return result

# OK 17% runtime, 77% mem