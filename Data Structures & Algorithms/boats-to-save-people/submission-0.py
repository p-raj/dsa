class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lft = 0
        rgt = len(people) - 1
        crossed = 0
        boats = 0
        while crossed != len(people):
            if people[lft] + people[rgt] > limit:
                crossed += 1
                rgt -= 1
            else:
                crossed += 2
                lft += 1
                rgt -= 1
            boats += 1
        return boats