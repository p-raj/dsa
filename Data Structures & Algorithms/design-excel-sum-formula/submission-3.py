from collections import Counter

DBG = True


class Excel:
    def __init__(self, height: int, width: str):
        self.h = height
        self.w = self._get_col_idx(width)
        self.sheet = [[0 for _ in range(self.w + 1)] for _ in range(self.h)]
        self.cell_depends_on = {}
        self.on_chng_push_to = {}

    def _get_col_idx(self, column: str) -> int:
        return ord(column) - ord("A")

    def _get_col_str(self, col_idx: int) -> str:
        return chr(col_idx + ord("A"))

    def _parse_number_to_idx(self, number: str) -> tuple[int, int]:
        col = number[0]
        row = number[1:]
        return int(row) - 1, self._get_col_idx(col)

    def _parse_idx_to_number(self, row_idx: int, col_idx: int) -> str:
        r = row_idx + 1
        c = self._get_col_str(col_idx)
        return f"{c}{r}"

    def _get_sum(self, number: str) -> int:
        if not number.strip():
            return 0
        elif number.find(":") >= 0:
            strt, end = number.split(":")
            strt_row, strt_col = self._parse_number_to_idx(strt)
            end_row, end_col = self._parse_number_to_idx(end)
            sm = 0
            r = strt_row
            while r != end_row + 1:
                c = strt_col
                while c != end_col + 1:
                    sm += self.sheet[r][c]
                    c += 1
                r += 1
            return sm
        else:
            strt = number
            r, c = self._parse_number_to_idx(strt)
            return self.sheet[r][c]

    def _get_range_number(self, number: str) -> list[str]:
        nums = []
        if not number.strip():
            return nums
        elif number.find(":") >= 0:
            strt, end = number.split(":")
            strt_row, strt_col = self._parse_number_to_idx(strt)
            end_row, end_col = self._parse_number_to_idx(end)
            r = strt_row
            while r != end_row + 1:
                c = strt_col
                while c != end_col + 1:
                    nums.append(self._parse_idx_to_number(r, c))
                    c += 1
                r += 1
            return nums
        else:
            strt = number
            r, c = self._parse_number_to_idx(strt)
            nums.append(self._parse_idx_to_number(r, c))
            return nums

    def _get_range_numbers(self, numbers: list[str]) -> list[str]:
        nums = []
        for n in numbers:
            nums += self._get_range_number(n)
        return nums

    def _get_number(self, row: int, column: str) -> str:
        return f"{column}{row}"

    def _add_dependencies(self, row, column, numbers):
        target = self._get_number(row, column)

        for source in self.cell_depends_on[target]:
            if source not in self.on_chng_push_to:
                self.on_chng_push_to[source] = Counter()

            self.on_chng_push_to[source][target] += 1

    def _rm_dependencies(self, row, column):
        target = self._get_number(row, column)

        sources = self.cell_depends_on.pop(target, [])

        for source in set(sources):
            dependents = self.on_chng_push_to[source]

            del dependents[target]

            if not dependents:
                del self.on_chng_push_to[source]

    def _update_dependencies(self, row: int, column: str, numbers: List[str]):
        self._rm_dependencies(row, column)
        didx = self._get_number(row, column)
        self.cell_depends_on[didx] = self._get_range_numbers(numbers)
        self._add_dependencies(row, column, numbers)

    def _trigger_topology(self, row: int, column: str):
        # cascading updates
        # topological sorting
        didx = self._get_number(row, column)
        cidx = self._get_col_idx(column)
        sm = self.sheet[row - 1][cidx]
        if didx not in self.cell_depends_on:
            return
        for deps in self.cell_depends_on[didx]:
            DBG and print(deps, self._get_sum(deps))
            sm += self._get_sum(deps)
        self.sheet[row - 1][cidx] = sm
        DBG and print(self.cell_depends_on)
        DBG and print(self.on_chng_push_to)
        DBG and print(self.sheet)

    def _set(self, row: int, column: str, val: int) -> None:
        col_idx = self._get_col_idx(column)

        old = self.sheet[row - 1][col_idx]
        self.sheet[row - 1][col_idx] = val

        delta = val - old

        stack = [(self._get_number(row, column), delta)]

        while stack:
            source, change = stack.pop()

            if change == 0:
                continue

            for target, weight in self.on_chng_push_to.get(source, {}).items():
                propagated_change = change * weight
                r, c = self._parse_number_to_idx(target)
                self.sheet[r][c] += propagated_change
                stack.append((target, propagated_change))

    def set(self, row: int, column: str, val: int) -> None:
        self._rm_dependencies(row, column)
        self._set(row, column, val)

    def _get_by_num(self, number: str) -> int:
        r, c = self._parse_number_to_idx(number)
        return self.sheet[r][c]

    def get(self, row: int, column: str) -> int:
        return self._get_by_num(f"{column}{row}")

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        # Expand ranges, preserving repeated references.
        references = self._get_range_numbers(numbers)

        # Calculate the new formula value.
        new_value = sum(self._get_by_num(ref) for ref in references)

        # Replace the previous formula and its graph edges.
        self._update_dependencies(row, column, numbers)

        # Update through the propagation mechanism.
        self._set(row, column, new_value)

        return new_value


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
