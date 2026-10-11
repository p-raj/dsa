class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        ans = 0

        a &= 0xffff
        b &= 0xffff

        for i in range(16):
            abit = a & 1
            bbit = b & 1

            s = abit ^ bbit ^ carry
            carry = (abit & bbit) | (abit & carry) | (bbit & carry)

            ans |= s << i

            a >>= 1
            b >>= 1