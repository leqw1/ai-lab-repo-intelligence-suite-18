import unittest

from app.services.audit_trail import AuditTrail


class AuditTrailTest(unittest.TestCase):
    def test_recent_keeps_entries(self):
        trail = AuditTrail()
        trail.record("qa", "tests passed")
        self.assertIn("tests passed", trail.recent()[0])
