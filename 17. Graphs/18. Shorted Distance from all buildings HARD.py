# prune if the new bfs doesn't visit as many buildings as we previously
# visited. cause thats not going to be a good contender anyway.
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        visited = [[[0,0] for i in range(len(grid[0]))] for j in range(len(grid))]

        buildings = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # start from buildings
                    self.bfs(i, j, grid, visited, buildings)
                    buildings += 1
        
        result = float('inf')
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if visited[i][j][1] == buildings:
                    result = min(result, visited[i][j][0])
        
        return result if result!=float('inf') else -1
    
    def bfs(self, row, col, grid, visited, buildings):
        queue = deque([(row, col, 0)]) # row, col, steps
        while queue:
            r, c, step = queue.popleft()
            for dir in [(1, 0), (0,1), (-1, 0), (0, -1)]:
                new_row = r + dir[0]
                new_col = c + dir[1]
                if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and visited[new_row][new_col][1]==buildings and grid[new_row][new_col] == 0:
                    visited[new_row][new_col][0] += step + 1
                    visited[new_row][new_col][1] = buildings + 1 # 1 for this current building's bfs
                    queue.append((new_row, new_col, step+1))