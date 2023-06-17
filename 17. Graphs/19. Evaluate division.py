class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value  # a/b = value, given
            graph[b][a] = 1/value  # b/a = 1/(a/b) = 1/value
            
        result = []
        
        for a, b in queries:
            queue = deque()  # for BFS traversion
            seen = set()  # all visited expressions
            curr = -1  # the current result
            if a in graph:
                queue.append((a, 1))
                seen.add(a)
            while queue:
                i, value = queue.popleft()
                if i == b:
                    curr = value  # the resultant value of a/b
                    break
                for adj, adj_value in graph[i].items():
                    if adj not in seen:
                        queue.append((adj, value*adj_value))  # a/adj = (a/i) * (i/adj) = value*adj_value
                        seen.add(adj)
            result.append(curr)
        return result