import numpy as np


def compute_running_max(tree_map: np.ndarray[np.ndarray[int]]) -> np.ndarray[np.ndarray[bool]]:
    row_dim = (1, tree_map.shape[1])
    running_max = np.full(row_dim, -1)
    for tree_row in tree_map:
        running_max = np.r_[running_max, np.where(tree_row > running_max[-1], tree_row, running_max[-1]).reshape(row_dim)]
    return running_max


def main():
    with open("inp.txt") as file:
        tree_map = np.array(list(map(lambda x: list(map(int, x)), file.read().splitlines())))

    up_running_max = compute_running_max(tree_map)
    down_running_max = compute_running_max(tree_map[::-1])[::-1]
    left_running_max = compute_running_max(tree_map.T).T
    right_running_max = compute_running_max(tree_map.T[::-1])[::-1].T

    visibile = (
        (tree_map > up_running_max[:-1])
        | (tree_map > down_running_max[1:])
        | (tree_map > left_running_max[:, :-1])
        | (tree_map > right_running_max[:, 1:])
    )
    print(np.sum(visibile))


if __name__ == "__main__":
    main()
