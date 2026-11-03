from bisect import bisect_left as bi_lft


class MyCalendar:
    def __init__(self):
        # any insert would either split the timline in two
        # of merge two timelines to make one
        # [(...).{.V.}.(...)] => [(...).(...).(...)]
        # [(...){..V.}.(...)] => [(......).(...)]
        self.timeline = []

    def _check(self, startTime: int, endTime: int) -> tuple[int, int]:
        sidx = bi_lft(self.timeline, startTime, key=lambda x: x[1])
        eidx = bi_lft(self.timeline, endTime, key=lambda x: x[0])
        return sidx, eidx

    def _split(self, startTime: int, endTime: int):
        pass

    def _merge(self, startTime: int, endTime: int):
        pass

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.timeline:
            self.timeline.append([startTime, endTime])
            return True
        else:
            sidx, eidx = self._check(startTime, endTime)
            compare_times = []
            if sidx < len(self.timeline):
                compare_times.append(self.timeline[sidx])
            if eidx < len(self.timeline):
                compare_times.append(self.timeline[eidx])
            if sidx == eidx and eidx == len(self.timeline):
                compare_times.append(self.timeline[-1])
            for s, e in compare_times:
                if (
                    (s <= startTime < e)
                    or (s < endTime < e)
                    or (startTime <= s and endTime > e)
                    or (startTime >= s and endTime < e)
                ):
                    return False
            self.timeline.insert(sidx, [startTime, endTime])
            print(self.timeline)
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
