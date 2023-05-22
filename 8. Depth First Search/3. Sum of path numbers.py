# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(node, currNum):
            nonlocal root_to_leaf
            if node:
                currNum = currNum*10 + node.val
                if not node.left and not node.right:
                    root_to_leaf += currNum
                preorder(node.left, currNum)
                preorder(node.right, currNum)
        
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
    # morris traversal TBD?????