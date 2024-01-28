from flask import Flask, jsonify, request
import flashcards_database
from chatgptAPI import *
from pdf import *

app = Flask(__name__)

@app.route('/api/flashcards', methods=['GET'])
def get_all_flashcards():
    connection = flashcards_database.connect()
    flashcards = flashcards_database.get_all_flashcards(connection, 'flashcards')
    return jsonify({'flashcards': flashcards})


@app.route('/api/add_flashcard', methods=['POST'])
def add_flashcard():
    data = request.json
    question = data['question']
    answer = data['answer']
    connection = flashcards_database.connect()
    flashcards_database.add_flashcard(connection, 'flashcards', question, answer)
    return jsonify({'message': 'Flashcard added successfully'})

# Add more routes for other functions as needed

if __name__ == '__main__':
    connection = flashcards_database.connect()
    flashcards_database.create_tables(connection, 'flashcards')
    a = text_to_dict(m)
    flashcards_database.dict_to_flashcards(connection, 'flashcards', a)
    app.run(debug=True)
