class Solution:
    def longestSubarray(self, nums) -> int:
        res = last = curr = 0

        for num in nums:
            if num: 
                curr += 1 
            else:
                last, curr = curr, 0
            res = max(res, last + curr)

        return res - (len(nums) == res)
    
if __name__ == "__main__":
    # print(Solution().longestSubarray([0, 0, 0, 0]))
    # print(Solution().longestSubarray([0, 1]))
    print(Solution().longestSubarray([1,1,0,1]))

#OK, 81%, 26%