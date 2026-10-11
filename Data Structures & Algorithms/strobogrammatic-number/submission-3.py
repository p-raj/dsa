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
        rot = [c for c in num]
        for idx, c in enumerate(rot):
            if c not in map_180:
                return False
            rot[idx] = map_180[c]
        lft = 0
        rgt = len(rot) - 1
        while lft <= rgt:
            print(num[lft], rot[rgt], num[lft] == rot[rgt])
            if num[lft] == rot[rgt]:
                lft += 1
                rgt -= 1
            else:
                return False
        print(rot, num)
        return True
