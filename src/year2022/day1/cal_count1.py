import regex


def main():
    with open("inp.txt") as file:
        cal_counts = file.read()
    indiv_counts = regex.split(r"(?:\r|\n|\r\n){2}", cal_counts)
    indiv_cals = map(lambda counts: sum(map(int, counts.splitlines())), indiv_counts)
    print(max(indiv_cals))


if __name__ == "__main__":
    main()
