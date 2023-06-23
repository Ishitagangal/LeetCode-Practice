# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp = None
        carry = 0
        
        if l1 is None and l2 is not None:
            return l2
        elif l2 is None and l1 is not None:
            return l1
        
        while l1 is not None or l2 is not None:
            current_sum = carry
            if l1 is not None:
                current_sum += l1.val
                l1 = l1.next
            if l2 is not None:
                current_sum += l2.val
                l2 = l2.next
            
            node = ListNode(current_sum%10)
            carry = current_sum // 10
            
            if temp is None:
                temp = head = node
            else:
                temp.next = node
                temp = temp.next
        if carry>0:
            temp.next = ListNode(carry)
        return head