from __future__ import annotations

from operator import attrgetter

import regex

from src.year2022.day7.classes.Directory import Directory
from src.year2022.day7.classes.File import File


def main():
    with open("inp.txt") as file:
        output = file.read().splitlines()

    cwd_path = ['/']
    root = cwd = Directory("/", None)
    all_dirs: list[Directory] = [root]

    def set_cwd(command: str):
        nonlocal cwd_path, cwd
        if not (match_ := regex.match(r"^\$ cd ([\w.]+)", command)):
            return

        if (directory := match_.group(1)) == "..":
            cwd_path.pop()
            cwd = cwd.parent
        else:
            cwd_path.append(directory)
            cwd = Directory("/".join(cwd_path)[1:], cwd)
            cwd.parent.dirs.append(cwd)
            all_dirs.append(cwd)

    for cmd in output:
        if cmd.startswith("$"):
            set_cwd(cmd)
            continue
        if match := regex.match(r"(\d+) ([\w.]+)", cmd):
            cwd.files.append(File(f'{"/".join(cwd_path)[1:]}/{match.group(2)}', int(match.group(1))))

    print(sum(filter(lambda size: size < 100_000, map(attrgetter('size'), all_dirs))))


if __name__ == "__main__":
    main()
