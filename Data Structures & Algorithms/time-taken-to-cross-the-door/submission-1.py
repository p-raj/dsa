class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        # one door
        # arrival = [1,2,3,4]
        # state   = [0,1,0,1]
        # if door not used in last second => exit
        # if used for enter => enter
        # if used for exit  => exit
        # smallest person wins
        # answer  = [t1, t2, t3, t4]
        answer = [0] * len(arrival)
        last_door = None # 0 (enter), 1 (exit)
        ent0 = []
        exi1 = []
        idx = 0
        t = 0
        while True:
            if len(ent0) == 0 and len(exi1) == 0 and idx >= len(arrival):
                return answer
            while idx < len(arrival) and arrival[idx] <= t:
                if state[idx]:
                    exi1.append((arrival[idx], idx))
                else:
                    ent0.append((arrival[idx], idx))
                idx += 1
            # if not exi1 and not ent0 and idx < len(arrival):
            #     # optimization
            #     t = max(t, arrival[idx])
            #     last_door = None
            # who should go first?
            if last_door is None or last_door == 1:
                if exi1 and exi1[0][0] <= t:
                    answer[exi1[0][1]] = t
                    exi1.pop(0)
                    last_door = 1
                elif ent0 and ent0[0][0] <= t:
                    answer[ent0[0][1]] = t
                    ent0.pop(0)
                    last_door = 0
                else:
                    last_door = None
            else:
                if ent0 and ent0[0][0] <= t:
                    answer[ent0[0][1]] = t
                    ent0.pop(0)
                    last_door = 0
                elif exi1 and exi1[0][0] <= t:
                    answer[exi1[0][1]] = t
                    exi1.pop(0)
                    last_door = 1
                else:
                    last_door = None
            t += 1