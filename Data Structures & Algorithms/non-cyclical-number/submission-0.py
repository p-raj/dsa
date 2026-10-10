class Solution:
    def get_digits(self, n: int) -> list[int]:
        digs = []
        while n > 0:
            ld = n % 10
            digs.append(ld)
            n -= ld
            n //= 10
        return digs

    def isHappy(self, n: int) -> bool:
        seen = dict()
        while True:
            if n not in seen:
                seen[n] = 0
            seen[n] += 1
            if seen[n] > 2:
                return False
            digs = self.get_digits(n)
            n = int(sum(map(lambda x: x**2, digs)))
            if n == 1:
                return True
