from __future__ import annotations

from src.year2022.day7.classes.File import File
from functools import cached_property
from itertools import chain
from operator import attrgetter


class Directory:
    def __init__(self, path: str, parent: Directory | None):
        self.path = path
        self.parent = parent
        self.files: list[File] = []
        self.dirs: list[Directory] = []

    @cached_property
    def name(self):
        return self.path.split("/")[-1]

    @cached_property
    def size(self) -> int:
        return sum(map(attrgetter('size'), chain(self.files, self.dirs)))

    @cached_property
    def depth(self) -> int:
        if self.parent is None:
            return 0
        return 1 + self.parent.depth

    def __repr__(self):
        indent = "    "*self.depth
        lf = f"\n{indent}"
        return f'V {self.name+"/:":<15}{self.size:>15,}{lf}{lf.join(map(repr, chain(self.files, self.dirs)))}'
