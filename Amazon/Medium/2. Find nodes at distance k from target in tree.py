# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        queue = collections.deque([(root, None)])
        # build graph from tree with bfs, can also do DFS to build this
        while queue:
            node, parent = queue.popleft()
            if node and parent:
                graph[parent].append(node)
                graph[node].append(parent)
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        
        # start bfs from target node till k level reached, every node at k level is result
        bfs = deque([(target, 0)])
        visited = set([target])
        result = []
        while bfs:
            node, distance = bfs.popleft()
            if distance > k:
                continue
            if distance == k:
                result.append(node.val)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    bfs.append((neighbor, distance + 1))
                    visited.add(neighbor)
        return result

