from __future__ import annotations

from dataclasses import dataclass

from app.core.domain import ProductProject


@dataclass(frozen=True)
class ProjectBoard:
    projects: tuple[ProductProject, ...]

    @classmethod
    def demo(cls) -> "ProjectBoard":
        return cls(
            projects=(
                ProductProject(
                    name="production-suite",
                    stage="architecture",
                    progress=42,
                    owner_decision_required=False,
                ),
                ProductProject(
                    name="approval-inbox",
                    stage="approval",
                    progress=99,
                    owner_decision_required=True,
                ),
            )
        )

    def owner_decision_count(self) -> int:
        return sum(1 for project in self.projects if project.owner_decision_required)
