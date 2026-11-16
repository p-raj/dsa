class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count = [abs(st-si) for st, si in zip(students, seats)]
        return sum(count)
