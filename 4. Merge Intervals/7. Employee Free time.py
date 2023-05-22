"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # O(nlogk) with heap use
        min_heap = []
        # for every employee, push first interval into heap
        for i, employee in enumerate(schedule):
            heapq.heappush(min_heap, (employee[0].start, i, 0))
            # interval start,emp id, event index # heapified on start time
        
        free_time = []
        _, i, j = min_heap[0]
        prev_end = schedule[i][j].end
        while min_heap:
            _, i, j = heapq.heappop(min_heap)
            if j+1 < len(schedule[i]): #more interval for this employee exist, push next interval into heap
                heapq.heappush(min_heap, (schedule[i][j+1].start, i, j+1))
            current_event = schedule[i][j]
            if current_event.start > prev_end: # the gap is between old event end and current event start
                free_time.append(Interval(start=prev_end, end=current_event.start))
            prev_end = max(current_event.end, prev_end)
        return free_time

    def employeeFreeTimeMergedIntervals(self, schedule: '[[Interval]]') -> '[Interval]':
        # O(nlogn) with sorting
        # merge intervals first, then go through resul to find gaps
        intervals = []
        #flatten
        for i in schedule:
            [intervals.append(x) for x in i]
        
        intervals.sort(key=lambda x: x.start)
        merged = []
        for i in intervals:
            if not merged or merged[-1].end < i.start:
                merged.append(i)
            else:
                merged[-1].end = max(i.end, merged[-1].end)
        
        free_time = []
        for i in range(1, len(merged)):
            free_interval = Interval(start=merged[i-1].end, end=merged[i].start)
            free_time.append(free_interval)
        return free_time
    