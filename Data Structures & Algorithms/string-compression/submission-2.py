DBG = False
class Solution:
    def compress(self, chars: List[str]) -> int:
        lft, rgt = 0, 0
        while rgt < len(chars):
            while rgt < len(chars) and chars[rgt] == chars[lft]:
                rgt += 1
            delta = rgt - lft
            if delta == 1:
                lft = rgt
            else:
                lft += 1
                for c in str(delta):
                    chars[lft] = c
                    lft += 1
        DBG and print(chars[:lft], lft, rgt)
        return lft
