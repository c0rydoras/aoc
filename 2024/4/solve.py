from pathlib import Path
import numpy as np

content = Path("input").read_text()

horizontal_lines = content.splitlines()

rows, cols = len(horizontal_lines), len(horizontal_lines[0])
arr = np.empty((rows, cols), dtype="U1")

for i, line in enumerate(horizontal_lines):
    arr[i, :] = list(line)

diags = []
for i in range(-rows + 1, cols):
    if (diag := arr.diagonal(i)).size > 0:
        diags.append(diag)

    flipped_diag = np.fliplr(arr).diagonal(i)
    if flipped_diag.size > 0:
        diags.append(flipped_diag)

vertical_lines = ["".join(line) for line in np.rot90(arr).tolist()]
diagonal_lines = ["".join(diag.tolist()) for diag in diags]

all_lines = [*horizontal_lines, *vertical_lines, *diagonal_lines]

print(sum([line.count("XMAS") + line.count("XMAS"[::-1]) for line in all_lines]))
