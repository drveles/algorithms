class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        result = s + 'invalid'
        left = right = curr_ctr = 0
        t_dict = Counter(t)
        window = Counter()

        while right < len(s):
            rchar = s[right]
            if rchar in t_dict:
                window[rchar] = window.get(rchar, 0) + 1
                if window[rchar] == t_dict[rchar]:
                    curr_ctr += 1

            while curr_ctr == len(t_dict):
                lchar = s[left]
                result = result if len(result) < right - left + 1 else s[left:right + 1]
                if lchar in window:
                    window[lchar] -= 1
                    if window[lchar] < t_dict[lchar]:
                        curr_ctr -= 1
                left += 1
            right += 1

        return result if len(result) <= len(s) else ''
