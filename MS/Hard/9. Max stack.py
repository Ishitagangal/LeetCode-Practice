class MaxStack:

    def __init__(self):
        self.max_heap = []
        self.index = 0
        self.stack = []
        self.removed = set() # for lazy update, so if we remove from either heap or stack, we can update theother data structure later on
        
    def push(self, x: int) -> None:
        heapq.heappush(self.max_heap, (-x, -self.index))
        self.stack.append((x, self.index))
        self.index += 1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop() # pop out old removed elements if they are still in stack
        num, index = self.stack.pop()
        self.removed.add(index)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.max_heap and -self.max_heap[0][1] in self.removed:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        while self.max_heap and -self.max_heap[0][1] in self.removed:
            heapq.heappop(self.max_heap)
        num, index = heapq.heappop(self.max_heap)
        self.removed.add(-index)
        return -num


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()