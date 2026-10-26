class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        slots1.sort()
        slots2.sort()

        lft1, lft2 = 0, 0
        while lft1 < len(slots1) and lft2 < len(slots2):
            # the meeting slot of one person ends before the start
            # of the slot for the other person
            if slots1[lft1][1] < slots2[lft2][0]:
                lft1 += 1
            elif slots2[lft2][1] < slots1[lft1][0]:
                lft2 += 1
            else:
                # there is some overlap
                # P2 starts late
                # meeting can finish
                # before the P1 ends
                if (
                    slots1[lft1][0] <= slots2[lft2][0]
                    and duration <= slots1[lft1][1] - slots2[lft2][0]
                    and slots2[lft2][1] - slots2[lft2][0] >= duration
                ):
                    return [slots2[lft2][0], slots2[lft2][0] + duration]
                # P1 starts late
                # meeting can finish
                # before the P2 ends
                if (
                    slots2[lft2][0] <= slots1[lft1][0]
                    and duration <= slots2[lft2][1] - slots1[lft1][0]
                    and slots1[lft1][1] - slots1[lft1][0] >= duration
                ):
                    return [slots1[lft1][0], slots1[lft1][0] + duration]
                
                # there were overlaps
                # but duration didnt meet before the slot was over
                # for the other person
                if slots1[lft1][0] <= slots2[lft2][0]:
                    if slots1[lft1][1] < slots2[lft2][1]:
                        lft1 += 1
                    else:
                        lft2 += 1
                    continue
                if slots2[lft2][0] <= slots1[lft1][0]:
                    if slots2[lft2][1] < slots1[lft1][1]:
                        lft2 += 1
                    else:
                        lft1 += 1
        return []
