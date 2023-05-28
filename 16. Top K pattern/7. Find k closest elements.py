class Solution:
    # start searching for the left bound of these k nums
    # check mid and mid + k index as only one can bein the final answer
    # binary search
    # O (log (n-k)) for binary search and O(k) to return final output
    def findClosestElementsBinary(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k # largest possible left bound

        while left < right:
            mid = left + (right - left)//2
            if x-arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left+k]


    # Max heap
    # O (nlogk)
    def findClosestElementsMaxHeap(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if len(arr) < k:
            return []
        
        heap = []
        
        #Implement Max Heap by inserting negative distance values
        for i in range(len(arr)):
            d = -abs(x-arr[i])            
            if len(heap) < k:             
                heapq.heappush(heap,(d,arr[i]))
            else:
                if -d < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(d,arr[i]))
        
        out = sorted([i[1] for i in heap])
               
        return out
    