class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0] * 26
        i = 0
        while i < len(t):
            # inc
            arr[ord(s[i]) - ord('a')] += 1
            # reset
            arr[ord(t[i]) - ord('a')] -= 1
            i += 1
        i = 0
        while i < len(arr):
            if arr[i] != 0:
                return False
            i += 1
        return True