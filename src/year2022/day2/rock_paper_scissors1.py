usage_point_table = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

vs_point_table = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}


def main():
    with open("inp.txt") as file:
        strat_guide_sheet = file.read()

    strat_guide = map(lambda x: x.split(" "), strat_guide_sheet.splitlines())

    total_points = 0

    for opp, resp in strat_guide:
        total_points += vs_point_table[opp][resp] + usage_point_table[resp]

    print(total_points)


if __name__ == "__main__":
    main()
