from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = 'flashcards_database.db'

# Function to connect to the SQLite database
def connect():
    return sqlite3.connect(DB_FILE)

# ... (Include the rest of your functions here)

@app.route('/flashcards', methods=['GET'])
def get_all_flashcards():
    connection = connect()
    flashcards = get_all_flashcards(connection, 'flashcards')
    connection.close()
    return jsonify(flashcards)


@app.route('/flashcards', methods=['POST'])
def add_flashcard():
    data = request.json
    connection = connect()
    add_flashcard(connection, 'flashcards', data['question'], data['answer'])
    connection.close()
    return jsonify({'message': 'Flashcard added successfully'})




if __name__ == '__main__':
    app.run(debug=True)
