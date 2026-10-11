# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        lft, rgt = head, head
        while rgt and n > 0:
            rgt = rgt.next
            n -= 1
        if rgt:
            print(f"{lft.val=}, {rgt.val=}")
        else:
            print(f"{lft.val=}, rgt == n")
        while rgt and rgt.next:
            lft = lft.next
            rgt = rgt.next
        if rgt:
            print(f"{lft.val=}, {rgt.val=}")
        else:
            print(f"{lft.val=}, rgt x")
        lft.next = rgt
        return head
