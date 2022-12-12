img = [list("."*40) for _ in range(6)]


def draw(reg_x: int, cycle: int):
    global img
    j = (cycle-1)%40
    i = (cycle-1)//40
    if reg_x - 1 <= j <= reg_x + 1:
        img[i][j] = "#"


def main():
    with open("inp.txt") as file:
        instructions = file.read().splitlines()

    cycle = 1
    reg_x = 1
    for instruction in instructions:
        draw(reg_x, cycle)
        if instruction.startswith("noop"):
            cycle += 1
            continue
        cycle += 1
        draw(reg_x, cycle)
        val = int(instruction.removeprefix("addx "))
        cycle += 1
        reg_x += val

    print("\n".join(map("".join, img)))  # EKRHEPUZ


if __name__ == "__main__":
    main()
