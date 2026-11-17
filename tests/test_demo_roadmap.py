import unittest
from demo_roadmap import SAMPLE_ITEMS, summarize


class SummaryTests(unittest.TestCase):
    def test_active_count_excludes_closed_items(self):
        report = summarize(SAMPLE_ITEMS)
        self.assertEqual(report["active_items"], 3)
        self.assertEqual(report["excluded_items"], 1)

    def test_relationships_do_not_create_duplicate_items(self):
        report = summarize(SAMPLE_ITEMS)
        self.assertEqual(report["by_kind"]["Change Request"], 2)
        self.assertEqual(len(report["relationships"]), 2)


if __name__ == "__main__":
    unittest.main()
