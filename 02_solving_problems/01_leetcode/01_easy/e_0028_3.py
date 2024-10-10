class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == len(needle) and haystack == needle:
            return 0
            
        needle_hash = hash(needle)

        for idx in range(len(needle) - 1, len(haystack)):
            if hash(haystack[idx + 1 - len(needle):idx + 1]) == needle_hash:
                if haystack[idx + 1 - len(needle):idx + 1] == needle:
                    return idx + 1 - len(needle)
        
        return -1
