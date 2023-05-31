class TimeMap:

    def __init__(self):
        self.key_time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_time_map:
            self.key_time_map[key] = []
        self.key_time_map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_time_map:
            return ""
        if timestamp < self.key_time_map[key][0][0]: #smaller than first key timestampe
            return ""
        
        #binary search to find it
        left = 0
        right = len(self.key_time_map[key])

        while left < right:
            mid = left + (right-left)//2
            if self.key_time_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return "" if right == 0 else self.key_time_map[key][right - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)