"""
    - Cron expression
        - Minutes: 0 - 59
        - hour: 0: 23
        - Day of month: 1-31
        - month: 1-12
        - Day of week: Sunday - Saturday
        - Command -

        * - any value
        , - Value list separator
        - - Range
        / - Step values
"""

import sys
from constants import *
from field_parser import *


class CronExpression:

    def __init__(self, expression: str):
        self.expression = expression
        self.command = None
        self.values = []

    def parse(self):
        fields = self.expression.split(" ", 5)
        self.command = fields[-1]

        for i, s in enumerate(fields[:-1]):
            field_name = FIELD_NAMES[i]
            cf = Field(field_name, s)
            cf.parse()
            self.values.append(cf)

    def format_response(self):
        response = []
        for field in self.values:
            response.append(f"{field.name:<15}{str(field.values)}")
        response.append(f"{'command':<15}{self.command}")
        return "\n".join(response)


if __name__ == "__main__":
    # expression = "*/15 0 1,15 * * /usr/bin/find"
    expression = sys.argv[1]
    print(expression)
    exp = CronExpression(expression)
    exp.parse()
    print(exp.format_response())


