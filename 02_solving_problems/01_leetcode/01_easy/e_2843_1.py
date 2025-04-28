class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0

        while low <= high:
            str_num = str(low)
            len_num = len(str_num)
            low += 1
            if len_num % 2:
                continue
            idx = left = right = 0
            while idx < len_num // 2:
                left += int(str_num[idx])
                right += int(str_num[-(idx+1)])
                idx += 1
            if left == right:
                result += 1

        return result
