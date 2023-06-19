class Solution:
    # O(N log N)
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        stations.append((target, float('inf')))
        tank = startFuel
        result = prev = 0
        for location, capacity in stations:
            tank -= location - prev # account for prev as refueling location
            # if we keep going ahead and tank becomes less than 0, we should have refuled in the past
            # pretend we did and continue
            while max_heap and tank < 0:
                tank += (-heapq.heappop(max_heap))
                result += 1
            # now tank has positive fuel in it again or no more station left
            if tank < 0:
                return -1
            heapq.heappush(max_heap, -capacity)
            prev = location # location we refuled
        return result 