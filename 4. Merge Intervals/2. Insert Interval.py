class Solution:
    # O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        result.append(newInterval)
        return result

    # O(log n)
    https://leetcode.com/problems/insert-interval/solutions/3173774/efficient-interval-insertion-a-binary-search-solution-with-o-log-n-time-complexity/
