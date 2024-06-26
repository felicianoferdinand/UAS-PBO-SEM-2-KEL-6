from flask import Flask, request, jsonify
from e_ticket_resource import ETicketManager

app = Flask(__name__)
ticket_manager = ETicketManager()

@app.route('/issue_ticket', methods=['POST'])
def issue_ticket():
    data = request.get_json()
    event_name = data.get('event_name')
    holder_name = data.get('holder_name')
    date = data.get('date')
    if event_name and holder_name and date:
        ticket = ticket_manager.issue_ticket(event_name, holder_name, date)
        return jsonify({"message": "Ticket issued successfully", "ticket_id": ticket.ticket_id}), 200
    return jsonify({"message": "Invalid data"}), 400

@app.route('/view_tickets', methods=['GET'])
def view_tickets():
    tickets = ticket_manager.view_tickets()
    response = [{"ticket_id": ticket.ticket_id, "event_name": ticket.event_name, "holder_name": ticket.holder_name, "date": ticket.date} for ticket in tickets]
    return jsonify(response), 200

@app.route('/verify_ticket/<ticket_id>', methods=['GET'])
def verify_ticket(ticket_id):
    ticket = ticket_manager.verify_ticket(ticket_id)
    if ticket:
        return jsonify({"valid": True, "ticket": str(ticket)}), 200
    return jsonify({"valid": False, "message": "Ticket not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
