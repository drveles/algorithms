class Solution:
    def isValid(self, s: str) -> bool:
        pairs_dct = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            if c in pairs_dct:
                stack.append(c)
            else:
                if not stack or pairs_dct[stack.pop()] != c:
                    return False

        return False if stack else True

# OK, 87%, 22%