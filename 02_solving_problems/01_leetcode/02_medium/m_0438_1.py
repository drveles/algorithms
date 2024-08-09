class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = Counter(p)
        window_dict = {}
        left = right = 0
        result = []

        while right < len(s):
            if right - left + 1 > len(p):
                window_dict[s[left]] -= 1
                if window_dict[s[left]] == 0:
                    del window_dict[s[left]]
                left += 1
            window_dict[s[right]] = window_dict.get(s[right], 0) + 1

            if window_dict == p_dict:
                result.append(left)

            right += 1

        return result

#OK, 50%, 50%
