from collections import deque

class Solution:
    def timeTaken(
        self,
        arrival: List[int],
        state: List[int]
    ) -> List[int]:

        n = len(arrival)
        answer = [0] * n

        enter = deque()
        exit = deque()

        i = 0
        t = 0
        prev = -1  # -1: idle, 0: enter, 1: exit

        while i < n or enter or exit:

            # No one waiting? Jump to the next arrival.
            if not enter and not exit and i < n:
                if t < arrival[i]:
                    t = arrival[i]
                    prev = -1

            # Add everyone who has arrived by time t.
            while i < n and arrival[i] <= t:
                if state[i] == 0:
                    enter.append(i)
                else:
                    exit.append(i)
                i += 1

            # Determine preferred direction.
            # Idle door gives priority to exit.
            preferred = 1 if prev == -1 else prev

            # Select the next person.
            if preferred == 1:
                if exit:
                    person = exit.popleft()
                else:
                    person = enter.popleft()
            else:
                if enter:
                    person = enter.popleft()
                else:
                    person = exit.popleft()

            # Cross the door.
            answer[person] = t
            prev = state[person]
            t += 1

        return answer