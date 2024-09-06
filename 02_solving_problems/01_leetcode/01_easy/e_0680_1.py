class Solution:
    def validPalindrome(self, s: str) -> bool:
        def clear_check(s, skipped):
            left = 0
            right = len(s) - 1
            while left <= right:
                if s[left] != s[right]:
                    if skipped:
                        return False
                    else:
                        return clear_check(s[left:right], True) or clear_check(
                            s[left + 1 : right + 1], True
                        )
                left += 1
                right -= 1
            return True

        return clear_check(s, False)
