# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-1)
        new_head.next = head

        prev_node = new_head 
        while head and head.next:
            first_node = head
            second_node = head.next

            # swap
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node # new second node
            head = first_node.next
        return new_head.next
