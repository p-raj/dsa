class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        class BT:
            def __init__(self, x):
                self.x = x
                self.res = []

            def is_soln(self, state):
                return len(state) == len(self.x)

            def process(self, state):
                self.res.append([str(self.x[i]) for i in state])

            def candidates(self, state):
                return [i for i in range(len(self.x)) if i not in set(state)]

            def move(self, state, c):
                state.append(c)

            def undo(self, state, c):
                state.pop()

            def bt(self, state):
                if self.is_soln(state):
                    self.process(state)
                else:
                    for c in self.candidates(state):
                        self.move(state, c)
                        self.bt(state)
                        self.undo(state, c)

            def generate(self):
                self.bt([])
                return max(map(int, ["".join(n) for n in self.res]))

        def get_first_digit(n):
            return int(str(n)[0])

        N = {i: [] for i in range(10)}
        for num in nums:
            d = get_first_digit(num)
            N[d].append(num)

        res = ""
        for i in range(9, -1, -1):
            if N[i]:
                res += str(BT(N[i]).generate())
        return res
