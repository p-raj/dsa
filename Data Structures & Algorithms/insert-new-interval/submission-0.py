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
        if ridx < len(newInterval):
            end = max(rgt, intervals[ridx][1])
        else:
            end = rgt
        if include_last:
            res = [*intervals[:lidx], [start, end], *intervals[ridx:]]
            # print(lidx, ridx, res)
        else:
            res = [*intervals[:lidx], [start, end], *intervals[ridx+1:]]
            # print(lidx, ridx, res)
        return res

# intervals = [[1,3],[4,6]]
# newInterval = [2,5]
# Solution().insert(intervals, newInterval)

# intervals = [[1,3],[4,6]]
# newInterval = [2,7]
# Solution().insert(intervals, newInterval)

# intervals = [[1,3],[4,6]]
# newInterval = [0,7]
# Solution().insert(intervals, newInterval)

# intervals = [[1,2],[3,5],[9,10]]
# newInterval = [6,7]
# Solution().insert(intervals, newInterval)

# intervals = [[1,2],[3,5],[9,10]]
# newInterval = [6,11]
# Solution().insert(intervals, newInterval)

# intervals = [[1,2],[3,5],[9,10]]
# newInterval = [0,11]
# Solution().insert(intervals, newInterval)

# intervals = [[1,2],[3,5],[9,10]]
# newInterval = [3,11]
# Solution().insert(intervals, newInterval)

# intervals = [[1,2],[3,5],[9,10]]
# newInterval = [2,11]
# Solution().insert(intervals, newInterval)

# intervals = [[1,2],[3,5],[9,10]]
# newInterval = [4,6]
# Solution().insert(intervals, newInterval)