def main():
    with open("inp.txt") as file:
        assignment_lists = file.read().splitlines()

    def get_assignment_ranges(pair_assignment: str) -> tuple[tuple[int, int], tuple[int, int]]:
        assign1, assign2 = pair_assignment.split(",")
        (start1, end1), (start2, end2) = map(int, assign1.split("-")), map(int, assign2.split("-"))
        return (start1, end1), (start2, end2)

    assignments = map(get_assignment_ranges, assignment_lists)
    overlap = 0

    def overlaps(assign1: tuple[int, int], assign2: tuple[int, int]) -> bool:
        (start1, end1), (start2, end2) = assign1, assign2
        return start2 <= end1 and start1 <= end2

    for assignm1, assignm2 in assignments:
        if overlaps(assignm1, assignm2):
            overlap += 1

    print(overlap)


if __name__ == "__main__":
    main()
