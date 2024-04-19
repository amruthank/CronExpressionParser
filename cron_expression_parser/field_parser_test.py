import unittest
from field_parser import *


class TestField(unittest.TestCase):

    def test_field_parse_range(self):
        field = Field("hour", "1-5")
        field.parse()
        self.assertEqual(field.values, [1, 2, 3, 4, 5])

    def test_field_parse_list(self):
        field = Field("day of month", "1,2,3")
        field.parse()
        self.assertEqual(field.values, [1, 2, 3])

    def test_field_parse_step(self):
        field = Field("month", "*/2")
        field.parse()
        self.assertEqual(field.values, [1, 3, 5, 7, 9, 11])

    def test_field_parse_any(self):
        field = Field("day of week", "*")
        field.parse()
        self.assertEqual(field.values, [0, 1, 2, 3, 4, 5, 6])

    def test_field_parse_valid(self):
        field = Field("minute", "*/15")
        field.parse()
        self.assertEqual(field.values, [0, 15, 30, 45])

    def test_field_parse_invalid(self):
        field = Field("day of week", "*/15,1-8")
        with self.assertRaises(ValueError):
            field.parse()

if __name__ == '__main__':
    unittest.main()
