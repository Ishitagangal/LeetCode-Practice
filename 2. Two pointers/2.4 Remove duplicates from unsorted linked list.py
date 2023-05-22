# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
    
    
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dict_t = collections.defaultdict(int)
        curr = head
        while (curr):
            dict_t[curr.val] += 1
            curr = curr.next
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while head:
            if dict_t[head.val] > 1:
                prev.next = head.next
            else:
                prev = prev.next          
            head = head.next
        return dummy.next