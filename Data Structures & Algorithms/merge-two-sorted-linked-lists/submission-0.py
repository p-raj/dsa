# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        h3 = None
        node = None
        prev = None
        while h1 and h2:
            if h1.val > h2.val:
                node = ListNode(h2.val)
                if h3 is None:
                    h3 = node
                    prev = h3
                else:
                    prev.next = node
                    prev = node
                h2 = h2.next
            else:
                node = ListNode(h1.val)
                if h3 is None:
                    h3 = node
                    prev = h3
                else:
                    prev.next = node
                    prev = node
                h1 = h1.next
        
        while h1:
            node = ListNode(h1.val)
            if h3 is None:
                h3 = node
                prev = h3
            else:
                prev.next = node
                prev = node
            h1 = h1.next
        
        while h2:
            node = ListNode(h2.val)
            if h3 is None:
                h3 = node
                prev = h3
            else:
                prev.next = node
                prev = node
            h2 = h2.next
        
        return h3