import importlib.util
import unittest
from argparse import Namespace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("skill_manager", ROOT / "scripts/skill-manager.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SkillManagerTests(unittest.TestCase):
    def test_catalog_has_one_managed_skill(self):
        self.assertEqual(MODULE.names_in_catalog(), {"business-algorithm-visualizer"})

    def test_managed_skill_has_skill_file(self):
        skill = ROOT / "skills/business-algorithm-visualizer/SKILL.md"
        self.assertTrue(skill.is_file())
        self.assertEqual(MODULE.read_frontmatter(skill)["name"], "business-algorithm-visualizer")

    def test_validate(self):
        self.assertEqual(MODULE.cmd_validate(Namespace()), 0)


if __name__ == "__main__":
    unittest.main()
