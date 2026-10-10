from collections import defaultdict
from typing import List


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.freq = defaultdict(int)
        self.unique = {}

        for num in nums:
            self.add(num)

    def add(self, value: int) -> None:
        self.freq[value] += 1

        if self.freq[value] == 1:
            self.unique[value] = None

        elif self.freq[value] == 2:
            del self.unique[value]

    def showFirstUnique(self) -> int:
        if not self.unique:
            return -1

        return next(iter(self.unique))