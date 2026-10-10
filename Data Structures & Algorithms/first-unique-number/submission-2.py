from collections import Counter, deque
from typing import List


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.freq = Counter(nums)
        self.q = deque(nums)

    def showFirstUnique(self) -> int:
        while self.q and self.freq[self.q[0]] > 1:
            self.q.popleft()

        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        self.freq[value] += 1
        self.q.append(value)