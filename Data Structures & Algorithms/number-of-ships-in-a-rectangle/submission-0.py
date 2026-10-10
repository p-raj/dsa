# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point:
# def __init__(self, x: int, y: int):
# self.x = x
# self.y = y
import math


class Solution:
    def countShips(
        self, sea: "Sea", topRight: "Point", bottomLeft: "Point"
    ) -> int:

        stack = [(topRight, bottomLeft)]
        res = 0

        while stack:
            t_r, b_l = stack.pop()

            # 1. Reject invalid rectangles.
            if b_l.x > t_r.x or b_l.y > t_r.y:
                continue

            # 2. Prune empty rectangles.
            if not sea.hasShips(t_r, b_l):
                continue

            # 3. Single integer point containing a ship.
            if t_r.x == b_l.x and t_r.y == b_l.y:
                res += 1
                continue

            # 4. Integer midpoint.
            minx, maxx = b_l.x, t_r.x
            miny, maxy = b_l.y, t_r.y

            midx = (minx + maxx) // 2
            midy = (miny + maxy) // 2

            # 5. Four non-overlapping quadrants.
            q1 = (
                Point(midx, midy),
                Point(minx, miny),
            )

            q2 = (
                Point(maxx, midy),
                Point(midx + 1, miny),
            )

            q3 = (
                Point(maxx, maxy),
                Point(midx + 1, midy + 1),
            )

            q4 = (
                Point(midx, maxy),
                Point(minx, midy + 1),
            )

            stack.extend([q1, q2, q3, q4])

        return res