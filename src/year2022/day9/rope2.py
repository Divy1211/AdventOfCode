from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int


class Move(NamedTuple):
    direction: str
    steps: int


class Knot:
    def __init__(self, length = 2):
        self.pos = Position(0, 0)
        self.positions = {self.pos}
        self.tail = None
        if length > 1:
            self.tail = Knot(length-1)
        self.length = length

    def move(self, move: Move):
        if move.direction == "U":
            self.pos = Position(self.pos.x, self.pos.y + move.steps)
        if move.direction == "D":
            self.pos = Position(self.pos.x, self.pos.y - move.steps)
        if move.direction == "L":
            self.pos = Position(self.pos.x - move.steps, self.pos.y)
        if move.direction == "R":
            self.pos = Position(self.pos.x + move.steps, self.pos.y)

        self.move_tail()

    def move_tail(self):
        if self.tail is None:
            return

        head = self.pos
        tail = self.tail.pos

        dx, dy = head.x - tail.x, head.y - tail.y
        while abs(dx) > 1 or abs(dy) > 1:
            tail = Position(
                tail.x + dx//abs(dx) if abs(dx) > 1 or abs(dx) == 1 and abs(dy) > 1 else tail.x,
                tail.y + dy//abs(dy) if abs(dy) > 1 or abs(dy) == 1 and abs(dx) > 1 else tail.y,
            )
            self.tail.positions.add(tail)
            self.tail.pos = tail
            self.tail.move_tail()
            dx, dy = head.x - tail.x, head.y - tail.y


    def __getitem__(self, item: int) -> 'Knot':
        if item == 0:
            return self
        return self.tail[item-1]


def main():
    with open("inp.txt") as file:
        move_list = file.read().splitlines()

    def read_move(move_: str) -> Move:
        direction, steps = move_.split(" ")
        return Move(direction, int(steps))

    moves = list(map(read_move, move_list))
    head = Knot(10)
    for move in moves:
        head.move(move)

    print(len(head[9].positions))


if __name__ == "__main__":
    main()