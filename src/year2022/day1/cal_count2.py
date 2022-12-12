import regex


def main():
    with open("inp.txt") as file:
        cal_counts = file.read()
    indiv_counts = regex.split(r"(?:\r|\n|\r\n){2}", cal_counts)
    indiv_cals = map(lambda counts: sum(map(int, counts.splitlines())), indiv_counts)

    max3 = [-1, -1, -1]

    for cal in indiv_cals:
        for i, top in enumerate(max3):
            if cal <= top:
                continue
            max3[i+1:] = max3[i:-1]
            max3[i] = cal
            break

    print(sum(max3))


if __name__ == "__main__":
    main()
