import unittest

from app.services.readiness_score import ReadinessScorer
from app.services.repository_auditor import RepositoryAudit


class ReadinessScorerTest(unittest.TestCase):
    def test_ready_requires_real_surface(self):
        audit = RepositoryAudit(files=40, python_files=14, tests=5, docs=7, warnings=())
        score = ReadinessScorer().score(audit)
        self.assertEqual(score.decision, "ready")
        self.assertGreaterEqual(score.score, 85)
