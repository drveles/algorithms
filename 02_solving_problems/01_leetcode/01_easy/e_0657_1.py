class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dct = Counter(moves)

        return dct.get("U", 0) == dct.get("D", 0) and dct.get("L", 0) == dct.get("R", 0)


# OK, 65%, 91%
