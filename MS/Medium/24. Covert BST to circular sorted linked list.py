"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        head, prev =  None, None

        def inorder(node: 'Node'):
            nonlocal prev, head
            if node.left:
                inorder(node.left)
            if prev:
                node.left = prev
                prev.right = node
            if not head:
                head = node # first node of the linked list
            
            prev = node
            if node.right:
                inorder(node.right)
        
        inorder(root)
        prev.right = head
        head.left = prev
        return head