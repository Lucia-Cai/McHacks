# menu

import flashcards_database
from flashcards_database import *

# if you want to create flashcard use: add_flashcard(connection, 'question', 'answer')

def ask_wrong_flashcards(connection, table_name, wrong_flashcards):
    for question in all_flashcards:
        # insert code to ask question
        # question is question[0] ans asnwer is question [1]

        if question_right: # put condition here
            update_answer(connection, table_name, question, True)
        else:
            update_answer(connection, table_name, question, False)
    
    connection.commit()

# ask questions from a specific table from the database flashcards_database
def ask_questions(table_name):
    connection = flashcards_database.connect()
    flashcards_database.create_tables(connection, table_name)

    #get all questions:
    all_flashcards = get_all_flashcards(connection, table_name)

    # ask all questions:
    for question in all_flashcards:
        # insert code to ask question
        # question is question[0] ans asnwer is question [1]

        if question_right: # put condition here
            update_answer(connection, table_name, question, True)
        else:
            update_answer(connection, table_name, question, False)
    
    connection.commit()
        
    
    
    # ask again flashcards that are wrong until user gets them all right
    wrong_flashcards = get_wrong_flashcards(connection, table_name)

    while wrong_flashcards.len > 0:
        ask_wrong_flashcards(connection, table_name, wrong_flashcards)
        wrong_flashcards = get_wrong_flashcards(connection, table_name)


    # when we're done
    connection.close()


def menu():
    connection = flashcards_database.connect()
    connection.execute('DROP TABLE IF EXISTS flashcards')
    flashcards_database.create_tables(connection, 'flashcards')

    print(get_all_flashcards(connection, 'flashcards'))

menu()

