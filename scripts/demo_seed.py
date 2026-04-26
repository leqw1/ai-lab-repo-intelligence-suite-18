from __future__ import annotations

from app.services.memory import MemoryLedger


def build_demo_memory() -> MemoryLedger:
    ledger = MemoryLedger()
    ledger.remember("Keep production scope explicit before writing code.")
    ledger.remember("Block publication until owner approval.")
    return ledger
