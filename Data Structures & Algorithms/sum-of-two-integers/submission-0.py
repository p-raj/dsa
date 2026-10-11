class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        ans = 0
        place = 0

        while a != 0 or b != 0 or carry != 0:
            abit = a & 1
            bbit = b & 1

            sum_bit = abit ^ bbit ^ carry
            carry = (abit & bbit) | (abit & carry) | (bbit & carry)

            ans |= sum_bit << place

            a >>= 1
            b >>= 1
            place += 1

        return ans