from regex import regex


def main():
    with open("inp.txt") as file:
        crates = file.read()

    stack_list, move_list = regex.split(r"(?:\r|\n|\r\n){2}", crates)
    moves: list[str] = move_list.splitlines()
    *stack_rows, stack_indices = stack_list.splitlines()
    stacks: dict[int, list[str]] = {int(i): [] for i in stack_indices.strip().split("   ")}

    pattern_stack_row = r"(?:\[([A-Z])\]\s?|\s{4})"
    for row in stack_rows[::-1]:
        for i, match in enumerate(regex.finditer(pattern_stack_row, row)):
            if (crate := match.group(1)) is None:
                continue
            stacks[i+1].append(crate)

    pattern_move = r"move (\d+) from (\d+) to (\d+)"
    for move in moves:
        match = regex.match(pattern_move, move)
        count, from_, to = map(lambda x: int(match.group(x)), [1, 2, 3])
        stacks[from_], moving = stacks[from_][:-count], stacks[from_][-count:]
        stacks[to].extend(moving)

    print("".join(map(lambda x: x[-1], stacks.values())))


if __name__ == "__main__":
    main()
