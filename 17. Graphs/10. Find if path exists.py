class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        queue = deque([source])
        visited[source] = True

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return False