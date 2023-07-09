class Solution:
    #keep queue of size k, and keep index of max value in queue for that subaraay only
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

