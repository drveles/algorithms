class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row, col):
            if -1 < row < len(grid) and -1 < col < len(grid[0]) and grid[row][col] == "1":
                grid[row][col] = "0"
                bfs(row - 1, col)
                bfs(row + 1, col)
                bfs(row, col - 1)
                bfs(row, col + 1)
        
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    result += 1
                    bfs(row, col)
        
        return result
