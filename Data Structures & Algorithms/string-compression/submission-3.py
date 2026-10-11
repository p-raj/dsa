class Solution:
    def compress(self, chars: List[str]) -> int:
        lft, rgt = 0, 0
        n = len(chars)

        while rgt < n:
            char = chars[rgt]
            start = rgt

            # Find the end of the current group
            while rgt < n and chars[rgt] == char:
                rgt += 1

            # Number of characters in this group
            count = rgt - start

            # Always write the character
            chars[lft] = char
            lft += 1

            # Write the count only for repeated characters
            if count > 1:
                for digit in str(count):
                    chars[lft] = digit
                    lft += 1

        return lft