class Solution:
    # robot keeps going in on edirection until it hits the end of the row/column or an object and then turns right
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        state = cleaned = r = c = 0
        m, n = len(room), len(room[0])
        visited = set()
        room[0][0] = -1
        cleaned = 1 # cleaned starting tile 0,0

        while True:
            i, j = directions[state]
           
            if 0<=r+i<m and 0<=c+j<n and room[r+i][c+j] !=1:
                r, c = r+i, c+j
                if room[r][c] == 0:
                    cleaned += 1
                    room[r][c] = -1
            else:
                state = (state + 1) % 4 # change directions
            
            if (r, c, state) in visited:
                return cleaned
            visited.add((r, c, state))
