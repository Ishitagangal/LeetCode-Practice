class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        # or min_heap = nums, heapq.heapify(min_heap), then pop after size k
        for num in nums:
            if len(self.min_heap) < k:
                heapq.heappush(self.min_heap, num)
            else:
                if num > self.min_heap[0]:
                    heapq.heappop(self.min_heap)
                    heapq.heappush(self.min_heap, num)
        

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)