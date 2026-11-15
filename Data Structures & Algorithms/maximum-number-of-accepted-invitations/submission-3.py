class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        matched = [-1] * len(grid[0])

        def augment(boy, seen):
            for girl, allowed in enumerate(grid[boy]):
                if allowed and not seen[girl]:
                    seen[girl] = True
                    if matched[girl] == -1 or augment(matched[girl], seen):
                        matched[girl] = boy
                        return True
            return False

        return sum(augment(boy, [False] * len(matched)) for boy in range(len(grid)))
