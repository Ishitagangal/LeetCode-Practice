class Solution:
    def __init__(self):
        self.num_rows = 0
        self.num_cols = 0
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        self.num_rows, self.num_cols = len(heights), len(heights[0])
        
        pacific = deque()
        atlantic = deque()
        
        for i in range(self.num_rows):
            pacific.append((i,0))
            atlantic.append((i, self.num_cols -1))
        for i in range(self.num_cols):
            pacific.append((0, i))
            atlantic.append((self.num_rows -1, i))
        
        reachable_pacific = self.bfs(pacific, heights)
        reachable_atlantic = self.bfs(atlantic, heights)
        
        return list(reachable_pacific.intersection(reachable_atlantic))
    
    
    def bfs(self, queue: deque, heights):
        visited = set()
        
        while queue:
            row, col = queue.popleft()
            visited.add((row, col))
            
            for i, j in [(1,0), (0,1), (-1, 0), (0, -1)]:
                new_row, new_col = row + i, col + j
                
                if new_row<0 or new_row>=self.num_rows or new_col<0 or new_col>=self.num_cols:
                    continue
                
                if (new_row, new_col) in visited:
                    continue
                
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                queue.append((new_row, new_col))
        print(visited)
        return visited
            