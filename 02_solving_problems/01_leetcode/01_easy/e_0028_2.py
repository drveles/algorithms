class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx, char in enumerate(haystack):
            if char == needle[0]:
                if idx + len(needle) <= len(haystack) and haystack[idx:(idx + len(needle))] == needle: 
                    return idx
        
        return -1

#OK, 79%, 10%