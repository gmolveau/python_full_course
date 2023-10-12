import re

text_input = """a
    b
        c
        d
    e
f
"""

text_output = """1. a
    1.1. b
        1.1.1. c
        1.1.2. d
    1.2. e
2. f
"""

IGNORE_PATTERN = "//"
DEPTH_PATTERN = " " * 4  # 4 spaces


class Numerotation:
    def __init__(self) -> None:
        self._positions = [0]

    def update(self, depth):
        max_index = len(self._positions) - 1
        if depth > max_index:
            # to avoid the case with an identation level error
            # for example jumping from 2. to 2.1.1.
            # we keep adding depths
            for _ in range(depth - max_index):
                self._positions.append(1)
        elif depth == max_index:
            # we are still at the deepest level so we increment
            self._positions[depth] += 1
        else:
            # we are one or more level higher, we increment this level
            self._positions[depth] += 1
            # and delete the sub levels
            for _ in range(max_index - depth):
                self._positions.pop()

    def __str__(self):
        # we convert the list of int to a list of string first
        # then separate it with a dot and add a final dot
        o = ".".join(map(str, self._positions))
        return f"{o}."


def main():
    lines = text_input.splitlines()
    numerotation = Numerotation()
    output = []
    for line in lines:
        print(numerotation)
        if not line:
            continue
        if line.startswith(IGNORE_PATTERN):
            output.append(f"{line}\n")
            continue
        if not line.startswith(DEPTH_PATTERN):
            depth = 0
            numerotation.update(depth)
            output.append(f"{numerotation} {line}\n")
            continue
        depth = len(re.findall(DEPTH_PATTERN, line))
        if depth > 0:
            numerotation.update(depth)
            # we need to inject the numerotation after the depth patterns
            index_after_patterns = depth * len(DEPTH_PATTERN)
            o_line = f"{line[:index_after_patterns]}{numerotation} {line[index_after_patterns:]}\n"
            output.append(o_line)
            continue
    return "".join(output)


if __name__ == "__main__":
    o = main()
    assert o == text_output
