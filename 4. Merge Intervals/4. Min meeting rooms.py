class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        min_rooms = []
        intervals.sort(key=lambda x: x[0]) # sort by start time of meetings
        heapq.heappush(min_rooms, intervals[0][1]) # insert end time into min heap

        for interval in intervals[1:]:
            if min_rooms[0] <= interval[0]: # if meetings ends before new meeting starts pop
                heapq.heappop(min_rooms)
            heapq.heappush(min_rooms, interval[1])
        
        return len(min_rooms)