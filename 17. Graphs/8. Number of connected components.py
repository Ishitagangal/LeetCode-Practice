class Solution:
    def countComponents(self, n: int, edges: List[List[str]]) -> int:
        # visited = [ [ False for j in range(len(edges[i])) ] for i in range(len(edges)) ]
        
        count = 0
        graph = defaultdict(list)
        seen =  [False for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            for neighbor in graph[node]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    dfs(neighbor)
                    
        for i in range(n):
            if not seen[i]:
                count+=1
                seen[i] = True
                dfs(i)
        
       
                    
        return count