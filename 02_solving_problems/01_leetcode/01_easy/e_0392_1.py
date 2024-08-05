class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev_id = 0

        for c_s in s:
            for id_t in range(prev_id, len(t)):
                if t[id_t] == c_s:
                    prev_id = id_t + 1
                    break
            else:
                return False

        return True

# OK, 42%, 60%
