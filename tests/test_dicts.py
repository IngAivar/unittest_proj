import unittest
from utils import dicts


class TestDicts(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({"val": "mater"}, "val", "nope"), "mater")
        self.assertEqual(dicts.get_val({"val": "mater"}, "fill", "nope"), "nope")
        self.assertEqual(dicts.get_val({"val": "mater"}, "fill"), "git")
