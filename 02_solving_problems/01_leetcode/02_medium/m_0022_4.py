class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def plus_one(s: str, opened: int) -> str:
            if len(s) == n * 2:
                if not opened:
                    res.append(s)
                return
            if opened: 
                plus_one(s + ')', opened - 1)
            plus_one(s + '(', opened + 1)
        plus_one('(', 1)
        return res