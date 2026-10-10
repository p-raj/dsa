class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t = 0
        count = 0

        while t < len(target):
            old_t = t

            for ch in source:
                if t < len(target) and ch == target[t]:
                    t += 1

            if t == old_t:
                return -1

            count += 1

        return count