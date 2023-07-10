class Solution:
    # prim's algo
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a, b, cost in connections:
            graph[a].append((cost, b))
            graph[b].append((cost, a))
        
        queue = ([(0, n)])
        visited = set()
        result = 0
        while queue:
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                result += cost
                for c, next_city in graph[city]:
                    heapq.heappush(queue, (c, next_city))
        return result if len(visited) == n else -1