def is_good(line):
    for i in range(len(line) - 1):
        if (diff := line[i] - line[i + 1]) == 0 or abs(diff) > 3:
            return False
    return list(sorted(line)) == line or list(sorted(line, reverse=True)) == line


assert is_good([7, 6, 4, 2, 1])
assert not is_good([1, 2, 7, 8, 9])


numbers = [list(map(int, line.split())) for line in open("input")]
print(len(list(filter(is_good, numbers))))
