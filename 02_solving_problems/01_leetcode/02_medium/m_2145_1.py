class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        # хочу однопроходно найти минимум и максимум аккумулятивный и вернуть их разницу
        result = accum = min_num = max_num = 0
        for num in differences: 
            accum += num
            min_num = min(accum, min_num)
            max_num = max(accum, max_num)
        given_diff = upper - lower
        accum_diff = max_num - min_num

        return max(given_diff - accum_diff + 1, result)
