#flashcards database

import sqlite3

CREATE_FLASHCARDS_TABLE = 'CREATE TABLE IF NOT EXISTS flashcards (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, result INTEGER);'

ADD_FLASHCARD = 'INSERT INTO flashcards (question, answer, result) VALUES (?, ?, ?);'

GET_ALL_FLASHCARDS = 'SELECT * FROM flashcards;'

GET_WRONG_FLASHCARDS = 'SELECT * FROM FLASHCARDS WHERE relsult = 0;'

CHANGE_RESULT = '''
UPDATE flashcards
SET result = (?)
WHERE question = (?)'''

def connect():
    return sqlite3.connect('flashcards_database.db') # sqlite3 works with files, if file does not exist it creates it

def create_tables(connection):
    with connection:
        connection.execute(CREATE_FLASHCARDS_TABLE)

def add_flashcard(connection, question, answer, result = 0):
    with connection:
        connection.execute(ADD_FLASHCARD, (question, answer, result))

def get_all_flashcards(connection):
    with connection:
        return connection.execute(GET_ALL_FLASHCARDS).fetchall()

def get_wrong_flashcards(connection):
    with connection:
        return connection.execute(GET_WRONG_FLASHCARDS).fetchall()

def update_answer(connection, question, new_result):
    with connection:
        connection.execute(CHANGE_RESULT, (new_result, question))







