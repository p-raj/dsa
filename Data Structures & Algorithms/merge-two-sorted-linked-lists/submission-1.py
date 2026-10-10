class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        h1 = list1
        h2 = list2

        dummy = ListNode()
        tail = dummy

        while h1 and h2:
            if h1.val <= h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next

            tail = tail.next

        if h1:
            tail.next = h1
        else:
            tail.next = h2

        return dummy.next