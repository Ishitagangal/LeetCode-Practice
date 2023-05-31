class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = [i for i in range(n)]
        heapify(available_rooms)

        min_heap = [] # to track rooms assigned
        result = [0] * n # keep track of num of meetings in ith room
        meetings.sort(key = lambda x: x[0])
        for start, end in meetings:
            while min_heap and min_heap[0][0] <= start:
                _, room = heapq.heappop(min_heap)
                heapq.heappush(available_rooms, room) # if a room is free, put it back in avail
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(min_heap, [end, room])
            else:
                time, room = heapq.heappop(min_heap)
                heapq.heappush(min_heap, [time + end - start, room]) # meetin gis delayed until a room is free
            result[room] += 1
        
        return result.index(max(result))
        


