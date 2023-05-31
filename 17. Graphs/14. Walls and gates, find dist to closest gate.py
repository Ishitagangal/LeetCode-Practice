
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        rows = len(rooms)
        cols = len(rooms[0])
        
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0: # start searching from gate, update distance from gate during bfs below
                    q.append((i,j))
        
        while q:
            row, col = q.popleft()
            dist = rooms[row][col] + 1
            for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
                new_row = row + i
                new_col = col + j
                if 0 <= new_row < rows and 0 <= new_col < cols and rooms[new_row][new_col] == 2147483647: # inf here is 2^31 mean empty room
                    rooms[new_row][new_col] = dist
                    q.append((new_row,new_col))