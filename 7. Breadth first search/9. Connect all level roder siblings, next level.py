class Node:
    def __init__(self, val):
        self.val = val
        self.next = self. left = self.right = None


def populate_sibling_pointers(root):
    if not root:
        return
    
    head = root
    last_node = root

    while head != None:
        if head.left:
            last.next = head.left
            last = head.left
        if head.right:
            last.next = head.right
            last = head.right
        last.next = None
        head = head.next
    
