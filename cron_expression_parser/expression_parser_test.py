import unittest
from expression_parser import *

class TestCronExpression(unittest.TestCase):

    def test_cron_expression_parse_valid(self):
        valid_cron_expression = "*/15 0 1,15 * 1-5 /usr/bin/find"
        expression = CronExpression(valid_cron_expression)
        expression.parse()
        assert len(expression.values) == 5

    def test_cron_expression_parse_invalid(self):
        invalid_cron_expression = "*-/15 0 1,15 * 1-5 * /usr/bin/find"
        expression = CronExpression(invalid_cron_expression)
        with self.assertRaises(ValueError):
            expression.parse()


if __name__ == '__main__':
    unittest.main()


