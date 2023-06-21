class Solution:
    # djikstra's usin gmin heap
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_dict = collections.defaultdict(dict)
        for source, dest, price in flights:
            flight_dict[source][dest] = price
        min_heap = [(0, src, k+1)]
        while min_heap:
            price, stop, k = heapq.heappop(min_heap)
            if stop == dst:
                return price
            if k > 0:
                for next_flight in flight_dict[stop]:
                    heapq.heappush(min_heap, (price + flight_dict[stop][next_flight], next_flight, k -1))
        return -1

## Bellman Ford

    def findCheapestPriceBellmanFord(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        costs = [float("inf")] * n

        costs[src] = 0
        for i in range(k + 1):
            temp = costs.copy()
            for start, end, price in flights:
                if costs[start] != float("inf"):
                    temp[end] = min(costs[start] + price, temp[end])
            costs = temp
        return costs[dst] if costs[dst] != float("inf") else -1