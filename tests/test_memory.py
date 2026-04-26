from __future__ import annotations

import unittest

from app.services.memory import MemoryLedger


class MemoryLedgerTest(unittest.TestCase):
    def test_recent_records(self) -> None:
        ledger = MemoryLedger()
        ledger.remember("first")
        ledger.remember("second")
        self.assertEqual(ledger.recent(1), ["second"])


if __name__ == "__main__":
    unittest.main()
