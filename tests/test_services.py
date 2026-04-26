from __future__ import annotations

import unittest

from app.services.agent_company import AgentCompany
from app.services.project_board import ProjectBoard
from app.services.risk_engine import RiskEngine


class ServicesTest(unittest.TestCase):
    def test_company_has_production_roles(self) -> None:
        roles = AgentCompany.default().role_names()
        self.assertIn("Chief Strategy Agent", roles)
        self.assertIn("Security Agent", roles)
        self.assertGreaterEqual(len(roles), 8)

    def test_risk_engine_reports_owner_approval_warning(self) -> None:
        report = RiskEngine().evaluate_board(ProjectBoard.demo())
        self.assertGreater(report.score, 0)
        self.assertIn("owner approval pending", report.warnings)


if __name__ == "__main__":
    unittest.main()
