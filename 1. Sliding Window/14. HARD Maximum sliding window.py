# https://leetcode.com/problems/sliding-window-maximum/editorial/
# keep highest elements for a window in queue of size k
# monotonically increasing
# storing indexes in the queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0: return nums

        result = []
        queue = deque()
        for i in range(n):
            if queue and queue[0] < i - k + 1: # move window ahead
                queue.popleft()
            while(queue and nums[queue[-1]] < nums[i]):
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result
