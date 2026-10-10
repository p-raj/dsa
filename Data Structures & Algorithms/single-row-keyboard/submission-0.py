class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {
            ch:idx for idx, ch in enumerate(keyboard)
        }
        lft = 0
        time_ = 0
        for ch in word:
            time_ += abs(
                pos[ch] - lft
            )
            lft = pos[ch]
        return time_