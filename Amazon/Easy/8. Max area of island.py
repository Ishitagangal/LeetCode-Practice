class Solution:
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def __init__(self):
        self.max = 0 
    
    def maxAreaOfIsland(self, grid):
        if not grid or not grid[0]:
            return
        nr = len(grid)
        nc = len(grid[0])
        
        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
                    
        return self.max
    
    def bfs(self, grid, r, c):
        area = 0
        queue = deque()
        queue.append((r, c))
        grid[r][c] = 0
        while queue:
            area +=1
            row, col = queue.popleft()
            for i, j in [(0,1), (1,0), (-1, 0), (0, -1)]:
                new_row, new_col = row+i, col+j
                if new_row < 0 or new_col <0 or new_row>=len(grid) or new_col >= len(grid[0]):
                    continue
                elif grid[new_row][new_col] != 1:
                    continue
                else:
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 0
        self.max = max(self.max, area)
        print(self.max)