class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0,1,1]
        if n < 3: return nums[n]
        for _ in range(n - 2):
            nums.append(sum(nums))
            nums.pop(0)
        return nums.pop()

# OK 74%, 85%