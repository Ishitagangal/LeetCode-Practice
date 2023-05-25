class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        maxheap = []
        for n, f in frequency_map.items():
            heapq.heappush(maxheap, (-f, n))
        
        result = []
        while k:
            f, n = heapq.heappop(maxheap)
            result.append(n)
            k -=1
        
        return result