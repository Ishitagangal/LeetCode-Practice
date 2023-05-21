"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:

    def connect(self, root:'Optional[Node]')-> 'Optional[Node]':
        if not root:
            return root
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right 
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            leftmost = leftmost.left
        return root
    
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if not root:
#             return None
        
#         queue = collections.deque([root])
#         current = None
#         while queue:
#             size = len(queue)
            
#             for i in range(size):
#                 current = queue.popleft()
#                 if i < size - 1:
#                     current.next = queue[0]

#                 if current.left:
#                     queue.append(current.left)
#                 if current.right:
#                     queue.append(current.right)
#                 prev = current
#             print([node.val for node in queue])
            
#         return root
    