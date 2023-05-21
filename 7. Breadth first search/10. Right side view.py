# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        rightside = []

        while queue:
            num_nodes = len(queue)
            for i in range(num_nodes):
                node = queue.popleft()
                if i == num_nodes - 1:
                    rightside.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return rightside
            