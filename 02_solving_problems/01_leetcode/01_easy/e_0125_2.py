class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        if len(s) < 2: 
            return result
        left = 0
        right = len(s) - 1 

        while left < right:
            while not s[right].isalnum() and right > left:
                right -= 1
            while not s[left].isalnum() and left < right:
                left += 1
            if (not s[left].isalnum() or not s[left].isalnum() or s[left].lower() != s[right].lower()) and right != left:
                result = False 
                break
            left += 1
            right -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("0P"))


#OK 24%, 83%