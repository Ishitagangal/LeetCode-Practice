# number of distinct islands that can't be translated to each other
# so find relative position of each island from its initial start point call it origin 
# save it in a frozenset or tuple in a set
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def bfs(row_origin, col_origin):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            queue = deque([(row_origin, col_origin)])
            while queue:
                row, col = queue.popleft()
                current_island.add((row - row_origin, col-col_origin))
                visited.add((row, col))
                for dir in directions:
                    new_row, new_col = row + dir[0], col +dir[1]
                    if not(0<=new_row<len(grid) and 0<=new_col<len(grid[0])):
                        continue
                    if grid[new_row][new_col] !=1 or (new_row, new_col) in visited:
                        continue
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 0
        
        unique_islands = set()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = set()
                if grid[row][col] == 1 and (row, col) not in visited:
                    bfs(row, col)
                    if current_island:
                        unique_islands.add(frozenset(current_island)) # can also use tuple(current_island)
        return len(unique_islands)
