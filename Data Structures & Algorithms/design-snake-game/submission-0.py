from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_i = 0

        self.snake = deque([(0, 0)])
        self.occupied = {(0, 0)}

    def move(self, direction: str) -> int:
        r, c = self.snake[0]

        if direction == "R":
            c += 1
        elif direction == "L":
            c -= 1
        elif direction == "U":
            r -= 1
        elif direction == "D":
            r += 1

        nxt = (r, c)

        # 1. Wall collision
        if r < 0 or r >= self.height or c < 0 or c >= self.width:
            return -1

        # 2. Are we eating?
        eating = (
            self.food_i < len(self.food)
            and nxt == tuple(self.food[self.food_i])
        )

        # 3. If we're not eating, tail leaves first.
        if not eating:
            tail = self.snake.pop()
            self.occupied.remove(tail)

        # 4. Collision with remaining body.
        if nxt in self.occupied:
            return -1

        # 5. Add new head.
        self.snake.appendleft(nxt)
        self.occupied.add(nxt)

        # 6. Consume food.
        if eating:
            self.food_i += 1

        return len(self.snake) - 1