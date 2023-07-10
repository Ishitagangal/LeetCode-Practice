class Solution:
    def reorganizeString(self, s: str) -> str:
        result, c = [], Counter(s)
        max_heap = [(-value, key) for key, value in c.items()]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            freq1, char1 = heapq.heappop(max_heap)
            result.append(char1)
            freq2, char2 = heapq.heappop(max_heap)
            result.append(char2)

            if abs(freq1) > 1:
                heapq.heappush(max_heap, (freq1+1, char1))
            if abs(freq2) > 1:
                heapq.heappush(max_heap, (freq2+1, char2))
        
        if max_heap:
            freq, char = max_heap[0]
            if abs(freq) > 1:
                return "" # not possible to construct since repeating same character not allowed
            else:
                result.append(char)
        
        return "".join(result)