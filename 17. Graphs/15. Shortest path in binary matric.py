class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        directions = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1),(1, 0), (1, -1), (0, -1)]

        if grid[0][0] != 0 or grid[nr-1][nc-1] != 0:
            return -1
        
        queue = deque([(0,0)])
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (nr - 1, nc -1):
                return distance
            for i, j in directions:
                new_row = row + i
                new_col = col + j
                if not (0<=new_row<nr and 0<=new_col<nc):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                grid[new_row][new_col] = distance + 1
                queue.append((new_row, new_col))
        
        return -1