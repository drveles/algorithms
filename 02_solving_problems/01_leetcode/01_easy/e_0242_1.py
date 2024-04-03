class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dct = {}
        t_dct = {}

        for el in s:
            s_dct[el] = s_dct.get(el, 0) + 1
        for el in t:
            t_dct[el] = t_dct.get(el, 0) + 1

        return s_dct == t_dct
    
#OK 
# time 93%, mem 91%