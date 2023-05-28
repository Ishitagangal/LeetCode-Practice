class Solution:
    # with heap, at most 256 characters would mean heapify takes O(n)
    def frequencySort(self, s:str) -> str:
        freq_map = Counter(s) # val:freq
        max_heap = []
        max_heap = [(-freq, val) for val, freq in freq_map.items()]
        heapq.heapify(max_heap)
        string = []
        while max_heap:
            freq, val = heapq.heappop(max_heap)
            string.append(val * -freq)
        return "".join(string)

    # sorting, hashmap O nlogn due to sorting
    def frequencySort2(self, s: str) -> str:
        freq_map = Counter(s) # val:freq
        freq_list = list(zip(freq_map.keys(), freq_map.values()))
        freq_list.sort(key= lambda x:x[1], reverse=True)

        string = []
        for letter, freq in freq_list:
            string.append(letter*freq)
        return "".join(string)
    