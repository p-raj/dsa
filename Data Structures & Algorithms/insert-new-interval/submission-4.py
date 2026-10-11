import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        lft, rgt = newInterval
        lidx = bisect.bisect_left(intervals, lft, key= lambda x: x[1])
        if lidx == len(intervals):
            intervals.append(newInterval)
            return intervals

        start = min(lft, intervals[lidx][0])

        has_tail = False
        end = rgt
        ridx = lidx
        while ridx < len(intervals):
            print(len(intervals), ridx, rgt, intervals[ridx])
            if rgt > intervals[ridx][1]:
                ridx += 1
                continue

            if intervals[ridx][0] <= rgt < intervals[ridx][1]:
                end = intervals[ridx][1]
                ridx += 1
            break

        has_tail = ridx < len(intervals)
        if has_tail:
            res = [*intervals[:lidx], [start, end], *intervals[ridx:]]
        else:
            res = [*intervals[:lidx], [start, end], *intervals[ridx+1:]]
        print(lidx, ridx, " || ", res)
        print("--"*20)
        return res
