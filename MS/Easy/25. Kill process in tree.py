class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        for i, parent in enumerate(ppid):
            tree[parent].append(pid[i])
        
        queue = deque()
        queue.append(kill)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for children in tree[node]:
                queue.append(children)
        return result
        