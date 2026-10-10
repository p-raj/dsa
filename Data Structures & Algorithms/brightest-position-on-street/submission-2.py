from bisect import bisect_left, bisect_right

class Solution:
    def brightestPosition(self, lights):
        rng = [(o - r, o + r) for o, r in lights]

        starts = sorted(left for left, right in rng)
        ends = sorted(right for left, right in rng)

        best_brightness = 0
        best_position = None

        # Only start positions can introduce a new maximum.
        for x in starts:
            started = bisect_right(starts, x)
            ended = bisect_left(ends, x)

            brightness = started - ended

            if brightness > best_brightness:
                best_brightness = brightness
                best_position = x

        return best_position