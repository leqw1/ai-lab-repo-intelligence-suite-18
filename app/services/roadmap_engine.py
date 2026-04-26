from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RoadmapItem:
    title: str
    priority: str
    evidence: str

    def as_dict(self) -> dict[str, str]:
        return {"title": self.title, "priority": self.priority, "evidence": self.evidence}


class RoadmapEngine:
    def build(self, findings: list[str]) -> list[RoadmapItem]:
        if not findings:
            return [RoadmapItem("Keep improving test coverage", "medium", "no blockers found")]
        return [
            RoadmapItem(f"Fix {finding}", "high" if index == 0 else "medium", "automated audit")
            for index, finding in enumerate(findings[:8])
        ]
