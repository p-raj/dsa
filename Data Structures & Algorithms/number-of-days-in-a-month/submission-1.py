class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        leap_ = 0
        if ((year % 4) == 0 and (year % 100) != 0) or ((year % 400) == 0 and (year % 100) != 0):
            leap_ = 1

        if month <= 7:
            if month % 2:
                return 31
            if month == 2:
                return 28 + leap_
            return 30
        else:
            if month % 2:
                return 30
            return 31
