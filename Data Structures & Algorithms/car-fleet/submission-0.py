class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # s: o(n)
        pos_spd = [(pos, spd) for pos, spd in zip(position, speed)]
        # o(nln)
        pos_spd.sort()
        count = 0
        while pos_spd:
            count += 1
            p, s = pos_spd.pop()
            tim = (target - p)/s
            print(count, " > ", tim, p, s)
            while pos_spd:
                p2, s2 = pos_spd[-1]
                tim2 = (target-p2)/s2
                print(tim, tim2, tim <= tim2, p2, s2)
                if tim >= tim2:
                    pos_spd.pop()
                else:
                    break
        return count
