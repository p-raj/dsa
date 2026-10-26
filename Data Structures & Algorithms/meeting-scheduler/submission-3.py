class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        slots1.sort()
        slots2.sort()

        i = j = 0

        while i < len(slots1) and j < len(slots2):
            a_start, a_end = slots1[i]
            b_start, b_end = slots2[j]

            # Intersection of the current intervals
            start = max(a_start, b_start)
            end = min(a_end, b_end)

            if end - start >= duration:
                return [start, start + duration]

            # Discard the interval ending earlier
            if a_end <= b_end:
                i += 1
            else:
                j += 1

        return []