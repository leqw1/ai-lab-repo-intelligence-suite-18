from __future__ import annotations

from pathlib import Path

from app.services.readiness_score import ReadinessScorer
from app.services.repository_auditor import RepositoryAuditor


def main() -> int:
    audit = RepositoryAuditor().audit(Path.cwd())
    score = ReadinessScorer().score(audit)
    print(f"readiness={score.score} decision={score.decision}")
    return 0 if score.score >= 85 else 1


if __name__ == "__main__":
    raise SystemExit(main())
