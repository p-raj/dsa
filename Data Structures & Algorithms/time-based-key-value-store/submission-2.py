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
            if timestamp == ts[mid]:
                return self.kv[key][ts[mid]][-1]
            elif timestamp < ts[mid]:
                rgt = mid - 1
            else:
                lft = mid + 1
        if ts[lft] > timestamp:
            return ""
        return self.kv[key][ts[lft]][-1]
