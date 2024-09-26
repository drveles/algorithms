# Given an array of strings strs, group the
# anagrams together. You can return the answer in any order.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for string in strs:
            angaram = str(sorted(string))
            if angaram in result:
                result[angaram].append(string)
            else:
                result[angaram] = [string]

        return result.values()
