import sqlite3

# table_name = 'flashcards'

# CREATE_FLASHCARDS_TABLE = f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, result BOOLEAN);'

# ADD_FLASHCARD = f'INSERT INTO {table_name} (question, answer, result) VALUES (?, ?, ?);'

# GET_ALL_FLASHCARDS = f'SELECT * FROM {table_name};'

# GET_WRONG_FLASHCARDS = f'SELECT * FROM {table_name} WHERE relsult = False;'

# CHANGE_RESULT = f'''
# UPDATE {table_name}
# SET result = (?)
# WHERE question = (?)'''

# DELETE_ROW = f'DELETE FROM {table_name} WHERE question = (?)'

def connect():
    return sqlite3.connect('flashcards_database.db') # sqlite3 works with files, if file does not exist it creates it

def create_tables(connection, table_name):
    with connection:
        connection.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, question TEXT, answer TEXT, result BOOLEAN);')


def add_flashcard(connection, table_name, question, answer, result = False):
    with connection:
        connection.execute(f'INSERT INTO {table_name} (question, answer, result) VALUES (?, ?, ?);', (question, answer, result))

def dict_to_flashcards(connection, table_name, dict):
    for question, answer in dict.items():
        add_flashcard(connection, table_name, question, answer)

def get_all_flashcards(connection, table_name):
    with connection:
        return connection.execute(f'SELECT * FROM {table_name};').fetchall()

def get_wrong_flashcards(connection, table_name):
    with connection:
        return connection.execute(f'SELECT * FROM {table_name} WHERE relsult = False;').fetchall()

def update_answer(connection, table_name, question, new_result):
    with connection:
        connection.execute(f'''
                            UPDATE {table_name}
                            SET result = (?)
                            WHERE question = (?)'''\
                                , (table_name, new_result, question))


def remove_question(connection, table_name, question):
    with connection:
        connection.execute(f'DELETE FROM {table_name} WHERE question = (?)', (question))
        connection.commit()




