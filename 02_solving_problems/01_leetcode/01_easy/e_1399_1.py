class Solution:
    def countLargestGroup(self, n: int) -> int:
        dct = defaultdict(int)
        for i in range(1, n + 1):
            temp_sum = 0
            for j in str(i):
                temp_sum += int(j)
            dct[temp_sum] += 1 
        max_size = max(dct.values())
        result = sum(1 for size in dct.values() if size == max_size)
        return result
