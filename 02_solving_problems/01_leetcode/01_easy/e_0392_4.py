class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # о, это делается двумя указателями -> один смотрит на s, другой на t. ищем совпадения из s в t
        s_pointer = t_pointer = 0

        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1

        return s_pointer == len(s)
