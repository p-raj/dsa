class TimeMap:

    def __init__(self):
        self.kv = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv:
            self.kv[key] = {}
        if timestamp not in self.kv[key]:
            self.kv[key][timestamp] = list()
        self.kv[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kv:
            return ""
        ts = list(self.kv[key].keys())
        ts.sort()
        lft = 0
        rgt = len(ts) - 1
        while lft < rgt:
            mid = (lft+rgt)//2
            tmid = ts[mid]
            if timestamp == tmid:
                return self.kv[key][tmid][-1]
            elif timestamp < tmid:
                rgt = mid - 1
            else:
                lft = mid + 1
        lft = len(ts) - 1 if lft >= len(ts) else lft
        rgt = len(ts) - 1 if rgt >= len(ts) else rgt
        lft = 0 if lft < 0 else lft
        rgt = 0 if rgt < 0 else rgt
        if lft == 0 and ts[lft] > timestamp:
            return ""
        return self.kv[key][ts[rgt]][-1]
