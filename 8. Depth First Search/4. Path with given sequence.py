# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        if not root:
            return False
        return self.isValidHelper(root, arr, len(arr), index=0)
    
    def isValidHelper(self, root, arr, n, index):
        if not root or index == n:
            return False
        
        # leaf node
        if not root.left and not root.right:
            if index == n-1 and arr[index] == root.val:
                return True
            return False
        
        return index < n and arr[index] == root.val and (self.isValidHelper(root.left, arr, n, index + 1) or self.isValidHelper(root.right, arr, n, index+1))