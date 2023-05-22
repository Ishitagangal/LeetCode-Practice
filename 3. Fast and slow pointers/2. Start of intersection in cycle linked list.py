# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def find_intersection(self, head) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return fast
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        intersection_node = self.find_intersection(head)
        if not intersection_node:
            return None

        p1 = head
        p2 = intersection_node
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1 #start of cycle