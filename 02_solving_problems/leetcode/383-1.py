class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        flag = True
        ransom_dict = {}
        magazin_dict = {}
        
        for c in ransomNote:
            ransom_dict[c] = ransom_dict.get(c, 0) + 1
        
        for c in magazine:
            magazin_dict[c] = magazin_dict.get(c, 0) + 1

        for key in ransom_dict: 
            if key in magazin_dict:
                if not magazin_dict[key] >= ransom_dict[key]:
                    flag = False
                    break
            else:
                flag = False
                break
    
        return flag

#OK
#time 31% and 20% to mem