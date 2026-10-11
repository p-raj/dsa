class Solution:
    def update_map(self, ch, char_map: dict, action="+") -> tuple(str, int):
        if ch not in char_map:
            char_map[ch] = 0
        if action == "+":
            char_map[ch] += 1
        else:
            char_map[ch] -= 1
        max_k = None
        max_v = 0
        for k, v in char_map.items():
            if v > max_v:
                max_v = v
                max_k = k
        return max_k, max_v

    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        lft, rgt = 0, 0
        max_len = 0
        while rgt < len(s):
            mk, mv = self.update_map(s[rgt], char_map, "+")
            rgt += 1
            if rgt - lft > max_len:
                max_len = rgt - lft
            if max_len - mv <= k:
                rgt += 1
            else:
                lft += 1
                mk, mv = self.update_map(s[lft], char_map, "-")
        if rgt - lft > max_len:
            max_len = rgt - lft
        return max_len