class Solution:
    def isPathCrossing(self, path: str) -> bool:
        track = set()
        cur = (0, 0)
        d = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (-1, 0),
            "W": (1, 0),
        }
        for p in path:
            track.add(cur)
            cur = (cur[0] + d[p][0], cur[1] + d[p][1])
            if cur in track:
                return True
        return False
