class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connected = set()
        in_degrees = [0]*n
        for road in roads:
            in_degrees[road[0]] +=1
            in_degrees[road[1]] +=1
            connected.add((road[0], road[1]))
            connected.add((road[1], road[0]))
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                current = in_degrees[i] + in_degrees[j] - (1 if (i,j) in connected else 0)
                result = max(result, current)
        return result