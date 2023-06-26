class HitCounter:
    # could also use a deque
    def __init__(self):
        self.counter = [[0, 0] for _ in range(300)] # store count, timestamp reqrite after 300seconds
        

    def hit(self, timestamp: int) -> None:
        index = int((timestamp - 1) % 300)
        if self.counter[index][1] == timestamp:
            self.counter[index][0] += 1
        else:
            self.counter[index][0] = 1
            self.counter[index][1] = timestamp

    def getHits(self, timestamp: int) -> int:
        count = 0
        for hit in self.counter:
            freq, time = hit[0], hit[1]
            if timestamp - time < 300:
                count += freq
        return count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp