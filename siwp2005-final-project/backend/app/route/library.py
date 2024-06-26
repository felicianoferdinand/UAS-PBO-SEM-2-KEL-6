from flask import Flask, request, jsonify
from library_resource import Library

app = Flask(__name__)
library = Library()

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    data = request.get_json()
    student_name = data.get('student_name')
    book_name = data.get('book_name')
    if student_name and book_name:
        message = library.borrow_book(student_name, book_name)
        return jsonify({"message": message}), 200
    return jsonify({"message": "Invalid data"}), 400

@app.route('/borrow_computer', methods=['POST'])
def borrow_computer():
    data = request.get_json()
    user_name = data.get('user_name')
    computer_name = data.get('computer_name')
    if user_name and computer_name:
        message = library.borrow_computer(user_name, computer_name)
        return jsonify({"message": message}), 200
    return jsonify({"message": "Invalid data"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    books = library.view_books()
    return jsonify(books), 200

@app.route('/view_computers', methods=['GET'])
def view_computers():
    computers = library.view_computers()
    return jsonify(computers), 200

if __name__ == '__main__':
    app.run(debug=True)
