import re

from pathlib import Path
from operator import mul
from functools import reduce

content = Path("input").read_text()

pattern = r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"

findings = re.findall(pattern, content)

do = True

results = []

for finding in findings:
    if finding[0]:
        do = finding[0] == "do()"
    if finding[0] == "" and do:
        results.append(reduce(mul, map(int, finding[1:]), 1))
print(sum(results))
