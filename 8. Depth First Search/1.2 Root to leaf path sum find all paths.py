# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.allPaths(root, targetSum, [], result)
        return result
    
    def allPaths(self, root, target, currentPath, result):
        if not root:
            return 
        target -= root.val
        # currentPath.append(root.val) if you do this then also pop from currentpath after left and right subtree calls
        if not root.left and not root.right:
            if target == 0:
                result.append(currentPath+[root.val])
        return self.allPaths(root.left, target, currentPath+[root.val], result) or self.allPaths(root.right, target, currentPath+[root.val], result)