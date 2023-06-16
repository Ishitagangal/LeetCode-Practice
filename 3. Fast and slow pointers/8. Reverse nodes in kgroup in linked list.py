# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head= ktail = None
        curr = head

        while curr:
            count = 0
            curr = head
            while count < k and curr is not None:
                curr = curr.next
                count+=1
            
            if count == k:
                reversed_head = self.reverseLinkedList(head, k)
                if not new_head:
                    new_head = reversed_head # set new head of new final linked list
                # point previous knodes reversed tail to new reversed head
                if ktail:
                    ktail.next = reversed_head # for subsequent k node reversals attachment
                
                ktail = head # since reversed list's tail is the old original head
                head = curr # where we stopped counting k nodes to restart new k node group
        if ktail:
            ktail.next = head # remaining less than k nodes in the list if any
        
        return new_head if new_head else head
    
    def reverseLinkedList(self, head:ListNode, k:int) ->ListNode:
        prev = None
        curr = head
        while k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -=1
        return prev
                
                