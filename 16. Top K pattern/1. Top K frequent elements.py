class Solution:
    #min heap O(nlogk)
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

    # max heap, O nlogn
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencymap = {}
        
        for num in nums:
            frequencymap[num] = frequencymap.get(num, 0) + 1
        
        maxheap = []
        for n, f in frequencymap.items():
            heapq.heappush(maxheap, (-f, n))
        
        result = []
        while k:
            f, n = heapq.heappop(maxheap)
            result.append(n)
            k -=1
        
        return result