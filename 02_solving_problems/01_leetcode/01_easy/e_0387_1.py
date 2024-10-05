class Solution:
    def firstUniqChar(self, s: str) -> int:
        counted = Counter(s)

        for idx, char in enumerate(s): 
            if counted[char] == 1:
                return idx

        return -1
