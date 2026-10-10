# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def _dbg(self, name: str, node: Optional[ListNode]) -> None:
        return
        print(name, "]", end="")
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print()

    def revk_or_same(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        rev = []
        dummy = ListNode()
        tail = dummy

        while k != 0:
            if node:
                rev.append(node.val)
            else:
                for v in rev:
                    tail.next = ListNode(v)
                    tail = tail.next
                return dummy.next, tail, node
            node = node.next
            k-=1
        
        while rev:
            tail.next = ListNode(rev.pop())
            tail = tail.next
        self._dbg("dummy", dummy)
        self._dbg("node", node)
        return dummy.next, tail, node
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        nxt = head
        while True:
            nod, tal, nxt = self.revk_or_same(nxt, k)
            tail.next = nod
            tail = tal
            self._dbg("nod", nod)
            self._dbg("nxt", nxt)
            self._dbg("tail", tail)
            if nxt is None:
                break
        return dummy.next