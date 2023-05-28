class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        m, n = len(image), len(image[0])
        if old_color != color:
            queue = deque([(sr, sc)])
            while queue:
                i, j = queue.popleft()
                image[i][j] = color
                for x, y in [(1,0), (-1,0), (0, -1), (0, 1)]:
                    new_i, new_j = x+i, y+j
                    if 0<=new_i<m and 0<=new_j<n and image[new_i][new_j] == old_color:
                        queue.append((new_i,new_j))
        return image