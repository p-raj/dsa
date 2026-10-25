class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s)
        while left + 1 < right and s[left] == s[right - 1]:
            c = s[left]
            while left < right and s[left] == c:
                left += 1
            while left < right and s[right - 1] == c:
                right -= 1
        return right - left
