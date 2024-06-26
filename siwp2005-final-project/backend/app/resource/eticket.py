from e_ticket_model import ETicket
import uuid

class ETicketManager:
    def __init__(self):
        self.tickets = []

    def issue_ticket(self, event_name, holder_name, date):
        ticket_id = str(uuid.uuid4())
        ticket = ETicket(event_name, holder_name, date, ticket_id)
        self.tickets.append(ticket)
        return ticket

    def view_tickets(self):
        return self.tickets

    def verify_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None
