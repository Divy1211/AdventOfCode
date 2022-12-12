LOWERCASE_OFFSET = ord('a')-1
UPPERCASE_OFFSET = ord('A')-1-26


def main():
    with open("inp.txt") as file:
        rucksack_item_list = file.read()

    def find_common_and_priority(string: str) -> int:
        compartment_size = len(string)//2
        compartment1, compartment2 = set(string[:compartment_size]), set(string[compartment_size:])
        common_item = (compartment1 & compartment2).pop()

        if common_item.islower():
            return ord(common_item)-LOWERCASE_OFFSET
        return ord(common_item)-UPPERCASE_OFFSET

    print(sum(map(find_common_and_priority, rucksack_item_list.splitlines())))


if __name__ == "__main__":
    main()
