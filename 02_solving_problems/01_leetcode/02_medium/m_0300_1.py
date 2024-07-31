class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp_seq = [nums[0]]

        for num in nums:
            if num > temp_seq[-1]:
                temp_seq.append(num)
            elif num < temp_seq[-1]:
                left = 0
                while temp_seq[left] < num:
                    left += 1
                temp_seq[left] = num

        return len(temp_seq)


# OK, 81%, 62%
