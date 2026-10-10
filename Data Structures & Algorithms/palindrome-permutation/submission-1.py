class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        from collections import Counter

        freq = Counter(s)
        odds = 0

        for letter, count in freq.items():

            if count % 2 != 0:
                odds += 1

            if odds > 1:
                return False

        return True


        