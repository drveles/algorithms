# OK 27%, 98%

class Solution:
    def backtracking(self, s, ans, curr, temp=''):
        if curr == 4 and len(s) == 0:
            ans.append(temp[:-1])
            return
        if curr == 4 or len(s) == 0:
            return
        
        for i in range(3):
            if curr > 4 or i + 1 > len(s):
                break
            
            if int(s[:i+1]) > 255 or i != 0 and s[0] == '0':
                continue

            self.backtracking(s[i+1:], ans, curr + 1, temp+s[:i+1] + '.')


    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        curr = 0
        self.backtracking(s, ans, curr, '')
        return ans
