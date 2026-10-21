class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0]+skill[-1]
        l=0
        r=len(skill)-1
        chemistry=0
        while l<r:
            if skill[l]+skill[r]!=target:
                return -1
            else:
                chemistry+=skill[r]*skill[l]
            l+=1
            r-=1
        return(chemistry)



