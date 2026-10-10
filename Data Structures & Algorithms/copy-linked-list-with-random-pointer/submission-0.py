class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = None
        new_node = None
        node = head
        map_ = {}

        # pass 1: copy next-chain nodes
        while node:
            new_ = Node(x=node.val)

            if new_head is None:
                new_head = new_
                new_node = new_head
            else:
                new_node.next = new_
                new_node = new_node.next

            map_[node] = new_
            node = node.next

        # pass 2: copy random pointers
        node = head
        new_node = new_head

        while node:
            new_node.random = map_[node.random] if node.random else None
            node = node.next
            new_node = new_node.next

        return new_head