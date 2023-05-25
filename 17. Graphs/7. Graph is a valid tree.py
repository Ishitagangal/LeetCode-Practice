# graph is valid tree if len edges is exactly n - 1, and fully connected
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        seen = {0}
        queue = deque([0])
        
        while queue:
            index = queue.popleft()
            for neighbor in graph[index]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)
        return len(seen) == n