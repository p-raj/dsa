from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stdq = deque([(s,0) for s in students])
        swsq = deque(sandwiches)

        while stdq and swsq:
            stud, atmt = stdq.popleft()
            if atmt > len(sandwiches):
                return len(stdq) + 1
            sdwh = swsq.popleft()
            if sdwh == stud:
                continue
            else:
                atmt += 1
                stdq.append((stud, atmt))
                swsq.appendleft(sdwh)
        return 0
