class Solution:
    def isValid(self, s: str) -> bool:
        ctr = 0

        for c in s:
            if c == "(":
                ctr += 1
            elif c == ")":
                ctr -= 1
                if ctr < 0: 
                    return False

        return not ctr

    def removeInvalidParentheses(self, s: str) -> List[str]:
        if self.isValid(s):
            return [s]

        all_variants, result = {s, }, set()

        while not result:
            curr_variants = set()
            for temp_s in all_variants:
                for idx in range(len(temp_s)):
                    if temp_s[idx] not in "()": continue
                    temp_variant = temp_s[:idx] + temp_s[idx + 1:]
                    curr_variants.add(temp_variant)
                    if self.isValid(temp_variant):
                        result.add(temp_variant)
            all_variants = curr_variants

        return result
