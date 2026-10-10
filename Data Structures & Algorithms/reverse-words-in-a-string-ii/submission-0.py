class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lft = 0
        rgt = len(s)-1
        while lft < rgt:
            s[lft], s[rgt] = s[rgt], s[lft]
            lft += 1
            rgt -= 1
        lft = 0
        while lft < len(s):
            rgt = lft
            while rgt < len(s):
                if s[rgt] == " ":
                    break
                rgt += 1
            r = rgt - 1
            l = lft
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            lft = rgt + 1
# s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Solution().reverseWords(s)