class Clock:
    def __init__(self, hours, minutes):
        self.set_hours_and_minutes(hours, minutes)

    def set_hours_and_minutes(self, hours, minutes):
        revised_minutes = minutes % 60
        hours = hours + (minutes - revised_minutes) / 60
        self.hours = hours % 24
        self.minutes = revised_minutes
        return self

    def add(self, minutes):
        sum_of_minutes = self.minutes + minutes
        return self.set_hours_and_minutes(self.hours, sum_of_minutes)

    def formatted(self, time):
        return "0" + str(time) if (len(str(time)) == 1) else str(time)

    def __eq__(self, other):
        return self.minutes == other.minutes and self.hours == other.hours

    def __str__(self):
        return self.formatted(self.hours) + ":" + self.formatted(self.minutes)
