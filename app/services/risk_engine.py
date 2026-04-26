from __future__ import annotations

from app.core.domain import RiskReport
from app.services.project_board import ProjectBoard


class RiskEngine:
    def evaluate_board(self, board: ProjectBoard) -> RiskReport:
        blockers: list[str] = []
        warnings: list[str] = []
        if board.owner_decision_count() > 0:
            warnings.append("owner approval pending")
        score = 0.1 + 0.1 * len(warnings) + 0.4 * len(blockers)
        return RiskReport(score=min(score, 1.0), blockers=tuple(blockers), warnings=tuple(warnings))
