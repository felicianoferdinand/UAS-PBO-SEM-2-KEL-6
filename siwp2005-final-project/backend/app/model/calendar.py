class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f"{self.date}: {self.name}"


class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)
    
    def view_events(self):
        for event in self.events:
            print(event)

    def count_events_by_month(self, month):
        count = sum(1 for event in self.events if event.date.startswith(month))
        return count
