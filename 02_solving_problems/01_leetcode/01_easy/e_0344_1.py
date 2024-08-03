class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(1, len(s) // 2  + 1):
            s[i-1], s[-i] = s[-i], s[i-1]

# OK 56%, 81%