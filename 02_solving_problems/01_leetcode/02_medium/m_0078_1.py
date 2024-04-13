from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        len_nums = len(nums)
        sub_str = []

        def backtrack(i):
            if i > len_nums - 1:
                ans.append(sub_str.copy())
                return 
            sub_str.append(nums[i])
            backtrack(i + 1)
            sub_str.pop()
            backtrack(i + 1)    
        backtrack(0)    

        return ans
    

if __name__ == "__main__":
    Solution().subsets([1,2,3])