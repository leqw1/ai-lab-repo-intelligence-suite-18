from __future__ import annotations

from app.services.readiness_score import ReadinessScore


class ReportBuilder:
    def markdown(self, name: str, score: ReadinessScore) -> str:
        reasons = "\n".join(f"- {reason}" for reason in score.reasons) or "- no reasons"
        return (
            f"# {name} Report\n\n"
            f"Decision: {score.decision}\n\n"
            f"Score: {score.score}\n\n"
            f"Reasons:\n{reasons}\n"
        )


DEFAULT_REPORT_TITLE = "Ai Lab Repo Intelligence Suite 18"
