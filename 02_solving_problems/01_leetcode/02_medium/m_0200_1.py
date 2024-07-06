class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        res = 0

        def checker(h, w):
            if  0 > w or w >= width or 0 > h or h >= height: 
                return False
            if grid[h][w] == "1": 
                grid[h][w] = "0"
                checker(h, w - 1)
                checker(h, w + 1)
                checker(h - 1, w)
                checker(h + 1, w)
                return True
            else: 
                return False
        
        for id_h in range(height):
            for id_w in range(width):
                if checker(id_h, id_w): 
                    res += 1

        return res

# OK, 77%, 47%