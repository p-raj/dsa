class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        # A century year is a leap year only if divisible by 400.
        leap_ = 0
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            leap_ = 1

        # January through July: odd months have 31 days.
        if month <= 7:
            if month % 2:
                return 31
            if month == 2:
                return 28 + leap_
            return 30

        # August through December: even months have 31 days.
        else:
            if month % 2:
                return 30
            return 31