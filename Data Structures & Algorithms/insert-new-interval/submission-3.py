import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        lft, rgt = newInterval
        lidx = bisect.bisect_left(intervals, lft, key= lambda x: x[1])
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

# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
# Solution().insert(intervals, newInterval)

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# Solution().insert(intervals, newInterval)

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