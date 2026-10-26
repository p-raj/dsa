class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        short = sentence1.split(" ")
        long = sentence2.split(" ")

        if len(short) > len(long):
            short, long = long, short

        left = 0
        while left < len(short) and long[left] == short[left]:
            left += 1

        right = 0
        while right < len(short) - left and long[-1 - right] == short[-1 - right]:
            right += 1

        return left + right == len(short)
