from constants import *

class Field:

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.values = []

    def parse(self):
        if RANGE_OF_VALUES in self.value:
            list_of_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
            start, end = self.value.split("-")
            if start.isnumeric():
                start = int(start)
            else:
                start = list_of_day.index(start)

            if end.isnumeric():
                end = int(end)
            else:
                end = list_of_day.index(end)
            if start < end:
                self.values = list(range(start, end + 1))
            else:
                self.values = list(range(start,self.getMax()+1))
                self.values.extend(list(range(0, end+1)))

        elif STEP_VALUES in self.value:
            list_of_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
            try:
                _, step = self.value.split(STEP_VALUES)
            except Exception:
                raise ValueError(f"Invalid cron expression for the field {self.name} - {self.value}")
            else:
                step = int(step)
            if step > self.getMax():
                raise ValueError(f"Invalid cron expression for the field {self.name} - {self.value}")
            for num in range(self.getMin(), self.getMax()+1):
                if (num-self.getMin())%step == 0:
                    self.values.append(num)
        elif VALUE_LIST_SEPARATOR in self.value:
            list_of_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
            parts = self.value.split(",")
            for part in parts:
                if part == "*":
                    continue
                elif STEP_VALUES in part:
                    step_parts = part.split(STEP_VALUES)
                    if len(step_parts) != 2:
                        raise ValueError(f"Invalid cron field value for {self.name}: {self.value}")
                    else:
                        if int(step_parts[1]) > self.getMax():
                            raise ValueError(f"Invalid cron field value for {self.name}: {self.value}")
                        for num in range(self.getMin(), self.getMax() + 1):
                            if (num - self.getMin()) % step_parts[1]:
                                self.values.append(num)
                elif RANGE_OF_VALUES in part:
                    start, end = part.split("-")
                    if start.isnumeric():
                        start = int(start)
                    else:
                        start = list_of_day.index(start)

                    if end.isnumeric():
                        end = int(end)
                    else:
                        end = list_of_day.index(end)

                    self.values.extend(list(start, end+1))
                else:
                    self.values.append(int(part))
        elif self.value == ANY_VALUE:
            self.values = list(range(self.getMin(), self.getMax() + 1))
        else:
            self.values = [int(self.value)]

    def getMin(self):
        min_values = [0, 0, 1, 1, 0]
        return min_values[FIELD_NAMES.index(self.name)]

    def getMax(self):
        max_values = [59, 23, 31, 12, 6]
        return max_values[FIELD_NAMES.index(self.name)]