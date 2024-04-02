class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        nums_count  = {}

        for i in nums: 
            nums_count[i] = nums_count.get(i, 0) + 1
        while k:
            max_counter = max(nums_count.values())
            for el in nums_count:
                if nums_count[el] == max_counter:
                    answer += [el] 
                    del nums_count[el] 
                    break
            k -= 1

        return answer
    
# 6%, 73% 