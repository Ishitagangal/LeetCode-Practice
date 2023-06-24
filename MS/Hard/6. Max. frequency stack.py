class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.map_freqs = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]
        self.map_freqs[self.freq[val]].append(val)
        

    def pop(self) -> int:
        val = self.map_freqs[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.map_freqs[self.max_freq]:
            self.max_freq -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()