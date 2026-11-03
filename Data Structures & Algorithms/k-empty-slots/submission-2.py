DBG = False


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        N1 = -1
        Bidx = {d: idx for idx, d in enumerate(bulbs)}
        last_on = N1

        day = 0
        while day < len(bulbs):
            day += 1
            oidx = Bidx[day]
            DBG and print(f"{last_on=} | {oidx - last_on=}")
            if (last_on == N1) or (last_on > N1 and abs(oidx - last_on) != (k + 1)):
                last_on = oidx
            else:
                return day
        return -1
