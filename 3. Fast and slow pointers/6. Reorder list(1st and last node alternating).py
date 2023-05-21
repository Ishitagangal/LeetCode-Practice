# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid_node = self.middle_node(head)
        second_list_head = self.reverse_list(mid_node)

        first, second = head, second_list_head
        while second.next:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp

    
    def middle_node(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list(self, head):
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev