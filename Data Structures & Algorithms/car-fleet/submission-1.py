class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # s: o(n)
        pos_spd = [(pos, spd) for pos, spd in zip(position, speed)]
        # o(nln)
        pos_spd.sort(reverse=True)
        stack = []
        for idx, (p,s) in enumerate(pos_spd):
            t = (target - p)/s
            if not stack or (stack and stack[-1] < t):
                stack.append(t)
        return len(stack)
        