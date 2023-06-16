class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n + 1)
        for start, length in enumerate(ranges):
            left, right = max(0, start - length), min(n, start+length)
            max_range[left] = max(max_range[left], right)
        
        start = end = step = 0
        while end < n:
            step+=1
            temp = end
            end = max(max_range[i] for i in range(start, end + 1))
            start = temp
            # or in one line below
            #  start, end = end, max(max_range[i] for i in range(start, end + 1))
            if start == end: return -1
        return step
        