class Solution(object):
    def checkPowersOfThree(self, n):
        nums = [14348907, 4782969, 1594323, 531441, 177147, 59049, 19683, 6561, 2187, 729, 243, 81, 27, 9, 3, 1]

        for num in nums:
            if n >= num:
                n -= num
        return n == 0
