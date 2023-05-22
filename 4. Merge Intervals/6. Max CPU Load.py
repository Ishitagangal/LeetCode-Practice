# Given an array of jobs with different time requirements, where each job consists of start time, end time and CPU load. 
# The task is to find the maximum CPU load at any time if all jobs are running on the same machine.

class Job:
    def __init__(self, start, end, cpu):
        self.start = start
        self.end = end
        self.cpu_load = cpu

def max_cpu_time(self, jobs:List[Job]) -> int:
    jobs.sort(key=lambda x: x.start)
    min_heap = []
    max_load = current_load = 0

    for job in jobs:
        # remove all jobs that have ended from min heap
        while min_heap and min_heap[0].end <= job.start:
            current_load -= min_heap[0].cpu_load
            heappop(min_heap)
        
        #add current job to heap
        heapq.heappush(min_heap, job)
        current_load += job.cpu_load
        max_load = max(max_load, current_load)
    
    return max_load
