class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        curr_id = 0

        for c_t in t:
            if s[curr_id] == c_t:
                curr_id += 1
                if curr_id == len(s):
                    return True

        return False


# OK, 71%, 91%
