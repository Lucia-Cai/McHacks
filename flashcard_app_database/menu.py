# menu

import flashcards_database

# if you want to create flashcard use: add_flashcard(connection, 'question', 'answer')

def ask_wrong_flashcards(connection, wrong_flashcards):
    for question in all_flashcards:
        # insert code to ask question
        # question is question[0] ans asnwer is question [1]

        if question_right: # put condition here
            update_answer(connection, question, 1)
        else:
            update_answer(connection, question, 0)
    
    connection.commit()

def ask_questions():
    connection = flashcards_database.connect()
    flashcards_database.create_tables(connection)

    #get all questions:
    all_flashcards = get_all_flashcards(connection)

    # ask all questions:
    for question in all_flashcards:
        # insert code to ask question
        # question is question[0] ans asnwer is question [1]

        if question_right: # put condition here
            update_answer(connection, question, 1)
        else:
            update_answer(connection, question, 0)
    
    connection.commit()
        
    
    
    # ask again flashcards that are wrong until user gets them all right
    wrong_flashcards = get_wrong_flashcards(connection)

    while wrong_flashcards.len > 0:
        ask_wrong_flashcards(connection, wrong_flashcards)
        wrong_flashcards = get_wrong_flashcards(connection)


    # when we're done
    connection.close()


