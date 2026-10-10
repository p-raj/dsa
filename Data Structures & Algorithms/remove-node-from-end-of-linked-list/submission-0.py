# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        len_ = 0
        while node:
            node = node.next
            len_ += 1

        rem_at =  len_ - n
        prev = None
        node = head
        curr = 0
        print(curr, rem_at)
        while curr != rem_at and node:
            print(curr, rem_at, node.val)
            prev = node
            node = node.next
            curr += 1
        if not prev:
            head = head.next
            return head
        if not node.next:
            prev.next = None
        else:
            prev.next = node.next
        node.next = None
        return head