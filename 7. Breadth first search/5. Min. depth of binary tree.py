# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(1, root)])

        while queue:
            depth, node = queue.popleft()
            child_nodes = [node.left, node.right]
            if not any(child_nodes):
                return depth
            for child in child_nodes:
                if child:
                    queue.append((depth+1, child))