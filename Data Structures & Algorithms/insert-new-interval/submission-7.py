import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        lft, rgt = newInterval

        if len(intervals) == 1:
            if rgt < intervals[0][0]:
                intervals.insert(0, newInterval)
                return intervals
            if lft > intervals[0][1]:
                intervals.append(newInterval)
                return intervals
            elif intervals[0][0] <= lft <= intervals[0][1] or intervals[0][0] <= rgt <= intervals[0][1]:
                return [[min(intervals[0][0], lft), max(intervals[0][1], rgt)]]
    

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
        return res
