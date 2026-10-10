# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rais = 0
        carr = 0
        num1 = l1
        num2 = l2
        prev1 = None
        while num1 and num2:
            v = carr + num1.val + num2.val
            if v > 9:
                carr = 1
                v = v % 10
            else:
                carr = 0
            num1.val = v
            prev1 = num1
            num1 = num1.next
            num2 = num2.next

        while num1:
            v = carr + num1.val
            if v > 9:
                carr = 1
                v = v % 10
            else:
                carr = 0
            prev1 = num1
            num1.val = v
            num1 = num1.next

        while num2:
            v = carr + num2.val
            if v > 9:
                carr = 1
                v = v % 10
            else:
                carr = 0
            prev1.next = num2
            num2.val = v
            prev1 = num2
            num2 = num2.next

        if carr:
            prev1.next = ListNode(1)
        return l1