from flask import Flask, request, jsonify
from Model import Event, Calendar

app = Flask(__name__)
calendar = Calendar()

@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.get_json()
    name = data.get('name')
    date = data.get('date')
    if name and date:
        event = Event(name, date)
        calendar.add_event(event)
        return jsonify({"message": "Event added successfully"}), 200
    return jsonify({"message": "Invalid data"}), 400

@app.route('/view_events', methods=['GET'])
def view_events():
    events = [{"name": event.name, "date": event.date} for event in calendar.events]
    return jsonify(events), 200

@app.route('/count_events_by_month/<month>', methods=['GET'])
def count_events_by_month(month):
    count = calendar.count_events_by_month(month)
    return jsonify({"month": month, "count": count}), 200

if __name__ == '__main__':
    app.run(debug=True)
