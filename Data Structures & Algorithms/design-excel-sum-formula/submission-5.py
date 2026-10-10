
from collections import Counter
from typing import List


class Excel:
    def __init__(self, height: int, width: str):
        cols = ord(width) - ord("A") + 1

        # Values assigned directly using set().
        self.values = [[0] * cols for _ in range(height)]

        # (row, col) -> Counter of referenced cells
        self.formulas = {}

    def _parse(self, cell: str) -> tuple[int, int]:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        return row, col

    def set(self, row: int, column: str, val: int) -> None:
        r = row - 1
        c = ord(column) - ord("A")
        cell = (r, c)

        # A direct assignment replaces any existing formula.
        self.formulas.pop(cell, None)
        self.values[r][c] = val

    def get(self, row: int, column: str) -> int:
        cell = (row - 1, ord(column) - ord("A"))
        memo = {}

        def evaluate(cell):
            if cell in memo:
                return memo[cell]

            # Literal cells have no formula.
            if cell not in self.formulas:
                r, c = cell
                result = self.values[r][c]
            else:
                # Recursively evaluate referenced cells.
                result = 0

                for dependency, count in self.formulas[cell].items():
                    result += count * evaluate(dependency)

            memo[cell] = result
            return result

        return evaluate(cell)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        references = Counter()

        for number in numbers:
            if ":" not in number:
                # Single cell reference.
                references[self._parse(number)] += 1
            else:
                # Rectangular range.
                start, end = number.split(":")
                r1, c1 = self._parse(start)
                r2, c2 = self._parse(end)

                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        references[(r, c)] += 1

        cell = (row - 1, ord(column) - ord("A"))

        # Replace any previous formula with this one.
        self.formulas[cell] = references

        # Evaluate the new formula.
        return self.get(row, column)
