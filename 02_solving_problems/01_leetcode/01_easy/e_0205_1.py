class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        eq_dict = {}

        for idx in range(len(s)):
            if s[idx] not in eq_dict:
                eq_dict[s[idx]] = t[idx]
            elif eq_dict[s[idx]] != t[idx]:
                return False

        return True and len(set(eq_dict.values())) == len(set(eq_dict.keys()))


# OK 33%, 77%
