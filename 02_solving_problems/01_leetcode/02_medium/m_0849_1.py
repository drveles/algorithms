class Solution:
    def maxDistToClosest(self, seats) -> int:
        longest_space = curr_space = space_ctr = 0
        for seat in seats: 
            if seat: 
                longest_space = max(longest_space, curr_space)
                curr_space = 0
                space_ctr +=1
            else:
                curr_space += 1
        if space_ctr == 1:
            return max(longest_space, curr_space) 
        return longest_space // 2 + longest_space % 2 
    
if __name__ == "__main__":
    print(Solution().maxDistToClosest([1,1,1,1,1,1,1,0]))


# WA