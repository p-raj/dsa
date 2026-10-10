class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lft, rgt = head, head
        while rgt and rgt.next:
            lft = lft.next
            rgt = rgt.next.next
            if lft == rgt:
                return True
        return False