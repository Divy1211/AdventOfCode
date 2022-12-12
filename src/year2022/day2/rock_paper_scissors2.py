usage_point_table = {
    "A": 1,
    "B": 2,
    "C": 3,
}

vs_point_table = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

shape_by_outcome = {
    "A": {"X": "C", "Y": "A", "Z": "B"},
    "B": {"X": "A", "Y": "B", "Z": "C"},
    "C": {"X": "B", "Y": "C", "Z": "A"},
}


def main():
    with open("inp.txt") as file:
        strat_guide_sheet = file.read()

    strat_guide = map(lambda x: x.split(" "), strat_guide_sheet.splitlines())

    total_points = 0

    for opp, outcome in strat_guide:
        shape = shape_by_outcome[opp][outcome]
        total_points += vs_point_table[outcome] + usage_point_table[shape]

    print(total_points)


if __name__ == "__main__":
    main()
