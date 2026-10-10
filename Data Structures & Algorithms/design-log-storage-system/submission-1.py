from datetime import datetime


class LogSystem:
    def __init__(self):
        self.tree = Btree()

    def _dt(self, timestamp: str, granularity: str | None = None) -> datetime:
        yyyy, mm, dd, HH, MM, SS = map(int, timestamp.split(":"))
        # datetime(year, month, day, hour, minute, second, microsecond)
        # if granularity == "Year":
        #     dt = datetime(yyyy, 1, 1, 0, 0, 0)
        # elif granularity == "Month":
        #     dt = datetime(yyyy, mm, 1, 0, 0, 0)
        # elif granularity == "Day":
        #     dt = datetime(yyyy, mm, dd, 0, 0, 0)
        # elif granularity == "Hour":
        #     dt = datetime(yyyy, mm, dd, HH, 0, 0)
        # elif granularity == "Minute":
        #     dt = datetime(yyyy, mm, dd, HH, MM, 0)
        # else:
        return datetime(yyyy, mm, dd, HH, MM, SS)

    def put(self, id: int, timestamp: str) -> None:
        ut = self._dt(timestamp)
        self.tree.add(ut, id)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        uts = self._dt(start, granularity)
        ute = self._dt(end, granularity)
        res = self.tree.search(uts, ute, granularity)
        return [v for _, v in res]


class BNode:
    def __init__(
        self,
        key: datetime,
        val: int,
        lft: BNode | None = None,
        rgt: BNode | None = None,
    ):
        self.key = key
        self.val = val
        self.lft = lft
        self.rgt = rgt


class Btree:
    def __init__(self):
        self.root: BNode | None = None

    def add(self, key: datetime, val: int):
        node = BNode(key, val)

        # _insert returns the root of the modified subtree.
        self.root = self._insert(self.root, node)

    def _insert(self, root: BNode | None, node: BNode) -> BNode:
        # Found the position where the new node belongs.
        if root is None:
            return node

        if node.key < root.key:
            root.lft = self._insert(root.lft, node)
        else:
            root.rgt = self._insert(root.rgt, node)

        return root

    def search(self, start: datetime, end: datetime, granularity: str) -> list:
        result = list()
        self._retrieve(self.root, start, end, granularity, result)
        return result

    def _compare(self, start: datetime, root: datetime, end: datetime, granularity: str):
        if granularity == "Year":
            return start.year <= root.year <= end.year
        elif granularity == "Month":
            return (start.year, start.month) <= (root.year, root.month) <= (end.year, end.month)
        elif granularity == "Day":
            return (
                (start.year, start.month, start.day)
                <= (root.year, root.month, root.day)
                <= (end.year, end.month, end.day)
            )
        elif granularity == "Hour":
            return (
                (start.year, start.month, start.day, start.hour)
                <= (root.year, root.month, root.day, root.hour)
                <= (end.year, end.month, end.day, end.hour)
            )
        elif granularity == "Minute":
            return (
                (start.year, start.month, start.day, start.hour, start.minute)
                <= (root.year, root.month, root.day, root.hour, root.minute)
                <= (end.year, end.month, end.day, end.hour, end.minute)
            )
        else:
            return start <= root <= end

    def _gkey(self, dt: datetime, granularity: str):
        if granularity == "Year":
            return (dt.year,)
        elif granularity == "Month":
            return (dt.year, dt.month)
        elif granularity == "Day":
            return (dt.year, dt.month, dt.day)
        elif granularity == "Hour":
            return (dt.year, dt.month, dt.day, dt.hour)
        elif granularity == "Minute":
            return (dt.year, dt.month, dt.day, dt.hour, dt.minute)
        else:
            return (
                dt.year,
                dt.month,
                dt.day,
                dt.hour,
                dt.minute,
                dt.second,
            )

    def _retrieve(
        self, root: BNode | None, start: datetime, end: datetime, granularity: str, result: list
    ):
        if root is None:
            return
        s = self._gkey(start, granularity)
        r = self._gkey(root.key, granularity)
        e = self._gkey(end, granularity)
        if s <= r:
            self._retrieve(root.lft, start, end, granularity, result)

        if s <= r <= e:
            result.append((root.key, root.val))

        if r <= e:
            self._retrieve(root.rgt, start, end, granularity, result)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, root: BNode | None, depth: int = 0):
        if root is None:
            return

        # Print right subtree first
        self._print_tree(root.rgt, depth + 1)

        print("    " * depth + f"{root.key}: {root.val}")

        # Then print left subtree
        self._print_tree(root.lft, depth + 1)


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
