class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_n = len(numbers)
        dct_n = {}
        tgt = abs(target)

        for id1 in range(len_n):
            if numbers[id1] <= tgt or target == 0:
                temp_n = target - numbers[id1] 
                if temp_n in dct_n:
                    return (dct_n[temp_n] + 1, id1 + 1)
                dct_n[numbers[id1]] = id1

# OK, 95% time, 57% mem