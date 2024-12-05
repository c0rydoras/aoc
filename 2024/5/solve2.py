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

    def order(self, rules: list[Rule]):
        # some sort of sorting go brrr
        while True:
            for rule in rules:
                if rule.before in self.updates and rule.after in self.updates:
                    before_idx = self.updates.index(rule.before)
                    after_idx = self.updates.index(rule.after)

                    if before_idx > after_idx:
                        self.updates.remove(rule.before)
                        self.updates.insert(after_idx, rule.before)

            if self.satisfies_rules(rules):
                return self


content = Path("input").read_text()

lines = content.splitlines()
rules = [Rule(*map(int, line.split("|"))) for line in lines if "|" in line]
updates = [Update(list(map(int, line.split(",")))) for line in lines if "," in line]


updates_to_check = [update for update in updates if not update.satisfies_rules(rules)]
ordered_updates = list(filter(bool, [u.order(rules) for u in updates_to_check]))

assert all(u.satisfies_rules(rules) for u in ordered_updates)

print(sum([u.middle for u in ordered_updates]))
