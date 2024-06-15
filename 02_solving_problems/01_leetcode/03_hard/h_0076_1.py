class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        count_temp = {}
        have, need = 0, len(count_t)
        result = ""
        left = 0

        for right in range(len(s)):
            char = s[right]
            if char in count_t:
                count_temp[char] = count_temp.get(char, 0) + 1
                if count_temp[char] == count_t[char]:
                    have += 1

            while have == need:
                if not result or right - left + 1 < len(result):
                    result = s[left : right + 1]

                char = s[left]
                if char in count_t:
                    count_temp[char] -= 1
                    if count_temp[char] < count_t[char]:
                        have -= 1
                left += 1

        return result


# OK
