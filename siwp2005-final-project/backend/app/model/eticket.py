class ETicket:
    def __init__(self, event_name, holder_name, date, ticket_id):
        self.event_name = event_name
        self.holder_name = holder_name
        self.date = date
        self.ticket_id = ticket_id

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Event: {self.event_name}, Holder: {self.holder_name}, Date: {self.date}"
