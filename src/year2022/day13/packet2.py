from __future__ import annotations


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
        packet_list = file.read()
        packet_list = packet_list.replace("\n\n", "\n")
    packets = list(map(eval, packet_list.splitlines()))
    divider_packets = [[[2]], [[6]]]
    packets.extend(divider_packets)

    depths = map(depth, packets)
    max_depth = max(depths)
    for packet in packets:
        listify(packet, max_depth)
    packets.sort()

    print(*packets, sep = "\n")

    idx_prod = 1
    for packet in divider_packets:
        idx_prod *= packets.index(packet)+1
    print(idx_prod)


if __name__ == "__main__":
    main()
