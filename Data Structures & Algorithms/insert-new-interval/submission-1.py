import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lft, rgt = newInterval
        lidx = bisect.bisect_left(intervals, lft, key= lambda x: x[1])
        ridx = lidx
        include_last = False
        while ridx < len(intervals):
            if rgt < intervals[ridx][0]:
                include_last = True
                break
            if intervals[ridx][0] < rgt < intervals[ridx][1]:
                include_last = False
                break
            ridx += 1
        start = min(lft, intervals[lidx][0])
        end = rgt
        if ridx < len(newInterval):
            if not include_last:
                end = max(rgt, intervals[ridx][1])
            
        if include_last:
            res = [*intervals[:lidx], [start, end], *intervals[ridx:]]
            print(lidx, ridx, res)
        else:
            res = [*intervals[:lidx], [start, end], *intervals[ridx+1:]]
            print(lidx, ridx, res)
        return res
