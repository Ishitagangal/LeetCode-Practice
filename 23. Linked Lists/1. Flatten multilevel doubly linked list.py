"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return (None)
        self.travel(head)
        return (head)

    def travel(self, cur):
        while cur:
            next_node = cur.next # have to store next node in case cur.next gets overridden to point to child node. will use this to connect the child level back to current level
            if not next_node: tail = cur  # reached the last node in current level, assign it to 'tail' for return

            if cur.child: # if the current node contains a child node, this if clause will handle the child node's level and any more child nodes that it spawns
                cur.child.prev = cur
                cur.next = cur.child

                child_tail = self.travel(cur.child) #returns tail after traversing the child node's level
                if next_node:     # if there exists a node in the prior level, connect its prev pointer to the child node's tail. if there is none, then no need
                    next_node.prev = child_tail

                child_tail.next = next_node  # have to connect child_tail back to prior level regardless if next node is null or not
                cur.child = None  # clearing child pointers

            cur = cur.next  # this will either begin traversing cur's child node level (if exists) or resume traversing cur's current level

        return (tail)  # returns tail node of level  