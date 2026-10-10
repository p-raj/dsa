# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dbg(pos, head, node, prev):
            return
            if prev is None:
                print(f"{pos} ] head: {head.val} | node: {node.val} | prev: None")
            else:
                print(f"{pos} ] head: {head.val} | node: {node.val} | prev: {prev.val}")
        if not head or not head.next:
            return head
        prev = None
        node = head
        while node.next:
            dbg("start", head, node, prev)
            head = node.next
            dbg("head move", head, node, prev)
            node.next = prev
            dbg("reversed", head, node, prev)
            prev = node
            dbg("node -> prev", head, node, prev)
            node = head
            dbg("node fwd", head, node, prev)
        dbg("final", head, node, prev)
        node.next = prev
        return node
