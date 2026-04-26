from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class AuditTrail:
    entries: list[str] = field(default_factory=list)

    def record(self, actor: str, action: str) -> None:
        timestamp = datetime.now(timezone.utc).isoformat()
        self.entries.append(f"{timestamp} | {actor} | {action}")

    def recent(self, limit: int = 20) -> list[str]:
        return self.entries[-limit:]
