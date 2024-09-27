class Solution:
    def maxPower(self, s: str) -> int:
        result = temp = 1
        prev = s[0]

        for idx in range(1, len(s)):
            if s[idx] == prev:
                temp += 1
            else:
                result = max(result, temp)
                temp = 1
            prev = s[idx]
        result = max(result, temp)

        return result
