class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        target = rows-1, cols-1
        
        if k >= rows + cols - 2:
            return rows + cols - 2
        
        state = 0, 0, k  # row, col, quota
        queue = collections.deque([(state, 0)]) # state, steps
        visited = set([state])
        
        while queue:
            (r, c, k), step = queue.popleft()
            
            if (r, c) == target:
                return step
            
            for i, j in [(1,0), (0,1), (-1,0), (0, -1)]:
                new_row, new_col = r+i, c+j

                if (0 <= new_row < rows) and (0 <= new_col < cols):
                    remaining_quota = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, remaining_quota)

                    if remaining_quota >=0 and new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, step+1))
        return -1