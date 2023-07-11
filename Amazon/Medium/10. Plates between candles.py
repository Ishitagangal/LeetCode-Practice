class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left_nearest_candle = [-1] * len(s)
        right_nearest_candle = [-1] * len(s)
        candle_count = []

        index = -1
        for i in range(len(s)):
            if s[i] == '|':
                index = i
            left_nearest_candle[i] = index
        index = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == '|':
                index = i
            right_nearest_candle[i] = index
        count = 0
        for char in s:
            if char == '|':
                count +=1
            candle_count.append(count)

        result = [0] * len(queries)

        for i, query in enumerate(queries):
            start, end = query[0], query[1]
            left, right = right_nearest_candle[start], left_nearest_candle[end]
            if left == -1 or right == -1:
                result[i] = 0
            elif left < right:
                result[i] = right - left + 1 - (candle_count[right] - candle_count[left] + 1)

        return result

             