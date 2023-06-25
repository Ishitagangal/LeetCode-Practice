"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # if successor is below the node
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # if successor is above the node in the tree, look in parent
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent