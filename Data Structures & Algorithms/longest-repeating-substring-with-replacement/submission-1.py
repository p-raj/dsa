class Solution:
    def update_map(self, ch, char_map: dict, action="+"):
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
        lft = 0
        max_len = 0
        for rgt in range(len(s)):
            mk, mv = self.update_map(s[rgt], char_map, "+")
            while (rgt - lft + 1) - mv > k:
                mk, mv = self.update_map(s[lft], char_map, "-")
                lft += 1
            max_len = max(max_len, rgt - lft + 1)

        return max_len