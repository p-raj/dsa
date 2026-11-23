class Solution:
    def romanToInt(self, s: str) -> int:
        # C [D, M]
        # X [L, C]
        # I [V, X]
        # IXCD / IXCM
        # IXL / IXC
        # IV / IX
        # I
        map_ = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }
        num_ = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        lft = 0
        ans = 0
        while lft < len(s):
            roman = [s[lft]]
            rgt = lft + 1
            while rgt < len(s) and s[lft] in map_ and s[rgt] in map_[ s[lft]]:
                roman.append(s[rgt])
                rgt += 1
            lft = rgt
            if len(roman) == 1:
                ans += num_[roman.pop()]
            else:
                temp = 0
                while roman:
                    if temp == 0:
                        temp = num_[roman.pop()]
                    else:
                        temp -= num_[roman.pop()]
                ans += temp

        return ans
            