# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # DFS
        if root is None:
            return 0
        return max(self.maxDepth(root.left) +1, self.maxDepth(root.right)+1)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int: # BFS
        if root is None:
            return 0
        
        depth =0
        queue = [root]
        
        while queue:
            nextlevel = []
            for node in queue:
                if node.left: nextlevel.append(node.left)
                if node.right: nextlevel.append(node.right)
            depth +=1
            queue = nextlevel
        return depth