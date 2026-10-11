class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        lft = 0
        while lft < len(intervals):
            rgt = lft
            start, end = intervals[lft]
            while rgt < len(intervals) and start == intervals[rgt][0]:
                end = max(
                    end,
                    intervals[rgt][1]
                )
                rgt += 1
            if rgt == len(intervals):
                res.append([start, max(
                    end,
                    intervals[rgt-1][1]
                )])
                break
            elif end < intervals[rgt][0]:
                res.append([start, end])
                lft = rgt
            elif intervals[rgt][0] <= end <= intervals[rgt][1]:
                res.append([start, max(
                    end,
                    intervals[rgt][1]
                )])
                lft = rgt+1
        return res
            