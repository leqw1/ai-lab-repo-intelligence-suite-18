from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MemoryLedger:
    records: list[str] = field(default_factory=list)

    def remember(self, record: str) -> None:
        cleaned = record.strip()
        if cleaned:
            self.records.append(cleaned)

    def recent(self, limit: int = 5) -> list[str]:
        return self.records[-limit:]
