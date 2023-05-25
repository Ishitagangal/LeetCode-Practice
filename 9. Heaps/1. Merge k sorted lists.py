# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Wrapper():
            def __init__(self, val):
                self.val = val
            def __lt__(self, other):
                return self.val < other.val
    
        min_heap = []
        for list in lists:
            if list:
                heapq.heappush(min_heap, (Wrapper(list.val), list))
        
        head = cur = ListNode(0)
        while min_heap:
            obj, node = heapq.heappop(min_heap)
            cur.next = ListNode(obj.val)
            cur = cur.next
            if node.next:
                heappush(min_heap, (Wrapper(node.next.val), node.next))
        
        return head.next