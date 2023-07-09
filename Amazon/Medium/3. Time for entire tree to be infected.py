# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = collections.defaultdict(list)
        queue = collections.deque([(root, None)])
        # build graph from tree with bfs, can also do DFS to build this
        while queue:
            node, parent = queue.popleft()
            if node and parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        bfs = collections.deque([(start, 0)])
        visited = set()
        # result = 0
        while bfs:
            node, time = bfs.popleft()
            # result = max(time, result) can do this too
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    bfs.append((neighbor, time+1))
        return time