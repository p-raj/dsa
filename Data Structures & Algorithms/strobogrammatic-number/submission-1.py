class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map_180 = {
            "0": "0",
            "1": "1",
            # "2": "5",
            # 4?
            # "5": "2",
            "6": "9",
            # 7?
            "8": "8",
            "9": "6",
        }
        num = [c for c in num]
        for c in num:
            if c not in map_180:
                return False
        return True
