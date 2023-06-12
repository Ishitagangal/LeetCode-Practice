class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencymap = {}
        
        for num in nums:
            frequencymap[num] = frequencymap.get(num, 0) + 1
        
        min_heap = []
        for n, f in frequencymap.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (f, n))
            else:
                if f > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (f, n))
        
        return [x for _, x in min_heap]