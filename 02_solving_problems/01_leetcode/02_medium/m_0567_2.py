class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = right = 0 
        s1_dict = Counter(s1)
        wind_dict = {}
        ctr = 0

        while right < len(s2):
            if right - left == len(s1):
                if s2[left] in s1_dict:
                    wind_dict[s2[left]] -= 1
                    if not wind_dict[s2[left]]:
                        del wind_dict[s2[left]]
                    ctr -= 1
                left += 1
            if s2[right] in s1_dict:
                wind_dict[s2[right]] = wind_dict.get(s2[right], 0) + 1
                ctr += 1
            if ctr == len(s1) and wind_dict == s1_dict:
                return True  
            right += 1

        return False
