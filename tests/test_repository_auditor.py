from pathlib import Path
import shutil
import unittest

from app.services.repository_auditor import RepositoryAuditor


class RepositoryAuditorTest(unittest.TestCase):
    def test_counts_files_without_accepting_env(self):
        root = Path("tmp_test_repository_auditor")
        if root.exists():
            shutil.rmtree(root)
        try:
            root.mkdir()
            (root / "README.md").write_text("ok", encoding="utf-8")
            (root / "tests").mkdir()
            (root / "tests" / "test_demo.py").write_text("def test_ok(): pass", encoding="utf-8")
            audit = RepositoryAuditor().audit(root)
        finally:
            if root.exists():
                shutil.rmtree(root)
        self.assertEqual(audit.files, 2)
        self.assertEqual(audit.warnings, ())
