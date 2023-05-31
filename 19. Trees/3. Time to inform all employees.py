class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        child_nodes = defaultdict(list)
        for i, m in enumerate(manager):
            if m >= 0:
                child_nodes[m].append(i)
        self.result = 0
        def dfs(node, time):
            self.result = max(self.result, time)
            for child in child_nodes[node]:
                dfs(child, time + informTime[node])
            #  max(dfs(i) for i in child_nodes[node] or [0]) + informTime[i]
        dfs(headID, 0)
        return self.result
    

    def numOfMinutesBFS(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = collections.deque([(headID, 0)])
        subordinates = collections.defaultdict(list)
        res = 0
        for i, v in enumerate(manager):
            subordinates[v].append(i)
            
        while q:
            u, time = q.popleft()
            res = max(res, time)
            for v in subordinates[u]:
                q.append((v, time + informTime[u]))
        return res