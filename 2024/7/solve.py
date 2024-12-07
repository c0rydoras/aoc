from __future__ import annotations

from pathlib import Path
import operator
from itertools import product
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Self

content = Path("input").read_text()


@dataclass
class Calibration:
    test_value: int
    numbers: list[int]

    @classmethod
    def from_str(cls, string: str) -> Self:
        test_value, unsplit_numbers = string.split(":")
        return cls(int(test_value), list(map(int, unsplit_numbers.split())))

    def is_valid(self) -> bool:
        for ops in product([operator.add, operator.mul], repeat=len(self.numbers) - 1):
            result = self.numbers[0]
            for op, num in zip(ops, self.numbers[1:]):
                result = op(result, num)
            if result == self.test_value:
                return True
        return False


calibrations = map(Calibration.from_str, content.splitlines())
print(sum(map(lambda x: x.test_value, filter(Calibration.is_valid, calibrations))))
