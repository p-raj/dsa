class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        ans = 0
        mask = 0xFFFFFFFF
        a &= mask
        b &= mask

        for i in range(32):
            abit = a & 1
            bbit = b & 1

            s = abit ^ bbit ^ carry
            carry = (abit & bbit) | (abit & carry) | (bbit & carry)

            ans |= s << i

            a >>= 1
            b >>= 1
        if ans > 0x7FFFFFFF:
            ans = ~(ans ^ mask)
        return ans