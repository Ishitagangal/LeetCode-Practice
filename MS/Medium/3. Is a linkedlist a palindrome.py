# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        middle_node = self.middle_node(head)
        new_list = self.reverse_list(middle_node.next)
        
        flag = True
        copy_head = head
        copy_new_list = new_list
        while copy_new_list is not None:
            if copy_head.val == copy_new_list.val:
                copy_head = copy_head.next
                copy_new_list = copy_new_list.next
            else:
                flag = False
                break
        
        middle_node.next = self.reverse_list(new_list)
        return flag
    
    def middle_node(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
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
    