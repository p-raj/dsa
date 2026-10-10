class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.lft = None
        self.rgt = None
        self.par = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        prev = None
        node = self.root
        new_node = TreeNode(key, val)
        if not node:
            self.root = new_node
        else:
            while node:
                if node.key == key:
                    node.val = val
                    return
                prev = node
                if node.key > key:
                    node = node.lft
                else:
                    node = node.rgt

            if new_node.key > prev.key:
                prev.rgt = new_node
            else:
                prev.lft = new_node
            new_node.par = prev

    def get(self, key: int) -> int:
        node = self.root
        if not node:
            return -1

        while node:
            if key == node.key:
                return node.val
            elif key > node.key:
                node = node.rgt
            else:
                node = node.lft
        return -1

    def getMin(self) -> int:
        node = self.root
        if not node:
            return -1
        while node.lft:
            node = node.lft
        return node.val

    def getMax(self) -> int:
        node = self.root
        if not node:
            return -1
        while node.rgt:
            node = node.rgt
        return node.val
    
    def get_min(self, node: TreeNode) -> TreeNode:
        while node.lft:
            node = node.lft
        return node
    
    def get_max(self, node: TreeNode) -> TreeNode:
        while node.rgt:
            node = node.rgt
        return node

    def transplant(self, u: TreeNode, v: TreeNode):
        if u.par is None:
            self.root = v
        elif u.par.lft is u:
            u.par.lft = v
        else:
            u.par.rgt = v
        if v:
            v.par = u.par
    def remove(self, key: int) -> None:
        node = self.root
        while node and node.key != key:
            if node.key > key:
                node = node.lft
            else:
                node = node.rgt
        if not node:
            return
        
        if node.lft is None:
            self.transplant(node, node.rgt)
        elif node.rgt is None:
            self.transplant(node, node.lft)
        else:
            # 2 child
            succ = self.get_min(node.rgt)
            if succ.par is not node:
                self.transplant(succ, succ.rgt)
                succ.rgt = node.rgt
                succ.rgt.par = succ
            self.transplant(node, succ)
            succ.lft = node.lft
            succ.lft.par = succ

    def getInorderKeys(self) -> List[int]:
        stack = []
        values = []
        if not self.root:
            return values
        node = self.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.lft
            node = stack.pop()
            values.append(node.key)
            node = node.rgt
        return values
