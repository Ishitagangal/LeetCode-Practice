class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        nr, nc = len(grid), len(grid[0])

        queue = deque()

        for row in range(nr):
            for col in range(nc):
                if grid[row][col] == "*":
                    queue.append((row, col, 0))
                    break

        while queue:
            row, col, steps = queue.popleft()

            for i, j in [(-1,0), (0, -1), (1, 0), (0,1)]:
                new_row = row + i
                new_col = col + j

                if 0 <= new_row < nr and 0 <= new_col < nc and grid[new_row][new_col] in ("#", "O"):
                    if grid[new_row][new_col] == '#':
                        return steps + 1 # food found
                    
                    grid[new_row][new_col] = '!'
                    queue.append((new_row, new_col, steps + 1))
        
        return -1
