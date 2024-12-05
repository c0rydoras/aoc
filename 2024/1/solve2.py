from pathlib import Path

content = Path("input").read_text().split()


def to_ints(stuff: list[str]) -> list[int]:
    return [int(n) for n in stuff]


line_1 = to_ints(content[::2])
line_2 = to_ints(content[1::2])

similarity_score = 0
for number in line_1:
    similarity_score += number * line_2.count(number)

print(similarity_score)
