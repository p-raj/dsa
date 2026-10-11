class Solution:
    def compress(self, chars: List[str]) -> int:
        lft, rgt = 0, 1
        while rgt < len(chars):
            while rgt < len(chars) and chars[rgt] == chars[lft]:
                rgt += 1
            delta = rgt - lft
            if delta == 1:
                lft += 1
                rgt += 1
                continue
            else:
                lft += 1
                for c in str(delta):
                    chars[lft] = c
                    lft += 1
        print(chars, lft, rgt)
        return lft if lft != 0 else 1