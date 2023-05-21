# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        levels = []
        level = 0
        while queue:
            levels.append(deque([]))
            for i in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 0:
                    levels[level].append(node.val)
                else:
                    levels[level].appendleft(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1
        return levels