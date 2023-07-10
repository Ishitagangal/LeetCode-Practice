class Solution:
    # remove least frequent nums first 
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_freq = Counter(arr)
        min_heap = list(num_freq.values())
        heapq.heapify(min_heap)
        while k > 0:
            k -= heapq.heappop(min_heap)
        return len(min_heap) + 1 if k <0 else len(min_heap)

# O(n)
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        buckets = [[] for _ in range(len(arr) + 1)]
        counter = collections.Counter(arr)
        for key, freq in counter.items():
            buckets[freq].append(key)
        for freq in range(len(arr) + 1):
            if k == 0: break
            while buckets[freq] and k >= freq:
                del counter[buckets[freq].pop()]
                k -= freq
        return len(counter)