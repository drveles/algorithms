class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        prefs = set()
        result = [0] * len(A)

        for idx in range(len(B)):
            prefs.add(A[idx])
            prefs.add(B[idx])
            result[idx] = 2 * idx + 2 - len(prefs)

        return result


# OK, 77%, 43%
gj 