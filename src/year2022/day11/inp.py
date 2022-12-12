from __future__ import annotations

from typing import Callable

import numpy as np

ItemList = np.ndarray[np.uint64]


class Monkey:
    relief = True

    def __init__(
        self,
        starting_items: ItemList,
        op: Callable[[ItemList], ItemList],
        test: Callable[[ItemList], np.ndarray[np.bool_]],
    ):
        self.items = starting_items
        self.op = op
        self.test = test
        self.throw_to: tuple[Monkey, Monkey] = (None, None)
        self.num_inspections = 0

    def inspect(self):
        self.num_inspections += len(self.items)
        new_lvls = self.op(self.items) % 9699690
        if Monkey.relief:
            new_lvls //= 3
        test = self.test(new_lvls)
        self.throw_to[0].items = np.append(self.throw_to[0].items, new_lvls[~test])
        self.throw_to[1].items = np.append(self.throw_to[1].items, new_lvls[test])
        self.items = np.array([], dtype = np.uint64)


monkeys = [
    Monkey(
        np.array([54, 61, 97, 63, 74], dtype=np.uint64),
        lambda old: old * 7,
        lambda x: x % 17 == 0
    ),
    Monkey(
        np.array([61, 70, 97, 64, 99, 83, 52, 87], dtype=np.uint64),
        lambda old: old + 8,
        lambda x: x % 2 == 0
    ),
    Monkey(
        np.array([60, 67, 80, 65], dtype=np.uint64),
        lambda old: old * 13,
        lambda x: x % 5 == 0
    ),
    Monkey(
        np.array([61, 70, 76, 69, 82, 56], dtype=np.uint64),
        lambda old: old + 7,
        lambda x: x % 3 == 0
    ),
    Monkey(
        np.array([79, 98], dtype=np.uint64),
        lambda old: old + 2,
        lambda x: x % 7 == 0
    ),
    Monkey(
        np.array([72, 79, 55], dtype=np.uint64),
        lambda old: old + 1,
        lambda x: x % 13 == 0
    ),
    Monkey(
        np.array([63], dtype=np.uint64),
        lambda old: old + 4,
        lambda x: x % 19 == 0
    ),
    Monkey(
        np.array([72, 51, 93, 63, 80, 86, 81], dtype=np.uint64),
        lambda old: old * old,
        lambda x: x % 11 == 0
    ),
]

monkeys[0].throw_to = (monkeys[3], monkeys[5])
monkeys[1].throw_to = (monkeys[6], monkeys[7])
monkeys[2].throw_to = (monkeys[6], monkeys[1])
monkeys[3].throw_to = (monkeys[2], monkeys[5])
monkeys[4].throw_to = (monkeys[3], monkeys[0])
monkeys[5].throw_to = (monkeys[1], monkeys[2])
monkeys[6].throw_to = (monkeys[4], monkeys[7])
monkeys[7].throw_to = (monkeys[4], monkeys[0])
