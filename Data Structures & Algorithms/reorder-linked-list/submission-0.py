# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_ = []
        node = head
        while node:
            list_.append(node)
            node = node.next

        dummy = ListNode()
        tail = dummy
        lft, rgt = 0, len(list_)-1
        while lft <= rgt:
            tail.next = list_[lft]
            tail.next.next = list_[rgt]
            tail = tail.next.next
            lft += 1
            rgt -= 1
        tail.next = None
        head = dummy.next