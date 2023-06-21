class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <=1:
            return s
        
        char_frequency = collections.defaultdict(int)
        for char in s:
            char_frequency[char] +=1
        
        maxHeap =[]
        
        for char, freq in char_frequency.items():
            heapq.heappush(maxHeap,  (-freq, char))
        
        queue = collections.deque()
        result =[]
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            result.append(char)
            
            queue.append((char, freq + 1))
            
            if len(queue) == k:
                char, freq = queue.popleft()
                
                if -freq > 0:
                    heapq.heappush(maxHeap, (freq, char))
        
        return "".join(result) if len(result) == len(s) else ""
            
        