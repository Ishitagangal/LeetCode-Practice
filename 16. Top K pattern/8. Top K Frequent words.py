# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         word_freq = collections.Counter(words)
#         heap = []
#         for word, freq in word_freq.items():
#             heapq.heappush(heap, (freq, word))
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         return [heapq.heappop(heap)[1] for _ in range(k)]
    
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution(object):
    def topKFrequent(self, words, k):
        counts = collections.Counter(words)   
        
        freqs = []
        # heapq.heapify(freqs)
        for word, count in counts.items():
            heapq.heappush(freqs, (Element(count, word), word))
            if len(freqs) > k:
                heapq.heappop(freqs)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]