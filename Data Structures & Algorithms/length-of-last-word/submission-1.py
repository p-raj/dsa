class Solution:
    def is_alpha(self, ch: char) -> bool:
        # Uppercase (A-Z)65 – 90chr(65) returns 'A'
        # Lowercase (a-z)97 – 122chr(97) returns 'a'
        return 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122

    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        len_ = 0
        while end >= 0 and not self.is_alpha(s[end]):
            end -= 1
        if end < 0:
            return len_
        while end >= 0 and self.is_alpha(s[end]):
            len_ += 1
            end -= 1
        return len_
