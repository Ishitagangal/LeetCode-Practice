# maze 1 , find if can reach destination on stopping
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque([(start[0], start[1])])
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        while queue:
            row, col = queue.popleft()
            visited.add((row, col))
            if row == destination[0] and col == destination[1]:
                return True
            
            for i, j in directions:
                new_row = row + i
                new_col = col + j
                # keep rolling the ball until it hits a wall
                while 0<=new_row<len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != 1:
                    new_row += i
                    new_col += j
                # loop exits when new row and new col are a wall, so go back by negating it below
                new_row -= i
                new_col -= j
                if (new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
        
        return False

# maze 2 find the minimum distance to reach destination on stopping
class Solution:
    # use heapq to sort on distance and do Djikstra's instead of just BFS
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        queue = [(0, start[0], start[1])]
        visited = {(start[0], start[1]):0}
        while queue:
            dist, x, y = heapq.heappop(queue)
            if [x, y] == destination:
                return dist
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = x + i, y + j
                d = 1
                while 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] != 1:
                    new_row += i
                    new_col += j
                    d += 1
                new_row -=i
                new_col -=j
                d -=1
                if (new_row, new_col) not in visited or dist + d < visited[(new_row, new_col)]:
                    visited[(new_row, new_col)] = dist + d
                    heapq.heappush(queue, (dist + d, new_row, new_col))
        return -1

    # BFS< TLE use Djikstra's instead with a min heap on distance
    def shortestDistanceBFS(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze or not maze[0] or start == destination:
            return 0
        queue = deque([(start[0], start[1], 0)])
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        # visited = {(start[0], start[1]): 0}
        visited = defaultdict(int)
        visited[(start[0], start[1])] = 0

        while queue:
            row, col, distance = queue.popleft()
            
            for i, j in directions:
                new_row = row + i
                new_col = col + j
                d =0
                # keep rolling the ball until it hits a wall
                while 0<=new_row<len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
                    new_row += i
                    new_col += j
                    d += 1
                new_row -=i
                new_col -=j
                d -=1
                if (new_row, new_col) not in visited or ((new_row, new_col) in visited and visited[(new_row,new_col)]) > distance + d:

                    visited[(new_row, new_col)] = distance + d
                    if (new_row,new_col) != (destination[0], destination[1]):
                        queue.append((new_row, new_col, distance + d))
        
        return visited.get((destination[0], destination[1]), -1)