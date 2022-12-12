import numpy as np

LOWERCASE_OFFSET = ord('a')-1
UPPERCASE_OFFSET = ord('A')-1-26


def main():
    with open("inp.txt") as file:
        rucksack_item_list = file.read()

    def find_common_and_priority(grp_rucksacks: list[str]) -> int:
        rucksack1, rucksack2, rucksack3 = map(set, grp_rucksacks)
        common_item = (rucksack1 & rucksack2 & rucksack3).pop()

        if common_item.islower():
            return ord(common_item)-LOWERCASE_OFFSET
        return ord(common_item)-UPPERCASE_OFFSET

    rucksacks = rucksack_item_list.splitlines()
    elf_grps = np.split(np.array(rucksacks, dtype = str), len(rucksacks)//3)
    print(sum(map(find_common_and_priority, elf_grps)))


if __name__ == "__main__":
    main()
