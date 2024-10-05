class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prefixs = {}
        
        for idx, num in enumerate(numbers):
            if target - num in prefixs:
                return [prefixs[target - num] + 1, idx + 1] 
            prefixs[num] = idx
