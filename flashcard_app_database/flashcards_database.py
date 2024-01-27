#flashcards database

import sqlite3

CREATE_FLASHCARDS_TABLE = 'CREATE TABLE IF NOT EXISTS flashcards (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, result INTEGER);'

INSERT_FLASHCARD = 'INSERT INTO flashcards (question, answer, result) VALUES (?, ?, ?);'

GET_ALL_FLASHCARDS = 'SELECT * FROM flashcards;'

GET_WRONG_FLASHCARDS = 'SELECT * FROM FLASHCARDS WHERE relsult = 0;'

def connect():
    return sqlite3.connect('flashcards_database.db') # sqlite3 works with files, if file does not exist it creates it

def create_tables(connection):
    with connection:
        connection.execute(CREATE_FLASHCARDS_TABLE)

def add_bean(connection, question, answer, result = 0):
    with connection:
        connection.execute(CREATE_FLASHCARDS_TABLE, (question, answer, result))

def get_all_flashcards(connection):
    with connection:
        connection.execute(GET_ALL_FLASHCARDS)

def get_wrong_flashcards(connection):
    with connection:
        connection.execute(GET_WRONG_FLASHCARDS)
