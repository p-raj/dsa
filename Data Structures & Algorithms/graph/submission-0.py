class Graph:
    
    def __init__(self):
        self.graph: dict[int, set[int]] = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        if dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        stack = [src]
        processed = set()
        while stack:
            # print(f"f{stack=}")
            node = stack.pop()
            # print(f"{node=}")
            if node == dst:
                return True
            processed.add(node)
            # print(f"{processed=}")
            if node in self.graph:
                # print(f"{self.graph[node]=}")
                # print(f"{self.graph[node].difference(processed)}=")
                stack.extend(list(self.graph[node].difference(processed)) or [])

        return False