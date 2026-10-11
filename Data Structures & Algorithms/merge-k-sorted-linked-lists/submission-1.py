import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for idx, head in enumerate(lists):
            if head:
                arr.append((head.val, idx))
                head = head.next
                lists[idx] = head
        heapq.heapify(arr)
        
        dummy = ListNode()
        sorted_node = dummy
        while arr:
            val, lidx = heapq.heappop(arr)
            node = ListNode(val)
            sorted_node.next = node
            sorted_node = sorted_node.next
            # get next
            lhead = lists[lidx]
            if lhead:
                heapq.heapush((lhead.val, lidx))
                lhead = lhead.next
                lists[lidx] = lhead
        return dummy.next