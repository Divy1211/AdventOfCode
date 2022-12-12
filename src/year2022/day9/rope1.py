from typing import NamedTuple


class Move(NamedTuple):
    direction: str
    steps: int


class Position(NamedTuple):
    x: int
    y: int


def move_head(head: Position, move: Move) -> Position:
    if move.direction == "U":
        return Position(head.x, head.y + move.steps)
    if move.direction == "D":
        return Position(head.x, head.y - move.steps)
    if move.direction == "L":
        return Position(head.x - move.steps, head.y)
    if move.direction == "R":
        return Position(head.x + move.steps, head.y)


def main():
    with open("inp.txt") as file:
        move_list = file.read().splitlines()

    def read_move(move_: str) -> Move:
        direction, steps = move_.split(" ")
        return Move(direction, int(steps))

    moves = list(map(read_move, move_list))
    positions = {Position(0, 0)}
    head = Position(0, 0)
    tail = Position(0, 0)
    for move in moves:
        head = move_head(head, move)
        dx, dy = head.x - tail.x, head.y - tail.y
        while abs(dx) > 1 or abs(dy) > 1:
            tail = Position(
                tail.x + dx//abs(dx) if abs(dx) > 1 or abs(dx) == 1 and abs(dy) > 1 else tail.x,
                tail.y + dy//abs(dy) if abs(dy) > 1 or abs(dy) == 1 and abs(dx) > 1 else tail.y,
            )
            positions.add(tail)
            dx, dy = head.x - tail.x, head.y - tail.y

    print(len(positions))


if __name__ == "__main__":
    main()
