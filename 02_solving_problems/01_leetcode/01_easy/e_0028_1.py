class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        fast_needle = {needle,}
        len_needle = len(needle)
        len_haystack = len(haystack)

        for idx, char in enumerate(haystack):
            if char == needle[0]:
                if idx + len_needle <= len_haystack and haystack[idx:(idx + len_needle)] in fast_needle: 
                    return idx
        
        return -1

                
#OK, 7%, 42%
    