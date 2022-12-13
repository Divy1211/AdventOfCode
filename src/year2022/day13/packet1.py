from __future__ import annotations

import regex


def depth(ls: list) -> int:
    ls_str = f"{ls}"
    max_open = 0
    open_count = 0
    for c in ls_str:
        if c == "[":
            open_count += 1
        elif c == "]":
            open_count -= 1
        max_open = max(open_count, max_open)
    return max_open

def listify(ls: list, depth: int):
    for i, ele in enumerate(ls):
        if isinstance(ele, list):
            listify(ele, depth-1)
        if isinstance(ele, int):
            for _ in range(depth-1):
                ele = [ele]
            ls[i] = ele


def main():
    with open("inp.txt") as file:
        packets = file.read()
    packet_pairs = list(map(lambda x: list(map(eval, x.splitlines())),  regex.split(r"(?:\r|\n|\r\n){2}", packets)))
    idx_sum = 0
    for i, (packet1, packet2) in enumerate(packet_pairs, 1):
        depth1 = depth(packet1)
        depth2 = depth(packet2)
        max_depth = max(depth1, depth2)
        listify(packet1, max_depth)
        listify(packet2, max_depth)
        if packet1 < packet2:
            idx_sum += i
    print(idx_sum)

if __name__ == "__main__":
    main()
