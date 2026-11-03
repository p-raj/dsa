from bisect import bisect_left as bi_lft


class MyCalendar:
    def __init__(self):
        # any insert would either split the timline in two
        # of merge two timelines to make one
        # [(...).{.V.}.(...)] => [(...).(...).(...)]
        # [(...){..V.}.(...)] => [(......).(...)]
        self.timeline = []

    def _check(self, startTime: int, endTime: int) -> tuple[int, int]:
        # sidx = bi_lft(self.timeline, startTime, key=lambda x: x[1])
        # eidx = bi_lft(self.timeline, endTime, key=lambda x: x[0])
        iidx = bi_lft(self.timeline, [startTime, endTime])
        return iidx - 1, iidx, iidx

    def _split(self, startTime: int, endTime: int):
        pass

    def _merge(self, startTime: int, endTime: int):
        pass

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.timeline:
            self.timeline.append([startTime, endTime])
            return True
        else:
            sidx, eidx, iidx = self._check(startTime, endTime)
            compare_times = []
            for i in range(sidx, eidx + 1):
                if i < len(self.timeline):
                    compare_times.append(self.timeline[i])
            for s, e in compare_times:
                # simplified:
                # if startTime < e and s < endTime:
                #     return False
                print(s, e, startTime, endTime)
                if startTime == s and endTime == e:
                    return False
                if startTime < s and endTime > e:
                    return False
                if s < startTime < e:
                    return False
                if s < endTime < e:
                    return False
                if startTime < s < endTime:
                    return False
                if startTime < e < endTime:
                    return False
            self.timeline.insert(iidx, [startTime, endTime])
            print(self.timeline)
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
