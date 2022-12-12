import numpy as np


def compute_scenic_score(tree_map: np.ndarray[np.ndarray[int]]) -> np.ndarray[np.ndarray[int]]:
    row_dim = (1, tree_map.shape[1])
    scenic_score = np.full(row_dim, 0)
    for i, tree_row in enumerate(tree_map[1:], 1):
        upper_rows = tree_map[:i]
        is_ge = tree_row > upper_rows
        for row, prow in zip(is_ge[-2::-1], is_ge[::-1]):
            row[:] = row & prow
        adj = np.where(is_ge[0], 0, 1)
        scenic_score = np.r_[scenic_score, adj + np.sum(is_ge, axis = 0).reshape(row_dim)]
    return scenic_score


def main():
    with open("inp.txt") as file:
        tree_map = np.array(list(map(lambda x: list(map(int, x)), file.read().splitlines())))

    up_scenic_score = compute_scenic_score(tree_map)
    down_scenic_score = compute_scenic_score(tree_map[::-1])[::-1]
    left_scenic_score = compute_scenic_score(tree_map.T).T
    right_scenic_score = compute_scenic_score(tree_map.T[::-1])[::-1].T

    total_scenic_score = up_scenic_score * down_scenic_score * left_scenic_score * right_scenic_score
    print(np.max(total_scenic_score))


if __name__ == "__main__":
    main()
