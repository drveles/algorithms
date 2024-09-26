"""
Задан массив целых чисел nums и целое число k, верните общее количество подмассивов, сумма которых равна k.

Подмассив - это непрерывная непустая последовательность элементов внутри массива.
[1,2, 3], 3
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = summ_pref = 0
        all_pref = {0:1}

        for num in nums: 
            summ_pref += num
            result += all_pref.get(summ_pref - k, 0)
            all_pref[summ_pref] = all_pref.get(summ_pref, 0) + 1
        
        return result
