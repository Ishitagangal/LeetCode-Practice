# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        queue = deque([root])
        level = 0
        levels = []
        while queue:
            levels.append([])
            for i in range(len(queue)):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level +=1
        return levels

        