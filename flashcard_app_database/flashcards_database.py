#flashcards database

import sqlite3

table_name = 'flashcards'

CREATE_FLASHCARDS_TABLE = f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, result BOOLEAN);'

ADD_FLASHCARD = f'INSERT INTO {table_name} (question, answer, result) VALUES (?, ?, ?);'

GET_ALL_FLASHCARDS = f'SELECT * FROM {table_name};'

GET_WRONG_FLASHCARDS = f'SELECT * FROM {table_name} WHERE relsult = False;'

CHANGE_RESULT = f'''
UPDATE {table_name}
SET result = (?)
WHERE question = (?)'''

DELETE_ROW = f'DELETE FROM {table_name} WHERE question = (?)'

def connect():
    return sqlite3.connect('flashcards_database.db') # sqlite3 works with files, if file does not exist it creates it

def create_tables(connection):
    with connection:
        connection.execute(CREATE_FLASHCARDS_TABLE)

def add_flashcard(connection, question, answer, result = False):
    with connection:
        connection.execute(ADD_FLASHCARD, (question, answer, result))

def dict_to_flashcards(connection, dict):
    for question, answer in enumerate(dict.items()):
        add_flashcard(connection, question, answer)

def get_all_flashcards(connection):
    with connection:
        return connection.execute(GET_ALL_FLASHCARDS).fetchall()

def get_wrong_flashcards(connection):
    with connection:
        return connection.execute(GET_WRONG_FLASHCARDS).fetchall()

def update_answer(connection, question, new_result):
    with connection:
        connection.execute(CHANGE_RESULT, (table_name, new_result, question))


def remove_question(connection, question):
    with connection:
        connection.execute(DELETE_ROW, (question))
        connection.commit()




