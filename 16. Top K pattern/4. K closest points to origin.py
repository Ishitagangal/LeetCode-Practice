class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            x, y = point[0], point[1]
            d = x**2 + y**2
            heapq.heappush(max_heap, (-d, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [point for _, point in max_heap]