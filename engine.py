from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)


    def can_fire(self, rule: Rule) -> bool:                         
        return (
            all(a in self.facts for a in rule.antecedents)
            and rule.consequent not in self.facts
        )

    def run(self) -> None:
        while True:

            fireable = [r for r in self.rules if self.can_fire(r)]
            if not fireable:
                break

            fireable.sort(key=lambda r: r.priority, reverse=True)
            rule = fireable[0]

            self.facts.add(rule.consequent)
            self.trace.append({
                "rule": rule.name,
                "added": rule.consequent,
                "antecedents": rule.antecedents
            })

    def conclusions(self) -> Dict[str, List[str]]:
        recommendations = []
        specs = []
        facts = []

        for fact in self.facts:
            if fact.startswith("recommend:"):
                recommendations.append(fact.split("recommend:", 1)[1])
            elif fact.startswith("spec:"):
                specs.append(fact.split("spec:", 1)[1])
            else:
                facts.append(fact)

        return {
            "recommendations": recommendations,
            "specifications": specs,
            "facts": facts
        }
  