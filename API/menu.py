# menu

from chatgptAPI import *
from pdf import *

import flashcards_database as flashcards_database
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



# test for database

def menu():
    connection = flashcards_database.connect()
    create_tables(connection, 'flashcards')
    flashcards_database.create_tables(connection, 'flashcards')



    m = '''Question 1: What is the mycelium?
    Answer 1: The mycelium is a network of thread-like structures hidden beneath the substrate, such as soil or wood, and is the true essence of the fungus.

    Question 2: How do mushrooms reproduce?
    Answer 2: Mushrooms reproduce through the production and dispersal of spores, which are released from the gills or pores under the mushroom cap.

    Question 3: What is mycorrhizae?
    Answer 3: Mycorrhizae is the symbiotic relationship between mushrooms and plants, in which the fungus aids the plant in nutrient absorption and the plant provides carbohydrates to the fungus.

    Question 4: What is the ecological importance of mushrooms as decomposers?
    Answer 4: Mushrooms break down complex organic compounds in dead plant and animal material, releasing essential nutrients back into the environment and contributing to nutrient cycling in ecosystems.

    Question 5: What are some potential medicinal properties of mushrooms?
    Answer 5: Some mushrooms, such as reishi and shiitake, are known for their potential immune-boosting, antiviral, and cholesterol-lowering properties, highlighting their potential applications in human health and well-being.'''

    a = text_to_dict(m)


    dict_to_flashcards(connection, 'flashcards', a)

    print(get_all_flashcards(connection, 'flashcards'))


