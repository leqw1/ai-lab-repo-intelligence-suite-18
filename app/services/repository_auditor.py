from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RepositoryAudit:
    files: int
    python_files: int
    tests: int
    docs: int
    warnings: tuple[str, ...]

    @property
    def ready_for_review(self) -> bool:
        return self.files >= 35 and self.tests >= 4 and self.docs >= 6 and not self.warnings


class RepositoryAuditor:
    def audit(self, root: Path) -> RepositoryAudit:
        files = [path for path in root.rglob("*") if path.is_file()]
        relative = [path.relative_to(root).as_posix() for path in files]
        tests = [path for path in relative if path.startswith("tests/") and path.endswith(".py")]
        docs = [path for path in relative if path.startswith("docs/") and path.endswith(".md")]
        warnings: list[str] = []
        if "README.md" not in relative:
            warnings.append("README missing")
        if ".env" in relative:
            warnings.append("committed .env is forbidden")
        return RepositoryAudit(
            files=len(relative),
            python_files=sum(path.endswith(".py") for path in relative),
            tests=len(tests),
            docs=len(docs),
            warnings=tuple(warnings),
        )
