from __future__ import annotations

from dataclasses import dataclass

from app.core.domain import Agent


@dataclass(frozen=True)
class AgentCompany:
    agents: tuple[Agent, ...]

    @classmethod
    def default(cls) -> "AgentCompany":
        return cls(
            agents=(
                Agent("Chief Strategy Agent", "select ambitious product bets", "market fit"),
                Agent("Research Agent", "study comparable tools and docs", "evidence"),
                Agent("Product Manager Agent", "shape production scope", "requirements"),
                Agent("Architect Agent", "design modules and interfaces", "architecture"),
                Agent("Developer Agent", "write and refactor code", "implementation"),
                Agent("QA Agent", "test and open repair loops", "quality"),
                Agent("Security Agent", "block secrets and risky deploys", "safety"),
                Agent("DevOps Agent", "prepare release and operations", "deployment"),
                Agent("Reflection Agent", "turn lessons into skills", "memory"),
            )
        )

    def role_names(self) -> tuple[str, ...]:
        return tuple(agent.role for agent in self.agents)
