class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key= lambda x:x[0])
        total_days = max(end for _, end in events)
        i = 0
        min_heap = []
        result = 0
        for day in range(1, total_days + 1):
            # add all events that start today
            while i < len(events) and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1]) # push end date 
                i +=1

            # remove all events that ended before today
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                result += 1
        return result
