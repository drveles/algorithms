class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def combine(subtarget, source):
            if subtarget == 0:
                return [source]
            elif subtarget < 0:
                return []
            else:
                sub_res = []
                for el in candidates: 
                    if el >= source[-1]:
                        sub_res.extend(combine(subtarget - el, source + [el]))
                return sub_res
            
        for el in candidates: 
            res.extend(combine(target - el, [el]))
 
        return res

#OK 14%, 85% 