def sliding_window(stream: str, width: int):
    for i in range(len(stream)-width+1):
        yield i+width, stream[i:i+width]


def all_distinct(seq: str) -> bool:
    return len(set(seq)) == len(seq)


def main():
    with open("inp.txt") as file:
        stream = file.read()

    for end_idx, seq in sliding_window(stream, 4):
        if all_distinct(seq):
            break
    else:
        print("no start of packet marker found")
        return

    print(end_idx)


if __name__ == "__main__":
    main()
