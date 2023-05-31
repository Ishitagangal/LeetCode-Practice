# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def find_root_to_node(node, val, path) -> bool: # 1. find path from root
            if node.val == val:
                return True
            if node.left and find_root_to_node(node.left, val, path):
                path += "L"
            elif node.right and find_root_to_node(node.right, val, path):
                path += 'R'
            return path # true if path is not empty
        
        start, dest = [], []
        find_root_to_node(root, startValue, start)
        find_root_to_node(root, destValue, dest)
        print(start)
        print(dest)
        while len(start) and len(dest) and start[-1] == dest[-1]:
            start.pop()
            dest.pop()
        
        return "".join("U" * len(start)) + "".join(reversed(dest))