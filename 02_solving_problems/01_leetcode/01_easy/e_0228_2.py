class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        coords = [] 

        for num in nums: 
            if coords and coords[-1][1] == num - 1:
                coords[-1][1] = num
            else:
                coords.append([num, num])

        return [f"{x}" if x == y else f"{x}->{y}" for x,y in coords]
    
#OK, 68% , 45%