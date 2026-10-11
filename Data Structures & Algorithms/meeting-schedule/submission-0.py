"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meets = [(i.start, i.end) for i in intervals]
        meets = sorted(meets, key=lambda x: x[0])
        lft = 0
        while lft < len(meets) - 1:
            rgt = lft + 1
            if meets[rgt][0] > meets[lft][1]:
                lft = rgt
            else:
                return False
        return True