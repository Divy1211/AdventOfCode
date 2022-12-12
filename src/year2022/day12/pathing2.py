from typing import Sized


def find_locs(heigh_map: list[str]) -> tuple[int, int, int, int]:
    x, y, dest_x, dest_y = -1, -1, -1, -1
    for i, row in enumerate(heigh_map):
        if (j := row.find('S')) != -1:
            y, x = i, j
        if (j := row.find('E')) != -1:
            dest_y, dest_x = i, j
    return y, x, dest_y, dest_x


def out_of_bounds(i: int, ls: Sized) -> bool:
    return i < 0 or i >= len(ls)


def main():
    with open("inp.txt") as file:
        height_map = file.read().splitlines()

    start_y, start_x, dest_y, dest_x = find_locs(height_map)
    queue = [(dest_y, dest_x, 0, 'z')]
    queued = {(dest_y, dest_x)}
    height_map[start_y] = height_map[start_y].replace("S", "a")

    for y, x, dist, height in queue:
        for i, j in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
            if (
                out_of_bounds(i, height_map)
                or out_of_bounds(j, height_map[0])
                or (i, j) in queued
            ):
                continue
            to_height = height_map[i][j]
            if ord(to_height)-ord(height) < -1:
                continue
            if to_height == "a":
                print(dist+1)
                break
            queue.append((i, j, dist+1, to_height))
            queued.add((i, j))
        else:
            continue
        break

if __name__ == "__main__":
    main()
