from copy import deepcopy
from dataclasses import dataclass
import re



@dataclass
class Knot:
    x: int
    y: int

    def __hash__(self):
        return hash(str(self))

@dataclass
class Rope:
    head: Knot = Knot(0, 0)
    tail: Knot = Knot(0, 0)
    last_instruction: str = ""
    visited_tail_positions = []

    def __post_init__(self):
        self.INSTRUCTIONS_MAPPING = {
            'U': self._move_up,
            'D': self._move_down,
            'L': self._move_left,
            'R': self._move_right,
        }
        self.visited_tail_positions.append(deepcopy(self.tail))

    def _knots_close(self):
        if abs(self.head.x - self.tail.x) >= 2:
            return False
        if abs(self.head.y - self.tail.y) >= 2:
            return False
        return True

    def _move_tail(self):
        if self._knots_close():
            return
        if self.last_instruction == "R":
            self.tail.x = self.head.x - 1
            self.tail.y = self.head.y
        if self.last_instruction == "L":
            self.tail.x = self.head.x + 1
            self.tail.y = self.head.y
        if self.last_instruction == "U":
            self.tail.y = self.head.y - 1
            self.tail.x = self.head.x
        if self.last_instruction == "D":
            self.tail.y = self.head.y + 1
            self.tail.x = self.head.x
        self.visited_tail_positions.append(deepcopy(self.tail))

    def _move_right(self):
        self.head.x += 1

    def _move_left(self):
        self.head.x -= 1

    def _move_up(self):
        self.head.y += 1

    def _move_down(self):
        self.head.y -= 1

    def move(self, direction, distance):
        self.last_instruction = direction
        for _ in range(distance):
            self.INSTRUCTIONS_MAPPING[direction]()
            self._move_tail()


if __name__ == "__main__":
    rope = Rope(
        head=Knot(0,0),
        tail=Knot(0,0)
    )

    with open('puzzle9_input') as input:
        for line in input:
            direction = re.search('\w+', line)[0]
            distance = re.search('\d+', line)[0]
            rope.move(
                direction=direction,
                distance=int(distance)
            )
            print(direction, distance, rope.head, rope.tail)
    print(len(set(rope.visited_tail_positions)))
