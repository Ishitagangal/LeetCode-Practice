# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def max_path_sum(root):
            if not root:
                return 0
            nonlocal max_sum
            left_sum = max(max_path_sum(root.left), 0)
            right_sum = max(max_path_sum(root.right), 0)

            new_path = root.val + left_sum + right_sum
            max_sum = max(max_sum, new_path)

            return max(left_sum, right_sum) + root.val
        max_path_sum(root)
        return max_sum