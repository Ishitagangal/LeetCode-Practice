class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        numOfProvinces = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                numOfProvinces += 1
                self.bfs(isConnected, i, visited)
        return numOfProvinces
    
    def bfs(self, isConnected, index, visited):
        queue = deque([index])
        visited[index] = True

        while queue:
            node = queue.popleft()
            for i in range(len(isConnected)):
                if isConnected[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
        

