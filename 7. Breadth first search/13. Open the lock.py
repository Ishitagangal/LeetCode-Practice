class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1,1):
                    y = (x+d) % 10
                    yield node[:i] + str(y) + node[i+1:] ## yeild new numbers, 8 total?
        
        deadend = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        
        while queue:
            node, level = queue.popleft()
            if node == target:
                return level
            if node in deadend:
                continue
            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, level+1))
        
        return -1