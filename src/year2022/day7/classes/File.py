from functools import cached_property


class File:
    def __init__(self, path: str, size: int):
        self.path = path
        self.size = size

    @cached_property
    def name(self):
        return self.path.split("/")[-1]

    def __repr__(self) -> str:
        return f"- {self.name:<15}{self.size:>15,}"
