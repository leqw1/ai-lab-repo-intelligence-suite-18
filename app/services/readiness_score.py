from __future__ import annotations

from dataclasses import dataclass

from app.services.repository_auditor import RepositoryAudit


@dataclass(frozen=True)
class ReadinessScore:
    score: int
    decision: str
    reasons: tuple[str, ...]


class ReadinessScorer:
    def score(self, audit: RepositoryAudit) -> ReadinessScore:
        score = 20
        reasons: list[str] = []
        if audit.files >= 35:
            score += 20
            reasons.append("repository surface is broad")
        if audit.python_files >= 12:
            score += 20
            reasons.append("implementation modules are present")
        if audit.tests >= 4:
            score += 20
            reasons.append("tests cover core behavior")
        if audit.docs >= 6:
            score += 15
            reasons.append("operator documentation is present")
        if audit.warnings:
            score -= 20
            reasons.extend(audit.warnings)
        decision = "ready" if score >= 85 else "continue_building"
        return ReadinessScore(score=max(0, min(score, 100)), decision=decision, reasons=tuple(reasons))
