import unittest
import logic

class TestLogic(unittest.TestCase):

    def test_add_and_statistics(self):
        records = [
            {"id": 1, "title": "A", "category": "Cat1", "amount": 4, "completed": False},
            {"id": 2, "title": "B", "category": "Cat2", "amount": 2, "completed": True}
        ]
        logic.add_record(records, "C", "Cat1", 10)
        stats = logic.statistics(records)
        self.assertEqual(stats["total"], 3)
        self.assertEqual(stats["completed"], 1)
        self.assertEqual(stats["total_amount"], 16)
        self.assertEqual(stats["by_category"]["Cat1"], 14)

    def test_find_case_insensitive(self):
        records = [{"id": 1, "title": "Python", "category": "study", "amount": 1, "completed": False}]
        found = logic.find_records(records, "python")
        self.assertEqual(len(found), 1)

    def test_set_completed_unknown_id(self):
        records = [{"id": 1, "title": "A", "category": "Cat", "amount": 1, "completed": False}]
        result = logic.set_completed(records, 99, True)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
