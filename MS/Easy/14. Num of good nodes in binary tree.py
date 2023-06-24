# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS
    def goodNodesDFS(self, root) -> int:
        def dfs(node, max_so_far):
            nonlocal num_good_nodes
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.right:
                dfs(node.right, max(node.val, max_so_far))
            if node.left:
                dfs(node.left, max(node.val, max_so_far))
        
        num_good_nodes = 0
        dfs(root, float("-inf"))
        return num_good_nodes

    # BFS
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        queue = deque([(root, float('-inf'))])
        while queue:
            node, max_so_far = queue.popleft()
            if max_so_far <= node.val:
                result += 1
            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))
            if node.left:
                queue.append((node.left, max(node.val, max_so_far)))
        return result