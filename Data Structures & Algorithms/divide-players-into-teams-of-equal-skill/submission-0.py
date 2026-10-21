class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot = sum(skill)
        if tot % 2:
            return -1
        skill.sort()
        lft = 0
        rgt = len(skill) - 1

        sm_mul_ = 0
        sm_ = 0
        while lft < rgt:
            team = (skill[lft], skill[rgt])
            if sm_ == 0:
                sm_ = sum(team)
            elif sm_ != sum(team):
                return -1
            mul_ = skill[lft]* skill[rgt]
            sm_mul_ += mul_
            lft += 1
            rgt -= 1
        return sm_mul_