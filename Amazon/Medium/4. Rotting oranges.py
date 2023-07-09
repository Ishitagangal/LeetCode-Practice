class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque() # row, col, time
        fresh_oranges = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh_oranges +=1
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        time = 0
        while queue:
            row, col, time = queue.popleft()
            visited.add((row, col))
            for dir in directions:
                new_row, new_col = row+dir[0], col+dir[1]
                if not(0<=new_row<len(grid) and 0<=new_col<len(grid[0])):
                    continue
                if (new_row, new_col) in visited:
                    continue
                if grid[new_row][new_col] == 1:
                    visited.add((new_row,new_col))
                    queue.append((new_row, new_col, time+1))
                    fresh_oranges -=1
        return time if fresh_oranges == 0 else -1