class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        len_s = len(s)
        res = 0
        left = 0
        right = 1
        len_occ = 0
        count_c = {}
        count_c[s[0]] = 1
        
        while right < len_s:
            count_c[s[right]] = count_c.get(s[right], 0) + 1
            len_occ = max(count_c.values())
            
            if right - left + 1 - len_occ > k:
                count_c[s[left]] -= 1 
                left += 1
                res = max(res, right - left + 1)
            
            right += 1
        res = max(res, min(len_occ + k, len_s))
        return res 
    
# OK, 51% time, 49% mem