from itertools import combinations


def is_good(line):
    def _is_good(_line):
        for i in range(len(_line) - 1):
            if (diff := _line[i] - _line[i + 1]) == 0 or abs(diff) > 3:
                return False
        return (
            list(sorted(_line)) == _line or list(sorted(_line, reverse=True)) == _line
        )

    return any(_is_good(list(li)) for li in combinations(line, len(line) - 1))


assert is_good([7, 6, 4, 2, 1])
assert not is_good([1, 2, 7, 8, 9])

numbers = [list(map(int, line.split())) for line in open("input")]
print(len(list(filter(is_good, numbers))))
