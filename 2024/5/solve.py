from pathlib import Path
from dataclasses import dataclass


@dataclass
class Rule:
    before: int
    after: int


@dataclass
class Update:
    updates: list[int]

    def satisfies_rule(self, rule: Rule):
        if rule.before not in self.updates and rule.after not in self.updates:
            return True

        if rule.before not in self.updates or rule.after not in self.updates:
            return True

        return self.updates.index(rule.before) < self.updates.index(rule.after)

    def satisfies_rules(self, rules: list[Rule]):
        return all(self.satisfies_rule(rule) for rule in rules)

    @property
    def middle(self) -> int:
        return self.updates[len(self.updates) // 2]


content = Path("input").read_text()

lines = content.splitlines()
rules = [Rule(*map(int, line.split("|"))) for line in lines if "|" in line]
updates = [Update(list(map(int, line.split(",")))) for line in lines if "," in line]

print(sum([update.middle for update in updates if update.satisfies_rules(rules)]))
