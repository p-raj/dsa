# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        onex, twox = head, head
        while twox.next and twox.next.next:
            onex = onex.next
            twox = twox.next.next
        
        fro = head
        rev = self.reverse(onex.next)
        # break the lists
        onex.next = None

        while rev:
            tmp1 = fro.next
            tmp2 = rev.next

            fro.next = rev
            rev.next = tmp1

            fro = tmp1
            rev = tmp2

