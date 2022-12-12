interesting_cycles = iter([20, 60, 100, 140, 180, 220])
interesting_cycle = next(interesting_cycles)
signal_strenghts = {}


def note_value(reg_x: int, preg_x, cycle: int):
    global interesting_cycle
    if cycle == interesting_cycle:
        signal_strenghts[interesting_cycle] = interesting_cycle*reg_x
        interesting_cycle = next(interesting_cycles)
    if cycle > interesting_cycle:
        signal_strenghts[interesting_cycle] = interesting_cycle*preg_x
        interesting_cycle = next(interesting_cycles)


def main():
    with open("inp.txt") as file:
        instructions = file.read().splitlines()

    cycle = 1
    preg_x = reg_x = 1
    for instruction in instructions:
        try:
            note_value(reg_x, preg_x, cycle)
        except StopIteration:
            break
        preg_x = reg_x
        if instruction.startswith("noop"):
            cycle += 1
            continue
        val = int(instruction.removeprefix("addx "))
        cycle += 2
        reg_x += val

    print(sum(signal_strenghts.values()))


if __name__ == "__main__":
    main()
