class Solution:
    def rand10(self):        
        return (rand7() + rand7() + rand7() + rand7() + rand7()) % 10 + 1

# OK, 15%, 68%