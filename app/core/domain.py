from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Agent:
    role: str
    responsibility: str
    current_focus: str

    def as_dict(self) -> dict[str, str]:
        return {
            "role": self.role,
            "responsibility": self.responsibility,
            "current_focus": self.current_focus,
        }


@dataclass(frozen=True)
class ProductProject:
    name: str
    stage: str
    progress: int
    owner_decision_required: bool

    def as_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "stage": self.stage,
            "progress": self.progress,
            "owner_decision_required": self.owner_decision_required,
        }


@dataclass(frozen=True)
class RiskReport:
    score: float
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "score": self.score,
            "blockers": list(self.blockers),
            "warnings": list(self.warnings),
        }
