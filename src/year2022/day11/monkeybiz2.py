from operator import attrgetter

from src.year2022.day11.inp import monkeys, Monkey


def main():
    Monkey.relief = False

    for _ in range(10_000):
        for monkey in monkeys:
            monkey.inspect()

    a1, a2 = sorted(monkeys, key = attrgetter('num_inspections'), reverse = True)[:2]
    print(a1.num_inspections * a2.num_inspections)


if __name__ == "__main__":
    main()
