DBG = False
from collections import deque


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Friend (i)
        # In: times[i][0]
        # Out: times[i][1]
        # [
        # i=0  [1,3] In: 1, Out: 3
        # i=1  [2,5] In: 2, Out: 5
        # i=2  [3,6] In: 3, Out: 6
        # ]
        # In <> Out sorted
        in_ = {v[0]: idx for idx, v in enumerate(times)}

        maxt = max([v[1] for v in times])

        now = 0
        min_chair = 0
        chairs = deque()

        while now <= maxt:
            # # Pop from the left (front)
            # first = dq.popleft()
            while chairs:
                frnd, chair = chairs.popleft()
                DBG and print(f"{times[frnd]=}, {now=}")
                if times[frnd][1] <= now:
                    min_chair = min(min_chair, chair)
                else:
                    chairs.appendleft((frnd, chair))
                    break
            DBG and print(f"{chairs=}")
            DBG and print(f"{in_=}, {now=}, {now in in_}")
            # someone in?
            if now in in_:
                frnd = in_[now]
                if frnd == targetFriend:
                    return min_chair
                chairs.append((frnd, min_chair))
                min_chair += 1
                DBG and print(f"{chairs=}")
            # how many people are leaving now?
            # Push to the left (front)
            # dq.appendleft("a")
            # dq is now deque(['a', 'b', 'c'])
            now += 1
            
