class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return
        nr = len(grid)
        nc = len(grid[0])
        
        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count+=1
        return count
    
    def bfs(self, grid, r, c):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '0'
        while queue:
            row, col = queue.popleft()
            for i, j in [(0,1), (1,0), (-1, 0), (0, -1)]:
                new_row, new_col = row+i, col+j
                if new_row < 0 or new_col <0 or new_row>=len(grid) or new_col >= len(grid[0]):
                    continue
                elif grid[new_row][new_col] != '1':
                    continue
                else:
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = '0'

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count +=1
        return count
    
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    