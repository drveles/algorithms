class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        flag = False
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s2 < len_s1:
            return False
        left = 0
        s1_dct = {}
        for c in s1:
            s1_dct[c] = s1_dct.get(c, 0) + 1
        s2_dct = {}
        for c in s2[:len_s1]:
            s2_dct[c] = s2_dct.get(c, 0) + 1
        if s1_dct == s2_dct:
            flag = True
        else: 
            for right in range(len_s1, len_s2):
                s2_dct[s2[right]] = s2_dct.get(s2[right], 0) + 1
                s2_dct[s2[left]] -= 1
                if s2_dct[s2[left]] == 0: del s2_dct[s2[left]]
                if s1_dct == s2_dct:
                    flag = True
                    break
                left += 1

        return flag
    
#OK 97% time, 32% mem