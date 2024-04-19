# CronExpressionParser
    Cron expression parser is a python3 program it parsers cron expression into a human readable format.
    The input will be space separated cron expression such as minute, hour, day of month, month, and day of week) and a command.
    The output is formatted as a table with the field name taking the first 14 columns and the times as a space-separated list

    For example:
        The following input argument:
            */15 0 1,15 * 1-5 /usr/bin/find
        
        The following is the output format:
            minute 0 15 30 45
            hour 0
            day of month 1 15
            month 1 2 3 4 5 6 7 8 9 10 11 12
            day of week 1 2 3 4 5
            command /usr/bin/find
    

# System Requirements:
    1. Python >= 3.10 

# Usage
    1. Clone the repository to your local.
    2. Open the terminal at  cron_expression_parser directory. cron_expression_parser directory is present inside the root directory.
    3. Run following command:
        => python3 expression_parser.py  "*/15 0 1,15 * * /usr/bin/find"
        Replace the argument with your cron expression.
    4. For the above input, you should be able to see the above mentioned output on your terminal.
    5. To run the test files, you can use the following commands.
        => python -m unittest *_test.py




    
        