class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lft = 0
        rgt = len(s) - 1
        while lft < rgt:
            s[lft], s[rgt] = s[rgt], s[lft]
            rgt -= 1
            lft += 1