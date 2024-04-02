class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}

        for el1 in strs:
            sorted_el1 = ''.join(sorted(el1))
            if sorted_el1 in result_dict:
                result_dict[sorted_el1] = result_dict[sorted_el1] + [el1]
            else:
                result_dict[sorted_el1] = [el1]

        return result_dict.values()

# OK - [ Time taken: 1 hr 16 m 23 s ] 
# runtime 89%, mem 52%