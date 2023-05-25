class MedianFinder:

    def __init__(self):
        self.max_heap = [] # for first half of nums that are smaller
        self.min_heap = [] # for the larger nums

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num) # add num to lower nums maxheap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap)) # to balance, remove largest num from the lower side and move it to other heap
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return float(-self.max_heap[0] + self.min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()